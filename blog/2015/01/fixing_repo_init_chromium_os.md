```eval_rst
:heading: /var/log/mike
:subheading: Mike's Blog
:doc_type: blog

:orig_link: https://mikemabey.blogspot.com/2015/01/fixing-repo-init-to-check-out-chromium.html
:tags: Chrome OS, Chromium, Chromium OS, Linux Mint, Ubuntu
:day: 30
:month: 1
:year: 2015
```
# Fixing repo init to check out Chromium OS code

Building Chromium OS is a little tricky. Although the
[instructions](http://www.chromium.org/chromium-os/developer-guide) from the project page are pretty detailed, one bump
I ran into was this error when I put in the `repo init ...` command:

```
fatal: Cannot get https://chromium.googlesource.com/a/external/repo.git/clone.bundle
fatal: HTTP error 401
```

Turns out that there's an [issue](https://code.google.com/p/chromium/issues/detail?id=393715) with the `repo init` code
that makes it fail if there's anything wrong with your `~/.netrc` file. My system didn't even have a `.netrc` file,
which made it hard to know how to fix that problem.

As Mike Frysinger explained on the [Chromium OS
dev](https://groups.google.com/a/chromium.org/forum/#!msg/chromium-os-dev/uQIZ-ltbwLM/eUEZHhhhc4AJ) mailing list, it's
possible to make your own valid `.netrc` file by using the cookie values created when you set up your gerrit
credentials. The first thing I did was make a copy of the cookies file:

```
cp ~/.gitcookies ~/.netrc
```

From here, I went ahead and removed the second line (the cookie for chromium-review.googlesource.com) and reformatted
the information from:

```
chromium.googlesource.com FALSE / TRUE 2147483647 o git-<email address>=1/X_<cookie data>
```

to look like this:

```
machine chromium.googlesource.com login git-<email address> password 1/X_<cookie data>
```

When you run the full `repo init ...` command again, it will add a second entry in your `.netrc` file for
chromium-review.googlesource.com with the same cookie value and you'll be ready to run `repo sync`.

Be aware that (as of today, January 30, 2014) downloading the whole repository will take about 11GB of disk space. And
I'm working in Linux Mint 17, which is based on Ubuntu 14.04.

In any case, I hope this helps someone fix this issue faster than I did. The pieces of the puzzle were a little
scattered.
