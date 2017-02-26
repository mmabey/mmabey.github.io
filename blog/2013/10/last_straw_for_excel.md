{
  "template": "blog",
  "heading": "/var/log/mike",
  "subheading": "Mike's Blog",

  "title": "The Last Straw for Excel?",
  "orig_link": "https://mikemabey.blogspot.com/2013/10/the-last-straw-for-excel.html",
  "day": 19,
  "month": 10,
  "month_name": "October",
  "year": 2013
}

Microsoft Office and I haven't been getting along well lately, which is too bad because I have really liked all the new
features of Office 2013. But after upgrading Windows to 8.1 this week, Excel decided to stop working. As in, it
completely crashes whenever I try to go beyond the view of cells available when it opens. Not cool.

Normally I'd try to figure something out to get everything working, but this weekend I had to input my students' grades
so I could discuss their test scores with them on Monday, so I didn't have time to go on a wild Windoze chase for a
solution. Instead, I tried out the import feature of Google Docs, and overall I was pretty impressed. Let me share the
details...

But first, let me back up. I did try two things to get Excel to work: 1) I ran the installer again hoping it would
repair whatever was broken, and 2) I completely uninstalled, restarted, and re-installed Office. Both solutions still
left me with a broken version of Excel. I'm still hoping that it's just a compatibility issue with the brand-new update
of Windows, but for now, I've at least got options.

I have actually wanted to try out Google Drive's import feature on a complex spreadsheet for a while, but never got
around to it. The biggest benefit from this will be that I can access the grade book for my class anywhere on the web
when I need to. There have been a couple times when this would have been handy, and although Dropbox does give me
roundabout access, it doesn't work too great on my Chromebook.

After importing it, there was only one issue with my entire grade book, which is that Google Spreadsheets don't support
the `AVERAGEIF` function from Excel. Luckily, I found [this
forum](http://productforums.google.com/forum/#!topic/docs/L_CKN1AWM34) post that provided me with a pretty simple
workaround.

The key is if you have a function in Excel like this:

> =AVERAGEIF(A5:A10, ">1", B5:B10) *(Range, Criteria, [Sum Range])*

the equivalent Google Spreadsheet version uses the `FILTER` function inside the `AVERAGE` function like this:

> =AVERAGE(FILTER(B5:B10; A5:A10 > 1)) *(Sum Range, Array Condition 1, ...)*

In my case, the sum and criteria ranges were the same, so it made it even easier because there wasn't a chance of mixing
things up.

I was also impressed that the graphs in my spreadsheet stayed nearly exactly as they were in Excel. I had never used the
graph feature before in Google Spreadsheets, and found it to be better developed and more robust than I thought it would
have been.

The bottom line is, if you've been holding out on using Google Spreadsheets to replace some of your Excel data, it may
be less painful than you might think. It sure was for me.
