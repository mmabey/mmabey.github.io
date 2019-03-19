:heading: CSE 469 Computer and Network Forensics
:subheading: Spring 2019

==========================
Homework 3: Email Analysis
==========================

:Due Date: April 11
:Done By: Individuals
:Submission: On `Gradescope <https://www.gradescope.com/courses/32610/assignments/178568>`_

Email continues to be an essential component of conducting business. This assignment will introduce you to email
forensics by having you write a tool that can search for terms in the Enron email data set and, for any search results,
return the sender's email address and the date and time the message was sent.


Pre-Assignment
--------------

Do the following before you get started programming:

1. Download the Enron email data set from https://www.cs.cmu.edu/~enron/. Be sure to get the May 7, 2015 version (the
   file will be named ``enron_mail_20150507.tar.gz``).
2. Go to https://github.com/lintool/Enron2mbox and follow the instructions to convert the data to the mbox format.
3. For whatever language you plan to use for this assignment, find an mbox library.

If you plan to use Python, check out the following links:

- https://docs.python.org/3/library/mailbox.html#mbox

  - Take note that the ``mbox`` class is, because it is a subclass of the ``Mailbox`` class, an *iterator*, meaning you
    can use it in a ``for`` loop like this: ``for message in my_mbox_class_instance:``

- https://docs.python.org/3/library/mailbox.html#mailbox.mboxMessage

  - ``mailbox.mboxMessage`` is a subclass of ``mailbox.Message`` which is a subclass of ``email.message.Message``. You
    will need to understand the ``email.message.Message`` class's API for accessing the email's payload. Take note that
    ``email.message.Message`` is **not** a subclass of ``email.message.EmailMessage``.


The Program
-----------

Write a program that satisfies the description above and conforms to the following usage specifications::

   enron_search term [term ...]

|blockquote_options|

====  =========
term  A word to search for in the data set. The search will be case-insensitive,
      but exact, meaning neither fuzzy matching nor partial matching is
      performed. When more than one term is given, only emails with ALL terms
      in the body will be returned.
====  =========

|eblockquote|

Your program should ignore duplicate terms and term order, so that the following are equivalent::

   enron_search the The THE money
   enron_search MONEY tHe monEY
   enron_search the money

The exclusion of fuzzy matching means that the term ``cash`` will not match the string ``money``, although they are
semantically similar. Exact matching (no partial matching) means ``the`` will not match the string ``them``.

Your program should number the results and display the total number of results found when the search completes.

It is totally fine for your program to output the date and time in the same format as it is stored in the email headers.


Example
-------

The following examples are notional (i.e., made up) and are *not* from the Enron data set. Lines starting with ``$`` are
what the user enters into the command line. The other lines are the program's output.

::

   $ enron_search affair
   1. Creepy Dude <creeper@enron.com> Mon, 18 Mar 1995 15:45:04 -0500
   2. Creepy Dude <creeper@enron.com> Sun, 17 Mar 1995 14:47:38 -0500
   Results found: 2

::

   $ enron_search hide all the evidence
   1. Guy Incharge <incharge@enron.com> Mon, 18 Mar 1995 14:47:38 -0500
   2. Peon Smith <psmith@enron.com> Tue, 19 Mar 1995 14:47:38 -0500
   3. Guy Incharge <incharge@enron.com> Wed, 20 Mar 1995 14:47:38 -0500
   4. Peon Smith <psmith@enron.com> Thu, 21 Mar 1995 14:47:38 -0500
   Results found: 4


Implementation
--------------

Your program must work on `Ubuntu 18.04 64-bit <http://releases.ubuntu.com/18.04/>`__ with the default packages
installed. You may find it helpful to set up a virtual machine to do your development. `VirtualBox
<https://www.virtualbox.org/>`_ is a free and open-source VM system.

If you wish to use packages that are not installed on Ubuntu 18.04 64-bit by default, please submit a file with your
code named ``packages``, with a list of packages that you would like installed before calling ``make``. Each line of
``packages`` must be a `valid package name <https://packages.ubuntu.com/bionic/>`__, one package per line. The submission
system will automatically install all the dependencies that the package lists.

For example, if you were going to write your assignment in `Haskell <https://www.haskell.org/>`_, you could install the
`GHC compiler <https://www.haskell.org/ghc/>`_ with the following ``packages`` file:

::

   ghc
   ghc-dynamic

We've created a `test script <hwx/test.sh>`_ called ``test.sh`` to help you test your program before compiling.

1. Download `test.sh <test script_>`_ to the directory where your code lives (including ``README`` and ``Makefile``).
2. Ensure that ``test.sh`` is executable: ``chmod +x test.sh``
3. Run: ``./test.sh``


Submission Instructions
-----------------------

You will need to submit your source code, along with a Makefile and README, on `Gradescope`_. The Makefile must create
your executable, called ``enron_search``, when the command ``make`` is run. Your README file must be plain text and
should contain your name, ASU ID, and a description of how your program works.

A prior TA compiled some resources on how to write a Makefile which might be helpful:

https://www.cs.swarthmore.edu/~newhall/unixhelp/howto_makefiles.html


.. |blockquote_options| raw:: html

   <blockquote class="options_table">

.. |eblockquote| raw:: html

   </blockquote>
