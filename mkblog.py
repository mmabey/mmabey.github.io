#! /usr/bin/env python3
# *-* coding: utf-8 *-*

import json
import logging
import sys
from os import walk, rename, mkdir
from os.path import join, abspath
from re import compile, search, sub
from shutil import copytree, rmtree
from subprocess import call

from bs4 import BeautifulSoup

BUILD_DIR = abspath('_build/html')
BLOG_DIR = 'blog'
INDEX_FILE = join(BLOG_DIR, 'index.md')
MONTH = ('',  # Makes it so we don't have to do any subtraction later
         'Jan',
         'Feb',
         'Mar',
         'Apr',
         'May',
         'Jun',
         'Jul',
         'Aug',
         'Sep',
         'Oct',
         'Nov',
         'Dec')

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def get_entry_metadata(filename):
    """Extract the metadata from the entry at `filename`.

    See https://caddyserver.com/docs/markdown for details.

    :param str filename: Path to the blog entry to parse.
    :return: The metadata from the top portion of the entry.
    :rtype: dict
    """
    logging.debug('Extracting metadata from file: {}'.format(filename))
    with open(filename) as fin:
        json_header = ''
        started = False
        line_num = 0
        for line in fin:
            line_num += 1
            logging.debug('On line {}'.format(line_num))
            if not started and '{' in line:
                json_header += line
                started = True
            elif started:
                json_header += line
                if '}' in line:
                    break
    logging.debug('Header contents:\n{}'.format(json_header))
    data = json.loads(json_header)
    data['link'] = '/{}'.format(filename)
    data['tag-classes'] = process_tags(data.get('tags', []))
    return data


def process_tags(tags_list):
    """Turn the list of tags into a string of CSS classes.

    :param list tags_list: List of tags for the entry.
    :return: String of space-delimited tags, formatted to be valid CSS class
        names.
    :rtype: str
    """
    tags = []
    for tag in tags_list:
        tags.append(transform_tag(tag))

    return ' '.join(tags)


def transform_tag(tag):
    """Remove charaters that would make the tag an invalid CSS class name.

    :param str tag: A single tag.
    :return: The transformed version of the tag.
    :rtype: str
    """
    table = {ord(' '): '_',
             ord('.'): '-'}
    tag = tag.strip().translate(table)
    # Remove any other invalid characters
    return sub(r'[^a-zA-Z0-9_\-]', r'', tag)


def get_entry_sort_key(item):
    """Return sort key.

    Used by :function:`sorted()` in :function:`add_entries_to_index` to order
    entries by the day they were created.

    :param dict item: Item from the dict of entries.
    :return: The day the entry was posted.
    :rtype: int
    """
    return item['day']


def add_entries_to_index(entries):
    """Add all the blog entries to the blog index.

    Creates a new index (overwriting if it exists) of the blog posts in
    Markdown format.

    :param dict entries: The set of blog entries as obtained by walking
        through the /blog directory and getting the entry metadata using the
        :function:`get_entry_metadata` function.
    :rtype: None
    """
    index_meta = {'template': 'blog',
                  'title': 'Blog Index',
                  'heading': '/var/log/mike',
                  'subheading': "Mike's Blog",
                  'NOTE!!!!!!': 'Don\'t forget! Do NOT edit this file!!! Your changes WILL be lost!'
                  }
    with open(INDEX_FILE, 'w') as idx:  # By default 'w' mode erases an existing file with the same name
        # Add metadata for the blog index
        idx.write(json.dumps(index_meta, indent=2))

        # No title (usually signified as "# Title") should be added since Sphinx will add it for us
        for year in sorted(entries, reverse=True):
            year_tags = {"entry"}
            year_str = ''
            for month in sorted(entries[year], reverse=True):
                for entry in sorted(entries[year][month], key=get_entry_sort_key, reverse=True):
                    year_str += '<li class="entry hidden_entry {tag-classes}"> {Month} {day}: <a href="{link}">{title}</a></li>\n'.\
                        format(Month=MONTH[int(month)], **entry)
                    try:
                        year_tags |= set(entry['tags'])
                    except KeyError:
                        pass

            year_str += '</ul>\n'
            _tags = process_tags(year_tags)
            idx.write('\n<h2 class="{t}">{y}</h2>\n\n<ul class="{t}">\n{a}'.format(t=_tags, y=year, a=year_str))


