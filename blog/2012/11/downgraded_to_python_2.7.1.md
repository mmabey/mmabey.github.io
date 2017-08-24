```eval_rst
:heading: /var/log/mike
:subheading: Mike's Blog
:doc_type: blog

:orig_link: https://mikemabey.blogspot.com/2012/11/downgraded-to-python-271-how-did-that.html
:tags: Box, Box sync, executable file's path, PEP 8, Py2Exe, Python, StackOverflow, Windows
:day: 7
:month: 11
:year: 2012
:title: Downgraded to Python 2.7.1? How did that happen?
:datePublished: 2012-11-07T00:00:00
:dateModified: 2012-11-07T00:00:00
```
# Downgraded to Python 2.7.1? How did that happen?

So I was doing some work on my home computer tonight which involved a little bit of Python hacking in Windows. At one
point I wanted to make sure that I had a certain library installed such that it was accessible to the script I was
working with, so naturally I opened up an interpreter and tried importing it. It failed, which surprised me since I had
just finished using pip to install it and no errors occurred.

The script I was working with was one I wrote a few years ago, so my first thought was that maybe they released a newer
version of the library with different capitalization. Kind of a strange guess, I know, but not too far-fetched
considering PEP 8 is still not completely followed by the community and some maintainers of certain libraries are
changing this to conform to the standard, but I digress. I run the pip install command one more time, just to make sure
that there wasn't an issue with naming. Nope, dependency already resolved.

Finally, I noticed that the interpreter I was running was Python 2.7.1. Well, I knew that couldn't be the problem, but I
like to always have the latest version of Python installed so I thought I'd take a minute to rectify that. But that was
another issue... why wasn't I running 2.7.3? It was weird that I had such an old version running when I'm usually so on
top of updating Python. Whatever.

So I first tried a repair. Still showed up as 2.7.1. Downloaded a fresh copy of the installer and verify the checksum.
Still showed up as 2.7.1. Removed it completely after making a backup of site-packages, then re-installed it. Still
showed up as 2.7.1. Uninstalled it again without re-installing it. The interpreter still ran and showed up as 2.7.1.
What the...?

I was starting to get fed up at this point. The system path didn't have anything out of the ordinary, like a separate
folder for an old installation, nothing. Finally, I found this
[StackOverflow](http://stackoverflow.com/questions/519410/find-the-path-of-notepad-exe-and-mspaint-exe) article which,
oddly enough, had an example of exactly what I needed to figure out what was going on and where this rouge installation
of Python was that was driving me crazy. Here's what I got:

```
C:\Users\Mike>for %i in (python.exe) do @echo %~$PATH:i
C:\Program Files\Box Sync\Python.exe
```

**Box Sync includes its own Python interpreter?** That's what's going on? And it somehow became the default interpreter
instead of my 2.7.3 installation? Okay... I guess that's great they're using Python, but why force my computer to use an
old interpreter? I'm no Windows expert, but it seems like there should be a better way to do whatever it is they're
trying to do. But I can also have sympathy for them not wanting to use Py2Exe... **shudder**

Apparently, this is something [Box is already aware
of](https://support.box.com/entries/21910576-why-is-box-sync-shipping-a-vulnerable-version-of-python-dll), but the whole
thing is still just so weird. I don't use Box that much as it is, so I think I'll just nuke their version of Python for
the time being. And yes, it did fix my problem.
