:heading: CSE 469 Computer and Network Forensics
:subheading: Spring 2019

.. include:: course_info.txt
   :end-before: start_instructor_info

========
Syllabus
========

.. include:: course_info.txt
   :start-after: start_instructor_info

Course Description
------------------

This course discusses identification, extraction, documentation, interpretation, and preservation of computer media for
evidentiary purposes and/or root cause analysis. Topics include techniques for discovering digital evidence; responding
to electronic incidents; tracking communications through networks; understanding electronic media, crypto-literacy, data
hiding, and system forensics; and the role of forensics and in the digital environment [#]_.


Prerequisites
-------------

Per the `course description <https://webapp4.asu.edu/catalog/course?t=2191&r=14879>`_: CSE 310 (Data Structures and
Algorithms) with C or better OR Computer Science and Engineering or Software Engineering graduate student.


Textbook
--------

All required information for the course will be provided in the lectures. However, I highly recommend these textbooks
for those wanting to gain a deeper understanding of the principles we will discuss:

- `Guide To Computer Forensics and Investigations
  <https://smile.amazon.com/Guide-Computer-Forensics-Investigations-Standalone-dp-1337568945/dp/1337568945/>`_ by Bill
  Nelson, Amelia Phillips, and Christopher Steuart

  - ISBN: 1337568945
  - Whether you get the Standalone Book (paperback bound) or the Loose-leaf Version (essentially a 3-ring binder) is
    your preference.

- `File System Forensic Analysis <https://smile.amazon.com/System-Forensic-Analysis-Brian-Carrier/dp/0321268172/>`_ by
  Brian Carrier

  - ISBN: 0321268172
  - An excellent resource if you want more detail about a variety of filesystems.

Other related books:

- Digital Evidence and Computer Crime. Eoghan Casey, Academic Press. 2011.
- Computer Forensics: Incident Response Essentials. Warren G. Kruse II and Jay G. Heiser. Addison Wesley. 2002.
- Incident Response. E. Eugene Schultz and Russell Shumway. New Riders. 2002.


Course Communication
--------------------

**All announcements and communications for the class will take place on Piazza:**
https://piazza.com/asu/spring2019/cse469/home

Students may use Piazza to ask questions on any topic from the lectures or to discuss homework assignments. The TA,
Instructor, or other students can respond or contribute to existing responses. Piazza is an awesome resource, but it
requires the use of common sense. For example:

- Do *not* post your code.
- Do *not* share solutions or answers.
- **Do** describe your question at a conceptual level.
- **Do** help point out others' mistakes.
- **Do** direct others to resources that will help them solve their own problem.
- Do *not* assume this list is exhaustive! ;)

.. warning::
   Sharing solutions, answers, code, etc. is expressly prohibited and will result in academic sanctions. Review the
   section below on Academic Integrity for more information.

.. important::
   Questions meant for the professor and/or TA should be sent as a *private post* on Piazza.

.. note::
   If you email the instructor or TA directly and we determine it will be useful for the rest of the class, we will
   repost it to Piazza.

.. seealso::
   The advice in `"How to Ask Questions the Smart Way" <http://www.catb.org/~esr/faqs/smart-questions.html>`_ will
   increase the chances of others answering your question.



Topics
------

.. important::
   The following is only a list of *possible* topics we will cover throughout the semester and may change as the
   semester progresses. Check the following sections on the `course homepage <index.html>`_ for the most up-to-date
   information:

   - `Important Dates <index.html#important-dates>`_
   - `Lecture Slides <index.html#lecture-slides>`_
   - `Schedule & Lecture Recordings <index.html#schedule-lecture-recordings>`_

#. Computing Basics

   #. File Systems
   #. Operating Systems
   #. Network

#. Computer Forensics Principles

   #. Acquisition/Preparation
   #. Authentication/Identification
   #. Analysis/Examination
   #. Documentation/Presentation
   #. Rules of Evidence

#. Computer Forensic Technologies

   #. Data Forensics
   #. Systems Forensics
   #. Network Forensics
   #. Malware Forensics
   #. Mobile Forensics

#. Computer Forensic Tools

   #. Commercial Tools
   #. Open Source Tools