def mod_toc():
    """Modify the "internal" links in the table of contents.

    When Sphinx compiles the blog template, it creates links in the table of
    contents that are relative to the root of the web site. This makes them all
    invalid from any blog files. To fix this, a '/' is inserted at the
    beginning of each link to turn them into absolute links instead of
    relative.

    :rtype: None
    """
    # Move the blog template to where Caddy expects it to be
    try:
        mkdir(join(BUILD_DIR, '_templates'))
    except FileExistsError:
        pass  # Dir already existed
    template_dest = join(BUILD_DIR, '_templates', 'blog_template.html')
    rename(join(BUILD_DIR, 'blog_template.html'), template_dest)

    # Read in the template, make a soup object
    with open(template_dest) as markup:
        soup = BeautifulSoup(markup.read(), 'lxml')

    # Change all "internal" links to start with '/'
    div = soup.select('div.wy-menu.wy-menu-vertical')[0]
    for link in div.select('a.reference.internal'):
        link['href'] = '/{}'.format(link['href'])

    # Make the TOC item for "Blog" current so it's highlighted
    for list_item in soup.select('li.toctree-l1'):
        if list(list_item.children)[0].string == 'Blog':
            list_item['class'] += ['current']
            break  # Got what we came for

    with open(template_dest, 'w') as markup:
        markup.write(soup.prettify('utf-8').decode('utf-8'))


def make_entry_dir(meta):
    # Get the year and month where this entry belongs
    year = str(meta['year'])
    month = '{:02}'.format(meta['month'])

    # Make dir where it's supposed to be
    for new_dir in (BLOG_DIR, join(BLOG_DIR, year), join(BLOG_DIR, year, month)):
        try:
            mkdir(new_dir)
        except FileExistsError:
            pass  # Dir already existed

    return year, month


def main():
    """Organize blog posts, prepare for publishing to web.

    Walks through the `blog` directory looking for entries. Entries should be
    organized into directories in the form `blog/<year>/<month>/`, where
    `<year>` and `<month>` should correspond to the values found in the entry's
    metadata (see :function:`get_entry_metadata`). If not, the entry will be
    moved to the correct directory and the process will be restarted.

    Once all the metadata for each entry has been collected, it is added to the
    index of blog entries, then all the source files are moved to the build dir
    where it will then be ready to be served by the web server.

    :rtype: None
    """
    # Cycle through the blog directories, get the info to create the index
    date_pat = compile(r'blog/(\d{4})/(\d{2})')
    entries = {}
    ttl = 0
    dirty_tree = False

    # First see if there are any files in the base blog dir that need to be placed elsewhere
    for root, dirs, files in walk(BLOG_DIR):
        for f in files:
            if f.endswith('.md') and f not in ('index.md', 'sample_blog.md'):
                meta = get_entry_metadata(join(root, f))
                year, month = make_entry_dir(meta)
                logging.info('Moving unsorted entry "{}" to the proper folder: {}/{}'.format(f, year, month))

                # Move the file
                rename(join(root, f), join(BLOG_DIR, year, month, f))

        # Just do the blog dir, nothing else
        break

    for root, dirs, files in walk(BLOG_DIR):
        m = search(date_pat, root)
        if not m:
            # Skip any dirs that don't match the pattern we're looking for
            continue

        year = m.group(1)
        month = m.group(2)

        if not len(files):
            # Remove this empty dir
            rmtree(root)

        for f in files:
            if f.startswith('.') or not f.endswith('.md'):
                # Skip files that start with '.' or that don't have the Markdown extension
                continue

            # Check that the published date in the metadata matches the dir it's in
            meta = get_entry_metadata(join(root, f))
            if year != str(meta['year']) or month != '{:02}'.format(meta['month']):
                dirty_tree = True
                logging.warning('DIRTY TREE DETECTED: Files not in the proper folder by date. Will need to re-parse '
                                'the directory of blog posts.')

                # Make dir where this entry is supposed to be, get actual year and month back
                year, month = make_entry_dir(meta)

                # Move the file
                rename(join(root, f), join(BLOG_DIR, year, month, f))

            # Make sure this year and month are in `entries`
            if year not in entries:
                entries[year] = {}
            if month not in entries[year]:
                entries[year][month] = []

            entries[year][month].append(meta)
            ttl += 1

    # If we had to move things around, just start over
    if dirty_tree:
        del entries
        logging.info('Beginning re-parsing of blog directory...')
        return main()

    add_entries_to_index(entries)
    logging.info('Added {} entries to blog index'.format(ttl))

    # Copy all source files to the _build directory
    call(['rsync', '-rcv', '--delete', '--exclude=blog/sample_blog.md', BLOG_DIR, BUILD_DIR])
    logging.info('Copy to build dir ({}/blog) complete'.format(BUILD_DIR))

    mod_toc()


if __name__ == '__main__':
    main()
