:heading: CSE 469 Computer and Network Forensics
:subheading: Spring 2019

==================================
Homework 5: MAC Conversion Utility
==================================

The purpose of this task is to write code that performs the MAC conversion based on the following usage specification
and input/output scheme. This conversion MUST follow the procedure that we discussed in the lecture. The code you write
for this project should be in a Linux-compatible language (e.g. C/C++, Java, Python, Perl, etc.). Your code should
assume that little endian reordering has already been applied to the input::

   mac_conversion -T|-D [-f filename | -x hex_value ]


Where the parameters must conform to the following specifications:

   -T  Use time conversion module. Either ``-f`` or ``-h`` must be given.
   -D  Use date conversion module. Either ``-f`` or ``-h`` must be given.
   -f filename
         This specifies the path to a filename that includes a hex value
         of time or date. Note that the hex value should follow this
         notation: ``0x1234``. For the multiple hex values in either a file
         or a command line input, we consider only one hex value so the
         recursive mode for MAC conversion is optional.
   -x hex_value
         This specifies the hex value for converting to either date or
         time value. Note that the hex value should follow this notation:
         ``Ox1234``. For the multiple hex values in either a file or a
         command line input, we consider only one hex value so the
         recursive mode for MAC conversion is optional.

The converted time or date value should be based on the following scheme::

   Time: hr:min:sec AM|PM
   Date: Month day, Year


Example
-------

An example of this in use would be the following, where the time conversion is requested with a file::

   $ mac_conversion -T -f test.txt
   Time: 10:31:44 AM

Another example shows the date conversion with the hex value as an input::

   $ mac_conversion -D -h 0x4f42
   Date: Feb 15, 2013


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

You will need to submit your source code, along with a Makefile and README. The Makefile must create your executable,
called ``mac_conversion``, when the command ``make`` is run. Your README file must be plain text and should contain your
name, ASU ID, and a description of how your program works.

A prior TA compiled some resources on how to write a Makefile which might be helpful:

https://www.cs.swarthmore.edu/~newhall/unixhelp/howto_makefiles.html


Submission Site
---------------

Create an account to submit your assignment for all parts on the course submission site:
https://cse469s19.mikemabey.com/
