{
  "template": "blog",
  "heading": "/var/log/mike",
  "subheading": "Mike's Blog",

  "title": "How to check out an old version of Chromium OS",
  "orig_link": "https://mikemabey.blogspot.com/2016/02/how-to-check-out-old-version-of.html",
  "tags": ["Chrome OS", "Chromebook", "Chromium", "Chromium OS", "git"],
  "day": 26,
  "month": 2,
  "year": 2016
}

You gotta love the combination of open source projects and git. Getting up and running with a project like Chromium OS
is pretty straightforward with [the guide available on the Chromium
Wiki](http://www.chromium.org/chromium-os/developer-guide). But what if, for some reason, you're interested in a version
*other* than the most recent? How do you dig through the combinations of repositories to get it? I recently had to
figure this out for a project I'm working on, so I thought I'd pass it along.

First off, you should know that version numbers between Chrome, Chrome OS, Chromium, and Chromium OS do have a [certain
correlation](https://www.chromium.org/developers/version-numbers), but isn't guaranteed to be the same across the
repositories for all of them.

Once you've figured out which version of you want, go to [this
list](https://chromium.googlesource.com/chromiumos/manifest-versions/+/master/paladin/buildspecs/) of build versions,
click on the version number in the list, then select a build number from the next page.

What you see next is a long XML file that tells repo (Google's wrapper around git) what versions of all the Chromium
repositories correspond to that build number. Scroll all the way down to the bottom of the page and click on the "txt"
link to download it. This will be a Base64-encoded version of the XML file you were just looking at.

Next, decode the text file with a command like this:
```
base64 -d [manifest_version].txt > [manifest_version].xml
```

This assumes you're working on a \*nix system. A quick [Google search](http://lmgtfy.com/?q=decode+base64+on+Windows)
will help Windows users. Be sure to replace `[manifest_version]` as appropriate.

Assuming you've checked out the Chromium OS repositories before using the repo command, run the `sync` command using the
manifest you just downloaded with:
```
repo sync -m /path/to/[manifest_version].xml
```

If you haven't checked out the repositories before, follow the instructions on the guide listed above, then replace the
`repo sync` command with the one above. Keep in mind that the sync process takes a VERY long time.

At this point, if you were to try and enter the SDK with the usual `cros_sdk` and do any commands, they would likely
fail because it is too new. Get the appropriate version with:
```
cros_sdk --replace
```
This command will also take a long time to complete.

Now you can enter the SDK with `cros_sdk`. Now you should rebuild all the packages with:
```
build_packages --nowithdebug --board=${BOARD}
```
This command will also take a long time to complete.

Finally, you can build an image with the usual command (adding any extra flags you need):
```
build_image --board=${BOARD}
```

That's it! Good luck working with Chromium OS!
