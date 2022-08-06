```{eval-rst}
:heading: /var/log/mike
:subheading: Mike's Blog
:doc_type: blog

:orig_link: https://mikemabey.blogspot.com/2016/03/using-git-stash-without-losing-staged.html
:tags: git, git index, git-stash
:day: 7
:month: 3
:year: 2016
:title: Using git-stash without losing staged changes
:datePublished: 2016-03-07T00:00:00
:dateModified: 2016-03-07T00:00:00
```
# Using git-stash without losing staged changes

When I learned about [`git-stash`](https://git-scm.com/docs/git-stash), my productivity with git from the command line
went way up. But it wasn't until recently that I figured out how to properly handle the situation where I had already
staged changes but needed to stash everything to do something without .

The problem comes from the fact that `stash` lumps all the changes to the tracked files together, without separating all
the things you've added to the [index](http://www.gitguys.com/topics/whats-the-deal-with-the-git-index/). If you've done
a patch add with `git add -p`, this can mean a lot of frustration at having to pick through all the changes again once
you do `git stash pop`.

To avoid this frustration, do the following and you'll be able to keep your staged changes over the course of using
`stash`.

1. First, do a stash of only the things you haven't yet staged:

        git stash save --keep-index "Un-staged changes"

    At this point, if you run `git status`, you should see all your changes that have been staged still there, but none of
    the changes NOT staged for commit (except of course for any untracked files).

2. Next, stash the staged changes as you normally would:

        git stash save "Staged"

3. Now is when you want to do any work you need to while the other changes are stashed. NOTE: If you need to make
   changes that are based on a file in the "Un-staged changes" stash, you will of course need to pop that stash
   specifically with `git stash pop stash@{1}`. But, in order to get the staged changes back, you'll need to do another
   `git stash save` to do things in the correct order.

4. To get your changes back, you're going to pop them off the stash in the reverse order. If you haven't stashed any
   other changes, you can do a simple pop:

        git stash pop

    Otherwise, you should run:

        git stash list

    and find the correct name of the stash to pop, e.g. `stash@{1}`.

5. All the changes you just popped aren't staged at this point but should be, so go ahead and add all of them to the
   index with `git add file1 file2 ...`

6. Finally, run `git stash pop` one more time to recover the un-staged changes you saved in step 1 and you'll have
   everything back to the way it was at the beginning.
