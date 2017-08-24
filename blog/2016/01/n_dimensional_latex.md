```eval_rst
:heading: /var/log/mike
:subheading: Mike's Blog
:doc_type: blog

:orig_link: https://mikemabey.blogspot.com/2016/01/getting-n-dimensional-to-look-right-in.html
:tags: dashes, LaTeX, n-dimensional, writing
:day: 18
:month: 1
:year: 2016
:title: Getting "n-dimensional" to look right in LaTeX
:datePublished: 2016-01-18T00:00:00
:dateModified: 2016-01-18T00:00:00
```
# Getting "n-dimensional" to look right in LaTeX

LaTeX has some interesting rules for [dashes](https://en.wikibooks.org/wiki/LaTeX/Text_Formatting#Dashes_and_hyphens)
and [hyphenation](https://en.wikibooks.org/wiki/LaTeX/Text_Formatting#Hyphenation) that are hard to get right in certain
scenarios. For example, if you use the term "n-dimensional" and it happens to fall near the end of a line, you'll end up
with something like this:

> text text text text text n-<br />
  dimensional

To get this right, try inserting this snippet in your document's preamble:

```
\usepackage{amsmath}
\renewcommand{\ndimensional}[1]{#1\nobreakdash\discretionary{-}{-}{-}\hspace{0pt}dimensional}
```

Then, replace "n-dimensional" in the document with the following:
```
\ndimensional{n}
```
or, to get the math environment look to the "n", do this:
```
\ndimensional{$n$}
```

## What's going on in the snippet?

The #1 refers to whatever you added as a parameter to the command, which in the example above is "n".

The `\nobreakdash` needs to be combined with a dash character. That means that in other situations you may just need to do this:
```
\renewcommand{\ndimensional}[1]{#1\nobreakdash-\hspace{0pt}dimensional}
```
While the output will be fine for many use cases, the previous snippet with the \discretionary command is a more
general-case solution. (See [this forum post](http://latex-community.org/forum/viewtopic.php?f=44&t=5673) for more info.)

The `\hspace{0pt}` tells LaTeX not to allow any space (including a newline) between the previous character and the one
that follows, acting like glue between the dash added with the `\discretionary` command and the "d" of dimensional.
Without it, you'll get output like this:

> text text text text text n-<br />
  -dimensional

**Edit**: Turns out you need the amsmath package for LaTeX to know what the `\nobreakdash` command is. I've added the
necessary command.
