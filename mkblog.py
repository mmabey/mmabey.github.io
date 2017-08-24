#! /usr/bin/env python3
# *-* coding: utf-8 *-*

import logging
import sys
from datetime import datetime
from os import walk, rename, mkdir
from os.path import join, abspath, exists
from re import compile, search, sub
from shutil import rmtree
from tempfile import TemporaryFile

BUILD_DIR = abspath('_build/html')
BLOG_DIR = 'blog'
INDEX_FILE = join(BLOG_DIR, 'index.md')
HEADER_FIELD_PAT = compile(r':(.*): (.*)$')
TITLE_PAT = compile(r'^# (.*)$')
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

    :param str filename: Path to the blog entry to parse.
    :return: The metadata from the top portion of the entry.
    :rtype: dict
    """
    logging.debug('Extracting metadata from file: {}'.format(filename))
    data = {}
    started = False
    looking_for_title = False
    add_title_to_metadata = True
    line_num = 0
    with open(filename) as fin:
        for line in fin:
            line_num += 1
            logging.debug('On line {}'.format(line_num))
            if not started and '```eval_rst' in line:
                started = True
            elif looking_for_title:
                m = search(TITLE_PAT, line)
                if m:
                    data['title'] = m.group(1)
                    break
            elif started and '```' in line:
                if not data.get('title'):
                    looking_for_title = True
                else:
                    add_title_to_metadata = False
                    break
            elif started:
                m = search(HEADER_FIELD_PAT, line)
                if m:
                    val = m.group(2)
                    if m.group(1) in ('day', 'month', 'year'):
                        val = int(val)
                    data[m.group(1)] = val

    metadata_to_add = ''
    # Add title to the metadata if not already there
    if add_title_to_metadata:
        metadata_to_add += ':title: {}\n'.format(data['title'])

    # Calculate the ISO 8601 format of the date published, add to metadata
    if not (data.get('datePublished') and data.get('dateModified')):
        try:
            the_date = datetime(data['year'], data['month'], data['day']).isoformat()
        except ValueError:
            print('Error processing file: {}'.format(filename))
            raise
        data['datePublished'] = data['dateModified'] = the_date
        metadata_to_add += ':datePublished: {0}\n:dateModified: {0}\n'.format(the_date)

    # If there's new metadata to add, rewrite the original post file
    if len(metadata_to_add):
        add_extras_to_metadata(filename, metadata_to_add)

    # Sphinx will compile the file to HTML and change the extension
    filename = ''.join([filename.rsplit('.')[0], '.html'])
    data['link'] = '/{}'.format(filename)
    data['tags'] = [x.strip() for x in data.get('tags', '').split(',')]
    if data.get('year'):
        data['tags'].append(str(data['year']))
    data['tag-classes'] = process_tags(data['tags'])
    return data


def add_extras_to_metadata(filename, metadata_str):
    """Add the metadata string to the file at filename.

    :param str filename: Path to the file to add the metadata to.
    :param str metadata_str: The metadata as a string.
    :rtype: None
    """
    started = False  # Set when we've found the first "```"
    finished = False  # Set when we've written out the new metadata
    with TemporaryFile('w+') as tmp:
        with open(filename) as orig:
            for line in orig:
                if finished:
                    tmp.write(line)  # Write the original line to the temp file
                    continue

                if not started and '```' in line:
                    tmp.write(line)  # Write the original line to the temp file
                    started = True
                elif started and '```' in line:  # Add metadata before this block ends
                    tmp.write(metadata_str)
                    tmp.write(line)  # Write the original line to the temp file
                    finished = True
                else:
                    tmp.write(line)  # Write the original line to the temp file

        # Copy the temp file to the original file
        tmp.seek(0)
        with open(filename, 'w') as orig:
            orig.write(tmp.read())


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


def add_entries_to_index(entries):
    """Add all the blog entries to the blog index.

    Creates a new index (overwriting if it exists) of the blog posts in
    Markdown format.

    :param dict entries: The set of blog entries as obtained by walking
        through the /blog directory and getting the entry metadata using the
        :function:`get_entry_metadata` function.
    :rtype: None
    """
    index_meta = '```eval_rst\n' \
                 ':heading: /var/log/mike\n' \
                 ':subheading: Mike\'s Blog\n' \
                 ':doc_type: blog\n' \
                 ':reminder: Don\'t forget! Do NOT edit this file!!! Your changes WILL be lost!\n' \
                 '```\n' \
                 '# Blog Index\n'
    with open(INDEX_FILE, 'w') as idx:  # By default 'w' mode erases an existing file with the same name
        # Add metadata and title for the blog index
        idx.write(index_meta)

        for year in sorted(entries, reverse=True):
            year_tags = {"entry"}
            year_str = ''
            for month in sorted(entries[year], reverse=True):
                for entry in sorted(entries[year][month], key=lambda item: item['day'], reverse=True):
                    year_str += '<li class="entry hidden_entry {tag-classes}"> {Month} {day}: ' \
                                '<a href="{link}">{title}</a></li>\n'.\
                        format(Month=MONTH[int(month)][:3], **entry)
                    try:
                        year_tags |= set(entry['tags'])
                    except KeyError:
                        pass

            year_str += '</ul>\n'
            _tags = process_tags(year_tags)
            idx.write('\n<h2 class="{t}">{y}</h2>\n\n<ul class="{t}">\n{a}'.format(t=_tags, y=year, a=year_str))

        # Make the table of contents tree
        idx.write('\n'
                  '```eval_rst\n'
                  '.. toctree::\n'
                  '   :hidden:\n'
                  '   :maxdepth: 1\n'
                  '\n')
        for year in sorted(entries, reverse=True):
            ensure_year_redirect(year)
            idx.write('   {0} Entries <{0}/index>\n'.format(year))
        idx.write('```\n')


def ensure_year_redirect(year):
    """Create the redirect file for the blog year if it doesn't already exist.

    :param int year: The blog subdirectory to check for the redirect file.
    :rtype: None
    """
    year = str(year)
    redir_file = join(BLOG_DIR, year, 'index.rst')
    if not exists(redir_file):
        with open(redir_file, 'w') as redir:
            redir.write('{bar}\n{year}\n{bar}\n'.format(bar='=' * len(year), year=year))
            redir.write('|redir|\n'
                        '\n'
                        '.. |redir| raw:: html\n'
                        '\n'
                        '   <script language="javascript">window.location.href = "/blog/?tag={}"</script>\n'
                        .format(year))


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


if __name__ == '__main__':
    main()
