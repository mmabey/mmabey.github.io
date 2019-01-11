:heading: CSE 469 Computer and Network Forensics
:subheading: Spring 2019

==========================================
Group Project: Blockchain Chain of Custody
==========================================

:Due Date: April 25
:Done By: Groups
:Checkpoint: March 28

The Chain of Custody form is a critical element to a forensic investigation because examiners use it to record the
history of the evidence from the time it is found until the case is closed or goes to court. By keeping this record,
examiners can show that the integrity of the evidence has been preserved and not open to compromise. And in the
unfortunate event that evidence *does* become contaminated, the chain of custody will clearly identify the responsible
individual.

A Chain of Custody form keeps track of three pieces of important information (in addition to all the details that
uniquely identify the specific piece of evidence):

1. **Where** the evidence was stored.
2. **Who** had access to the evidence and **when**.
3. **What** actions were done to the evidence.

As an example, please refer to this generic chain of custody for from NIST:

- URL for while the government is shut down: https://webcache.googleusercontent.com/search?q=cache:EDTx4jL_PqQJ:https://www.nist.gov/document/sample-chain-custody-formdocx+&cd=1&hl=en&ct=clnk&gl=us
- Regular URL: https://www.nist.gov/document/sample-chain-custody-formdocx+&cd=1&hl=en&ct=clnk&gl=us

For this project, your group will write a program that will be a digital equivalent to a chain of custody form. Each
entry in the form will be stored in a `blockchain <https://en.wikipedia.org/wiki/Blockchain>`__ of your own creation.

Blockchain technology has been touted as a solution that will improve every aspect of digital communication. However,
real-world results have been `practically non-existent
<https://www.computerworld.com/article/3324359/blockchain/blockchain-what-s-it-good-for-absolutely-nothing-report-finds.html>`__. Consider the following flow chart that explores some use cases where a blockchain may be a good idea:

.. image:: do_you_need_a_blockchain.jpg
   :scale: 50%
   :align: center

Considering that blockchains aren't suitable for very many use cases, this will largely be an academic exercise, but one
that I hope will be illustrative of how important it is to use the right tool for the job.


Requirements
------------

Your blockchain chain of custody program must implement the following commands::

   bchoc add -c case_id -i item_id [-i item_id ...]
   bchoc checkout -i item_id
   bchoc checkin -i item_id
   bchoc log [-r] [-n num_entries] [-c case_id] [-i item_id]
   bchoc remove -i item_id -y reason [-o owner]
   bchoc init
   bchoc verify

Where the parameters must conform to the following specifications:

|blockquote_options|

========  =================================================================
add       Add a new evidence item to the blockchain and associate it with
          the given case identifier. For users' convenience, more than one
          item_id may be given at a time, which will create a blockchain
          entry for each item without the need to enter the case_id multiple
          times. The state of a newly added item is ``CHECKEDIN``.
checkout  Add a new checkout entry to the chain of custody for the given
          evidence item. Checkout actions may only be performed on evidence
          items that have already been added to the blockchain.
checkin   Add a new checkin entry to the chain of custody for the given
          evidence item. Checkin actions may only be performed on evidence
          items that have already been added to the blockchain.
log       Display the blockchain entries giving the oldest first (unless ``-r``
          is given).
remove    Prevents any further action from being taken on the evidence item
          specified. The specified item must have a state of ``CHECKEDIN`` for
          the action to succeed.
init      Sanity check. Only starts up and checks for the initial block.
verify    Parse the blockchain and validate all entries.
========  =================================================================

|eblockquote|

   -c case_id
         Specifies the case identifier that the evidence is associated with.
         Must be a valid UUID. When used with ``log`` only blocks with the
         given ``case_id`` are returned.
   -i item_id
         Specifies the evidence item's identifier. When used with ``log`` only
         blocks with the given ``item_id`` are returned.
   -r, --reverse
         Reverses the order of the block entries to show the most recent entries
         first.
   -n num_entries
         When used with ``log``, shows ``num_entries`` number of block entries.
   -y reason, --why reason
         Reason for the removal of the evidence item. Must be one of:
         ``DISPOSED``, ``DESTROYED``, or ``RELEASED``. If the reason given is
         ``RELEASED``, ``-o`` must also be given.
   -o owner
         Information about the lawful owner to whom the evidence was released.


Every block in the blockchain will have the same structure:

============= ====
Length (bits) Field Name - Description
------------- ----
128           Index - Must be a valid UUID
160           Previous Hash - SHA-1 hash of this block's parent
64            Timestamp - Regular Unix timestamp
?             Case ID
?             Evidence Item ID
?             State - Must be one of: ``CHECKEDIN``, ``CHECKEDOUT``, ``DISPOSED``, ``DESTROYED``, or ``RELEASED``.
?             Data Length
?             Data
============= ====


When the program starts it should check if there are any existing blocks and create a block with the following
information if it doesn't find any:

- ``Index``: 0
- ``Previous Hash``: None, null, etc.
- ``Timestamp``: Current time
- ``Case ID``: None, null, etc.
- ``Evidence Item ID``: None, null, etc.
- ``State``: "INITIAL"
- ``Data Length``: 14 bytes
- ``Data``: The string: "Initial block"


All block data must be stored in a binary format. Plain text, JSON, CSV, and other similar formats are invalid for this
assignment.

All timestamps must be stored in UTC and account for the difference between local time and UTC.


Report
------

Just like in forensic investigations, your work on this project must be accompanied by a 5-page report, 12 point, 1.5
space, 1" margins. Include the following in the report:

- Requirements of the project in your own words. This will help you ensure you've captured all the details from above
  and understand what is expected.
- Design decisions made and why, including programming language, method of storing and parsing the blockchain, etc.
- Challenges you faced while working on the project and your solutions. Include any other lessons learned.
- Discussion on why a blockchain *is not* an appropriate choice for a production chain of custody solution.

I encourage you to include screenshot in your report, but know that they do not count toward your 5-page requirement, so
they should be part of an appendix and referenced accordingly in the text.


Checkpoint
----------

To help make sure you are on track to complete the project on time, you are required to submit an initial version of
your project by March 28 that includes the following functional elements:

1. ``bchoc init``
2. ``bchoc verify``

You are not required to submit a report for the checkpoint. All other submission guidelines apply.


Submission
----------

More details to come!



.. |blockquote_options| raw:: html

   <blockquote class="options_table">

.. |eblockquote| raw:: html

   </blockquote>
