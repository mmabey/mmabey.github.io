:heading: CSE 469 Computer and Network Forensics
:subheading: Spring 2019

===================================
Homework 1: MBR and Volume Analysis
===================================

:Due Date: February 15
:Done By: Individuals
:Submission: On `Gradescope <https://www.gradescope.com/courses/32610/assignments/151473>`__

For this project, you will write a program that analyzes the Master Boot Record (MBR) of a forensic image. A sample raw
image for you to use while programming is available `here <hw1/sample.raw.zip>`__ (you'll need to unzip it to get the
raw image). The SHA-256 checksum of the correct image is:
e60fcb65165416c5ab5b1cb1b66f7b84395220025c73334e0655d91c12b926d7

Your program, which must be an executable called ``mbr_info``, must take as input the path to a raw image, like so::

   $ ./mbr_info sample.raw

.. and open it as read-only before performing any other operations.

Before opening the raw image to perform any analyses, your program should first calculate MD5 *and* SHA1 checksums for
the image. The checksums should be stored as `MD5-[imagename].txt` and `SHA1-[imagename].txt` and should contain *only*
the checksum value, not any other text. For example, the name of raw image is `Sparky.raw` then your authentication
module needs to generate `MD5-Sparky.txt` and `SHA1-Sparky.txt` before opening the raw image.

Next, ensure that you open the image as read-only and locate and extract the partition tables from the MBR. Your program
MUST generate the partition type including hex value and corresponding type, start sector address (LBA), and size of
each partition in decimal as follows::

   (07) NTFS, 0002056320, 0000208845

.. note:: For the partition types, please take advantage of the list available on `Wikipedia
   <https://en.wikipedia.org/wiki/Partition_type>`__.

   This is the one instance where I will allow students to share information for homework solutions: If a more digitally
   ingestible version (e.g., JSON) of the partition types were to be distributed among the class, I would accept its use
   as not violating the academic integrity policy. However, the usual rules apply for citation, etc. As usual, please
   feel free to ask clarifying questions on Piazza.

.. note:: You should print integers showing 10 digits padded with zeros, as in the example above. Delimiters between
   values should also be as shown in the example.

For each partition your program discovers listed in the MBR, locate and read in the boot record of the partition (first
sector) and output the hexadecimal values of the final 8 bytes of the boot record, as follows::

   Partition number: 1
   Last 8 bytes of boot record: 67 66 72 65 65 6D 61 6E

.. note:: The above is only illustrative. The given hex values are not valid in a regular boot record.

So, invoking your program will output data in the following format::
   (07) NTFS, 0002056320, 0000208845
   (07) NTFS, 0002265165, 0000208845
   (07) NTFS, 0002474010, 0000208845
   (07) NTFS, 0002682855, 0000208845
   Partition number: 1
   Last 8 bytes of boot record: 67 66 72 65 65 6D 61 6E
   Partition number: 2
   Last 8 bytes of boot record: 67 66 72 65 65 6D 61 6E
   Partition number: 3
   Last 8 bytes of boot record: 67 66 72 65 65 6D 61 6E
   Partition number: 4
   Last 8 bytes of boot record: 67 66 72 65 65 6D 61 6E



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

We've created a `test script <hw1/test.sh>`_ called ``test.sh`` to help you test your program before compiling.

1. Download `test.sh <test script_>`_ to the directory where your code lives (including ``README`` and ``Makefile``).
2. Ensure that ``test.sh`` is executable: ``chmod +x test.sh``
3. Run: ``./test.sh``


Submission Instructions
-----------------------

You will need to submit your source code, along with a Makefile and README. The Makefile must create your executable,
called ``mbr_info``, when the command ``make`` is run. Your README file must be plain text and should contain your name,
ASU ID, and a description of how your program works.

A prior TA compiled some resources on how to write a Makefile which might be helpful:

https://www.cs.swarthmore.edu/~newhall/unixhelp/howto_makefiles.html


Submission Site
---------------

Log into `Gradescope <https://www.gradescope.com/courses/32610>`__ and look for Homework 1.
