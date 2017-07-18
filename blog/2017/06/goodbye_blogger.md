```eval_rst
:heading: /var/log/mike
:subheading: Mike's Blog
:doc_type: blog

:orig_link: http://mikemabey.blogspot.com/2017/06/goodbye-blogger.html
:tags: blog, Blogger, Markdown, Sphinx, git, website, mikemabey.com, Jinja, reStructuredText, RST, Caddy, HTTPS, gist
:day: 3
:month: 6
:year: 2017
:title: Goodbye Blogger!
```
# Goodbye Blogger!

Blogger has been good to me over the years. I set up my first blog on Blogger before I had any other digital real estate
to speak of. But ever since setting up [mikemabey.com](https://mikemabey.com), I've been looking for a way to migrate
off of Blogger and have everything all together on the same site. I recently completed that objective, and in this post
I'll share how I did it and what obstacles I encountered along the way.

Naturally, this is the final post I'll share on Blogger. Future blog entries will be available on the
[blog](https://blog.mikemabey.com) section of [my website](https://mikemabey.com).


## TL;DR

I write posts in [Markdown](https://daringfireball.net/projects/markdown/), which are processed by
[Sphinx](http://www.sphinx-doc.org/) which [supports Markdown](http://www.sphinx-doc.org/en/stable/markdown.html) via
[recommonmark](http://recommonmark.readthedocs.io/en/latest/index.html). I emulate support for tags using some custom
JavaScript and CSS, and I generate an index of entries with a Python script.


## Background

The source of my website is written in [reStructuredText](http://docutils.sourceforge.net/docs/user/rst/quickref.html)
(RST), a markup language favored by Python programmers in their documentation. I compile the source using
[Sphinx](http://www.sphinx-doc.org/), a documentation generation tool that can render RST into many formats, including
HTML, PDF, LaTeX, etc.

Sphinx uses [Jinja](http://jinja.pocoo.org/) templates to make everything more modular and customizable. You configure
the template for your docs, then Sphinx takes the relatively simple body of a document and renders it using the
template. It's pretty slick.


## Objectives

When migrating to my own site, I wanted to retain the following features from Blogger:

- Tags: On Blogger, each entry can have some tags indicating topics covered by the post. You can also filter posts by
  these tags to see other posts on the same topic.
- Search: Blogger has a search function available to users.
- Analytics: Blogger provides statistics on which pages have been visited how many times. It has been fun to watch a
  few of my posts reach certain page view milestones.

In addition to the above, I also wanted to add the following new features:

- Markdown: The idea of writing posts in Markdown really appeals to me. Of course, plain text files make it easy to
  maintain and keep track of using [git](https://git-scm.com/). It also lowers the barrier to writing new posts due to
  its simplicity and because I don't have to have web access.
- Web Hook: By changing my publication flow to incorporate git, it makes a lot of sense to incorporate web hooks to
  automatically update content on my site when I push new commits and thereby eliminate the need for FTP.


## First Attempt

Some of the objectives I listed above were actually inspired by the feature set of [Caddy](https://caddyserver.com/),
the first web server ever to provide automatic HTTPS _by default_. Caddy also supports rendering
[Markup](https://caddyserver.com/docs/markdown) as HTML on demand as well as [git
integration](https://caddyserver.com/docs/http.git).

### Markdown

Caddy's Markdown support is pretty cool. You can create a template using syntax defined in Go's
[text/template](http://golang.org/pkg/text/template/) package, which isn't that dissimilar to
[Jinja](http://jinja.pocoo.org/) syntax. I attempted using this by first rendering a very simple RST document to HTML,
then adding the template parameters to the HTML file where I needed Caddy to fill in some details, and used this as the
template for blog entries.

For the most part, this worked pretty well. Using JSON-formatted [Front Matter](https://caddyserver.com/docs/markdown),
I could specify certain metadata about each post, such as the date of the post, a link to the original post on Blogger,
and so forth. However, Sphinx was unable to add any of the posts to the site index (for search purposes) because all the
posts were being rendered outside the scope of what Sphinx knew about. I attempted some workarounds, but this was a deal
breaker for me in the end.

### Git Integration

Caddy allows you to specify a git repository for it to pull from to build your website. This plugin is pretty
feature-rich and includes support for specifying the following:

- Deployment SSH key for accessing a private git repository
- An interval at which it should automatically pull any new changes
- Commands to be executed after a successful pull
- [More](https://caddyserver.com/docs/http.git)...

One thing I found that helped when using this Caddy plugin was to have two separate versions of my
[Caddyfile](https://caddyserver.com/docs/caddyfile), one for development that is tracked by git along with the other
source files for the website, and another for production that I created as a [gist](https://gist.github.com/) on GitHub.
To illustrate why this was helpful, here is the development configuration:

```
http://mikemabey.com:8080 {
  root _build/html
  log stdout
  errors stderr
}

http://blog.mikemabey.com:8080 {
  redir http://mikemabey.com:8080/blog/
}
```

And this is my production configuration:

```
http://mikemabey.com {
  root /mnt/web_data/caddy_www/_build/html
  git git@bitbucket.org:mmabey/my_website {
    branch master
    path /mnt/web_data/caddy_www
    key /home/ubuntu/.ssh/id_rsa
    hook /webhook
    hook_type bitbucket
    then /mnt/web_data/caddy_www/run_make.sh
  }
  realip {
    from 10.90.0.0/16
  }
}

http://blog.mikemabey.com {
  redir https://mikemabey.com/blog/
}
```

Here are the key differences:

- When developing, I want to use port 8080
- I build the files myself when developing, but production should build itself
- No need to hook into the git repo on my dev machine
- I have different logging and error reporting needs when developing vs when in production

By the way, if you're wondering why my production configuration explicitly uses HTTP when I was touting the automatic
HTTPS feature of Caddy, it's because my website sits behind a [proxy](https://caddyserver.com/docs/proxy) (also running
Caddy) that handles the HTTPS certificates on my behalf.

**Edit** *(7/18/2017)*: If you happen to be running your web server behind a [reverse
proxy](https://caddyserver.com/docs/proxy), you should note that the [git plugin](https://caddyserver.com/docs/http.git)
verifies that each webhook request is actually coming from the expected service (e.g. GitHub, Bitbucket) or it will
return a `403 Forbidden` error. The problem is, as described in [this forum
discussion](https://caddy.community/t/best-practise-for-multiple-tenant-multiple-https-domain-server/2082/6), that the
proxy moves the actual remote IP address to a `X-Forwarded-For` header, resulting in a failed source validation. The
workaround is to add the `realip` directive to the Caddyfile as I have above, with the `from` field set to the internal
IP address of the reverse proxy server. This will restore "the real IP information when running caddy behind a proxy,"
as the [plugin documentation](https://github.com/captncraig/caddy-realip/blob/master/README.md) explains. Just don't
forget to add the `http.realip` plugin when you download Caddy!


## Final Setup

As it turns out, in addition to Sphinx supporting source files in RST, it also supports
[Markdown](http://www.sphinx-doc.org/en/stable/markdown.html), and it's surprisingly simple to set up. The
[recommonmark](http://recommonmark.readthedocs.io/en/latest/index.html) library, which Sphinx uses to render files to
HTML, even allows you to include portions of RST code that _get evaluated_ by Sphinx before it compiles it to HTML (this
is made possible by an add-on [component](http://recommonmark.readthedocs.io/en/latest/auto_structify.html) that you
have to configure before using).

### Tags

That last bit about adding RST snippets is actually super cool. What it really means is that if there is a RST command
that doesn't exist in Markdown, you can use this add-on so that you can still use that syntax in your Markdown file.
When I combined this feature with Sphinx's [file-wide
metadata](http://www.sphinx-doc.org/en/stable/markup/misc.html#file-wide-metadata) markup, all I have to do is add a
little RST section at the top of each Markdown file to be able to specify the metadata for that post, like this:

    ```eval_rst
    :heading: /var/log/mike
    :subheading: Mike's Blog
    :doc_type: blog

    :tags: blog, Blogger, Markdown, Sphinx, git, website, mikemabey.com, Jinja, reStructuredText, Caddy, HTTPS, gist
    :day: 3
    :month: 6
    :year: 2017
    ```

Notice the `:tags:` line. It's a comma-separated list that has to be all on the same line for Sphinx to assign it all to
the `:tags:` meta variable. I'll explain how I use these when I talk about the Blog Index.

### Search

Sphinx has a built-in search feature, which indexes the contents of all the source files during compilation and saves
the information to a static file. What all this means is that you get a searching feature for free without having to
give up running only static files on your site. By adding Markdown to the set of file types that Sphinx compiles to
HTML, I didn't have to do anything else to achieve this objective.

### Analytics

When I set up [mikemabey.com](https://mikemabey.com), I added [Google Analytics](https://analytics.google.com) to get an
idea of what traffic was coming to the site. Analytics generates a Pages Report automatically, giving details about each
page on the site. While it's not the same format as Blogger, it still provides the basic information I was looking for
to achieve this objective, so this wasn't any extra work for me.

### Blog Index

Including an index of all blog entries was the trickiest objective to achieve. Although it's easy to have Sphinx
generate a simple [table of contents](http://www.sphinx-doc.org/en/stable/markup/toctree.html) in such a way as to list
all the blog entries, doing things this way doesn't give you any control over how everything is displayed. The
objectives of my blog index were:

- Group entries by year, with each year being its own unordered list, and with everything in reverse chronological order
- Embed the entry's tags into each list item somehow to be able to selectively show them

The feature of Markdown that made all this possible was that you can include arbitrary HTML (with some limitations) and
it will all render properly. I leveraged this by creating an index in Markdown with all the custom HTML I needed while
not getting in Sphinx's way of generating the HTML that surrounds the article contents. This index file is regenerated
every time I compile to HTML by way of a Python script that the
[Makefile](http://www.sphinx-doc.org/en/stable/invocation.html) runs before telling Sphinx to do its thing.

The individual entries use `<li>` tags that belong to CSS classes that correspond with the tags for that entry. For
example:

```html
<li class="entry hidden_entry Chrome_OS Chromium Chromium_OS Linux_Mint Ubuntu 2015"> Jan 30: <a href="/blog/2015/01/fixing_repo_init_chromium_os.html">Fixing repo init to check out Chromium OS code</a></li>
```

This entry is part of the following classes:

- `entry`: All entries and year headers (which use a `<h2>` tag) use this class so I can easily get a handle on
  everything related to blog entries.
- `hidden_entry`: This is an aesthetic tweak. By trying out a few different techniques, I discovered that it looks
  better in the general case if all entries are hidden when the page first loads and then the selected tags have this
  class removed (making them appear), than to do this in the opposite order.
- `2015`: The year the post was created, allowing me to show entries by year.
- The other classes correspond with the tags for that entry.

I then have a custom set of CSS rules that handle the styling and turning on/off the display for tags, triggered by some
JavaScript. The filtering is set when the URL has the query parameter `?tag=some_tag`, and each blog entry's page has
a section at the bottom with links to the appropriate URLs that include this query.

### Year Indexes

The final piece of the puzzle was including a way to quickly jump to entries from a specific year. I wanted this to
appear in the main table of contents on the left panel, which meant working within the capabilities of Sphinx's [table
of contents](http://www.sphinx-doc.org/en/stable/markup/toctree.html) feature.

First, I modified my Python script that generates the blog index to add the following:

    ```eval_rst
    .. toctree::
       :hidden:
       :maxdepth: 1

       2017 Entries <2017/index>
       2016 Entries <2016/index>
       2015 Entries <2015/index>
       2013 Entries <2013/index>
       2012 Entries <2012/index>
    ```

Of course, this once again leverages [`recommonmark`'s
add-on](http://recommonmark.readthedocs.io/en/latest/auto_structify.html) that evaluates RST code. Here's what each part
means:

- `:hidden:` - The table of contents tree won't appear in the rendered document, but will tell Sphinx about the
  hierarchy of pages.
- `:maxdepth: 1` - Don't recurse into the directories.
- `2017 Entries <2017/index>` - Points to a file named `index.rst` in the year directory and labels it "2017 Entries"

The Python script also creates a file called `index.rst` in each of the year directories with contents similar to the
following:

    ====
    2017
    ====
    |redir|

    .. |redir| raw:: html

       <script language="javascript">window.location.href = "/blog/?tag=2017"</script>

This creates some raw HTML that redirects the browser back go the blog index with a query parameter specifying a
particular year.


## Final Thoughts

I'm really happy with the results of this transition, even though it took a while for me to figure out how to achieve
all of my objectives. If you're looking for a way to add Markdown files to your Sphinx-generated site, hopefully you'll
find some of the things I've discussed to be helpful. And give [Caddy](https://caddyserver.com/) try sometime, it's a
great web server!