#. Incident Responses

   #. Ethical Hacking Techniques
   #. Vulnerability Assessment
   #. Penetration Testing

#. Cybercrime Investigation

   #. Crimes and Violations
   #. Cybercrime Trends
   #. Forensic Accounting

#. Other Issues

   #. Ethics and Legal Issues
   #. Standards
   #. Reporting Requirements
   #. Hardware Reverse Engineering


Grading Policy
--------------

+------------+--------------------------+
| Area       |  Weight                  |
+============+==========================+
| Homework   | - Assignments: 35%       |
|            | - Course Project: 20%    |
|            | - Paper presentation: 5% |
+------------+--------------------------+
| Exams      | - Midterm: 15%           |
|            | - Final: 25%             |
+------------+--------------------------+
| Attendance | Will affect your grade   |
+------------+--------------------------+

Homework will consist of several exercises that reinforce the principles we will discuss in class. Unless otherwise
noted in an assignment description, all work is to be completed individually. Assignments and their due dates will be
posted to the course web site.

Groups of two will complete a course project that will be due by the end of the semester. There are never any penalties
for submitting assignments and projects early.

Each student is required to submit a report on a research paper from a list posted on the course web site. The report
must include a brief summary of the paper, critiques (strengths and weaknesses), and possible enhancements with some
research reasoning. The report must be at least 4 pages, 12 point, 1.5 space, 1" margins. Some extra points may be given
for reports compiled from LaTeX.

In addition to the paper report, every *honors student* and *graduate student* must also give a presentation on their
paper lasting 20 minutes plus Q&A. The presentation should include a clear introduction to the concept of the proposed
ideas or approaches, including some scientific reasoning about the paper's content. Undergraduate students may volunteer
to do a paper presentation for extra points. More details will be provided in the first couple weeks of class.

Late work will receive a deduction of 20% per day late. Exceptions to this policy will be at the discretion of the
instructor.

Exams will be administered in class. No notes, books, laptops, phones, smart devices (including watches), or calculators
are allowed during exams unless otherwise announced by the instructor in advance. Makeup exams will not be given except
in extenuating circumstances as determined by the instructor.

If an exam date conflicts with a religious holiday (in accordance with `ACD 304-04
<http://www.asu.edu/aad/manuals/acd/acd304-04.html>`_) or other university sanctioned activities (in accordance with
`ACD 304-02 <http://www.asu.edu/aad/manuals/acd/acd304-02.html>`_) the student must inform the instructor at least two
weeks before the exam date to schedule a makeup exam.


Special Accommodations
----------------------

Students requesting disability accommodations should register with the Disability Resource Center (DRC) and present the
instructor with appropriate documentation from the DRC.


Academic Integrity
------------------

Cheating will not be tolerated. Plagiarism, misrepresentation of work, falsification, or any other form of cheating will
result in any or all of the following: 1) receiving no credit for the work in question, 2) failure of the course (grade
XE “failure due to academic dishonesty”), 3) referral to the department administration and/or dean, 4) other
disciplinary actions as appropriate to the offense.

To understand your responsibilities as a student read: `ASU Student Code of Conduct
<http://www.asu.edu/aad/manuals/usi/usi104-01.html>`_ and `ASU Student Academic Integrity Policy
<http://provost.asu.edu/academicintegrity/policy>`_.

Students are allowed to use snippets of code found online (e.g., StackOverflow) as long as proper credit for the source
is given in a comment in your code **AND** as long as the snippet does not constitute a significant portion of your
code **AND** as long as the source is not another past or present student of the course.

Posting your assignment code online is expressly forbidden, and will be considered a violation of the academic integrity
policy. Note that this includes working out of a *public* GitHub repo. The GitHub Student Developer Pack provides
unlimited private repositories while you are a student. If you want to impress employers with your coding abilities,
create an open-source project that is done outside of class.


----

.. [#] © Copyright 2019, Mike Mabey. Copyright applies to all course materials, including, but not limited to: lecture
   slides, lecture recordings, assignment descriptions and solutions, the syllabus, and all components and source code
   of the course web site. Any recording of video, audio, or other form of digital recordings during class, without
   written authorization from Dr. Mabey, is prohibited. The sale of of any course materials, including notes taken by
   students, is also prohibited.
