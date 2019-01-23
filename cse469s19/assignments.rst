:heading: CSE 469 Computer and Network Forensics
:subheading: Spring 2019

===========
Assignments
===========

.. toctree::
   :hidden:

   paper_report
   project


================  ======  ================   ======
Title             Posted  Submissions Open   Due
================  ======  ================   ======
`Paper Report`_   N/A     N/A                Apr 11
`Group Project`_  Jan 17  N/A                Apr 25
================  ======  ================   ======


.. _Paper Report: paper_report.html
.. _Group Project: project.html



General Guidelines for Homework Submissions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following instructions apply to all programming assignments for this course.



Implementation
--------------

Your programs must work on `Ubuntu 18.04 64-bit <http://releases.ubuntu.com/18.04/>`__ with the default packages
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

For each assignment, we will create a test script to help you test your program before compiling.

1. Download the test script, which will be called ``test.sh``, to the directory where your code lives (including
   ``README`` and ``Makefile``).
2. Ensure that ``test.sh`` is executable: ``chmod +x test.sh``
3. Run: ``./test.sh``


Submission Instructions
-----------------------

You will need to submit your source code, along with a Makefile and README. The Makefile must create your executable
when the command ``make`` is run. Your README file must be plain text and should contain your name, ASU ID, and a
description of how your program works.

A prior TA compiled some resources on how to write a Makefile which might be helpful:

https://www.cs.swarthmore.edu/~newhall/unixhelp/howto_makefiles.html


Submission Site
---------------

Create an account to submit your assignment for all parts on the course submission site:
https://cse469s19.mikemabey.com/
