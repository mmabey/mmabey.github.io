{
  "template": "blog",
  "heading": "/var/log/mike",
  "subheading": "Mike's Blog",

  "title": "Debian on Android and my quest for a full-fledged terminal Python IDE",
  "orig_link": "https://mikemabey.blogspot.com/2012/06/debian-on-android-and-my-quest-for-full.html",
  "tags": ["Android", "Debian", "Linux", "Linux on Android", "Python", "Python on Android", "root", "Root Keeper",
           "rooting 9.4.2.21", "rooting 9.4.2.28", "rooting TF201", "Terminal Emulator", "Transformer Prime", "vim",
           "vim add-ons"],
  "day": 23,
  "month": 6,
  "year": 2012
}

So when I recently discovered that my Asus Transformer Prime [has Python on it](/blog/2012/06/pydroid_at_last.md), but
that it only has version 2.6.2 and is missing some needed libraries, I could tell that setting up a sweet Python
programming environment was going to be possible, but a little longer road than I thought it was going to be. Here's how
I successfully overcame multiple obstacles to get things working.

A few things indicated to me that what I wanted to accomplish would still be possible:

* I found [this blog post](http://blog.dispatched.ch/2009/05/24/vim-as-python-ide/) that talks about all sorts of
  add-ons to Vim that make it a really powerful IDE in a terminal environment. I like the idea of doing things this way
  so I'm dependent on what is available in the Android app store or what I could figure out how to create myself. Plus
  I would never have time to write my own Android app that filled that purpose to my satisfaction.
  <br /><br />
  The first major hurdle with this idea is that Vim has to be compiled with Python support. I knew (and later verified)
  that the [Vim app](https://play.google.com/store/apps/details?id=net.momodalo.app.vimtouch&) wasn't going to provide
  that, and I also knew that trying to cross-compile Vim on another machine and figure out how to get it on my tablet
  and working as expected wasn't going to be fun at all.
  <br /><br />
  The second major hurdle with this was figuring out how to get the add-ons installed such that Vim knew about them.
  With the differences in structure of the Android OS, I simply did not want to try to figure out what was going to
  work.

* The answer to many of the above listed problems seemed to be in an app I found called [Linux
  Installer](https://play.google.com/store/apps/details?id=com.galoula.LinuxInstall). The idea is that with root access
  on an Android device, you can create a loop device where you can install a full-fledged distribution of Linux , then
  mount the loop device and then utilize `chroot` to use that file system when working in something like [Terminal
  Emulator](https://play.google.com/store/apps/details?id=jackpal.androidterm). With this, I can install specific
  packages from a mainstream distribution that already satisfy the requirements of my project.

The first obstacle I faced was rooting my tablet. As of this writing, there isn't a direct method of rooting the current
version of the Prime's firmware, 9.4.2.28, or the previous version, 9.4.2.21. Searching around on XDA Developers turned
up some [instructions on downgrading the firmware of the
Prime](http://forum.xda-developers.com/showthread.php?t=1622628) to a "root-vulnerable" version. Then I [rooted
it](http://forum.xda-developers.com/showthread.php?t=1441138), installed [Root
Keeper](https://play.google.com/store/apps/details?id=org.projectvoodoo.otarootkeeper) (which protects your root
privileges between system upgrades), and did a system update to get the latest firmware again.

At this point I was ready to install Debian using Linux Installer. I had read some of the reviews of Linux Installer so
I would know a little better what to expect when running it, and some people reported having problems with the program
stalling and not successfully completing the installation. Looking through the sparse
[documentation](http://android.galoula.com/en/LinuxInstall/), however, shows the following instruction just before the
"Quick Tutorial" section:

> If some step fails, retry it twice. If a step fails three consecutive times, quit the application by pressing the back
  button several times, and restart it.

While this isn't the most eloquent of instructions, I took it to heart and got started. Sure enough, the installer had
problems getting through various steps of the process, stalling for literally days but still having the appearance of
making progress. I could never tell how long each step should take under ideal conditions or if allowing it to run and
run was actually doing any good.

I found the solution to be some mixture of the following steps, all the while taking measures to keep the tablet powered
and connected to the Internet:

* Let the installer go for a while and give it some time to try and resolve the step it's working on.
* After a while, stop the application from either the menu, "pressing the back button several times," or pressing the
  Home button and terminating the application using some other method.
* Restart the application. If it is unable to start running normally again, try exiting the program again and starting
  it up. If this still doesn't do the trick, reboot the tablet. There were several times that I had to do this more than
  once to get Linux Installer working normally again.
* Once it's running normally, remount the loop device and start the installation over. Chances are about 50% that it will
  get further than the previous installation attempt.

To give you an idea of where you are in the overall installation process, you can take a look at the console log. In it
at the top you should see several lines in blue text. These are the messages that appear on the main window of the
application in the top left corner that indicate what the installer is currently working on. One thing to take note of
is that they are logged in reverse chronological order, which is contrary to typical log files. The installer will go
through the following steps (assuming you did the default Debian installation like I did) *in this order* meaning the
log will show the following in reverse order:

1. Retrieving Release
2. Validating Packages
3. Resolving dependencies of required packages...
4. Resolving dependencies of base packages...
5. Found additional required dependencies: insserv libbz2-1.0 libdb4.8 libslang2
6. Found additional base dependencies: libnfnetlink0 libsqlite3-0
7. Checking component main on http://130.89.148.12/debian...

After it has completed step 7 above, it will alternate between retrieving and validating individual packages, like
libacl1, which happened to be the first package it worked on after step 7 for me. At this point it will choose an
extractor for all the .deb packages, then it will *extract* all the packages, *unpack* them, and then *configure* them.
It may also alternate between unpacking and configuring more packages that are not considered part of the base system,
but then you should be done!

I still haven't undertaken including all the add-ons to Vim so that it acts as the IDE I'm hoping to have for Python
development, nor have I figured out how to access `/sdcard` from Debian. I'm sure I'll be posting something in the near
future with any details of what I had to do to get things working. Until then, I hope the above helps someone to not get
discouraged with Linux Installer, because it really is cool once you have everything working. Happy hacking!
