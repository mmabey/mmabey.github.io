:heading: CSE 469 Computer and Network Forensics
:subheading: Spring 2019

======================================
Homework 4: Address Conversion Utility
======================================

Multiple addressing techniques are used on IBM PC-compatible hard drives and in FAT file systems to both simplify
addressing mechanisms and to reduce the number of bits necessary to locate all areas within a logical space, like a
partition.

For this assignment, you are to write a Unix-like command line utility that will convert between three different address
types when an address of a different type is given. This will require you to have a sound understanding of the following
principles:

1. Hard drive geometry and layout.
2. Sectors.
3. Partition creation.
4. FAT tables and clusters.
5. Addition, subtraction, multiplication, and division.

The code you write for this project should be in a Linux-compatible language (e.g. C/C++, Java, Python, Perl, etc.). Use
the following usage specifications for your utility:

::

    addrconv logical [-b offset] [-B [-s bytes]] [-p address] [-c address -k sectors -r sectors -t tables -f sectors]
    addrconv physical [-b offset] [-B [-s bytes]] [-l address] [-c address -k sectors -r sectors -t tables -f sectors]
    addrconv cluster [-b offset] [-B [-s bytes]] [-l address] [-p address]


Where the parameters must conform to the following specifications:

|blockquote_options|

======== =====
logical  Calculate the logical address from either the cluster address or
         the physical address. Either ``-c`` or ``-p`` must be given.
physical Calculate the physical address from either the cluster address
         or the logical address. Either ``-c`` or ``-l`` must be given.
cluster  Calculate the cluster address from either the logical address or
         the physical address. Either ``-l`` or ``-p`` must be given.
======== =====

|eblockquote|

   -b offset, --partition-start=offset
         This specifies the physical address (sector number) of the start
         of the partition, and defaults to 0 for ease in working with
         images of a single partition. The ``offset`` value will always
         translate into logical address 0.
   -B, --byte-address
         Instead of returning sector values for the conversion, this
         returns the byte address of the calculated value, which is the
         number of sectors multiplied by the number of ``bytes`` per sector.
   -s bytes, --sector-size=bytes
         When the ``-B`` option is used, this allows for a specification of
         ``bytes`` per sector other than the default 512. Has no affect on
         output without ``-B``.
   -l address, --logical-known=address
         This specifies the known logical ``address`` for calculating either
         a cluster address or a physical address. When used with the ``-L``
         option, this simply returns the value given for ``address``.
   -p address, --physical-known=address
         This specifies the known physical ``address`` for calculating either
         a cluster address or a logical address. When used with the ``-P``
         option, this simply returns the value given for ``address``.
   -c address, --cluster-known=address
         This specifies the known cluster ``address`` for calculating either
         a logical address or a physical address. When used with the ``-C``
         option, this simply returns the value given for ``address``. Note
         that options ``-k``, ``-r``, ``-t``, and ``-f`` must be provided with this
         option.
   -k sectors, --cluster-size=sectors
         This specifies the number of sectors per cluster.
   -r sectors, --reserved=sectors
         This specifies the number of reserved sectors in the partition.
   -t tables, --fat-tables=tables
         This specifies the number of FAT tables, which is usually 2.
   -f sectors, --fat-length=sectors
         This specifies the length of each FAT table in sectors.


One of the objectives of this assignment is to help you familiarize yourself with how to read and understand command
line specifications, such as the above. Take your time to understand each option, what it does, and the other options it
interacts with, and you'll do fine.


Example
-------

An example of this in use would be the following, where the desired number is the logical address of physical sector
12345678 in a partition that begins at physical sector 128::

   $ addrconv -L -b 128 --physical-known=12345678
   12345550

Another example shows the utility getting the physical address of cluster 58, in a partition that begins at physical
sector 128, has 2 FAT tables that are each 16 sectors long, 6 reserved sectors, and 4 sectors per cluster::

   $ addrconv -P --partition-start=128 -c 58 -k 4 -r 6 -t 2 -f 16
   390


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
called ``addrconv``, when the command ``make`` is run. Your README file must be plain text and should contain your name,
ASU ID, and a description of how your program works.

A prior TA compiled some resources on how to write a Makefile which might be helpful:

https://www.cs.swarthmore.edu/~newhall/unixhelp/howto_makefiles.html


Submission Site
---------------

Create an account to submit your assignment for all parts on the course submission site:
https://cse469s19.mikemabey.com/


.. |blockquote_options| raw:: html

   <blockquote class="options_table">

.. |eblockquote| raw:: html

   </blockquote>
