---
title: Spring 2021 - Cpt_S 360 - Systems Programming
date: 2021-03-01T00:00:00Z
draft: false
type: book
toc: true
linktitle: Cpt_S 360
weight: 1
---
<br>

## General Information

| Day/Time/Venue                              | Tuesday & Thursday / 1:30pm to 2:45pm / Zoom (ID: 920-9989-9866)                                                                                                                                                                                         |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Instructor                                  | Hassan Ghasemzadeh, Email: `hassan.ghasemzadeh@wsu.edu` <br> - Office Hours: Tuesdays 3pm to 4pm or by appointment.                                                                                                                                      |
| Pre-requisite                               | Basic knowledge and working experience in Unix commands; ability to program in C or C++                                                                                                                                                                  |
| Teaching Assistant (TAs)  and  Office Hours | Mahdi Pedram (`mahdi.pedram@wsu.edu`) <br>  - Monday and Thursday 12:00pm-1:00pm; Zoom Meeting ID: 513 382 9496         <br><br> Austin Nasralla (`austin.nasralla@wsu.edu`) <br>  - Tuesday and Thursday 10:30am-11:30am; Zoom Meeting ID: 782 546 7124 |
| Main Textbooks                              | \- Systems Programming in Unix/Linux, K.C. Wang, Springer International AG, 2018 <br> - Design and Implementation of the MTX Operating System, K.C. Wang, Springer International AG, 2015                                                                |
| Additional Textbook                         | Operating System Concepts, 10th Edition, Abraham Silberschatz, Greg Gagne, Peter B. Galvin, ISBN: 978-1-119-32091-3, April 2018, 1040 Pages                                                                                                              |

{{% callout note %}}
For the Zoom passcode, either contact Austin or refer to the ‘TAs’ folder in Blackboard
{{% /callout %}}

## Topics Covered

The following table shows the main topics that will be covered in this course.

| **No.** | **Topic**                                        | **Details**                                                                                                                                                                                             |
| ------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1       | Introduction to Unix/Linux and Operating Systems | Files, directories, special files, logical organization of Unix file system; user account, login process and command execution                                                                          |
| 2       | Program development                              | Source files; compiler, assembler and object files; linker, library and executable files; loader and execution images; symbolic debugger and run-time support                                           |
| 3       | Execution image of C programs                    | Code, data and stack segments; function calling convention, stack frames and parameter passing; long jumps                                                                                              |
| 4       | File Input/Output (I/O)                          | System calls and low-level file I/O; open, close, read, write, lseek, file descriptors and file sharing; execution of user mode and kernel mode images, implementation and implications of system calls |
| 5       | File Control                                     | Permissions and access control, fcntl, chown, chmod, hard and soft links, file status and statistics; I/O redirection, pipes, filters and applications                                                  |
| 6       | Standard I/O Library                             | Streams and high-level file I/O; user space buffering, relationship with low-level I/O, char and line mode I/O; formatted I/O.                                                                          |
| 7       | File system implementation                       | Inodes and file representation; mkfs and physical file system layout; traversal of the file system tree; booting system images                                                                          |
| 8       | Processes                                        | Concept and implementation of processes, process execution environment, user mode and kernel mode images, process states transitions; processes in the Unix system; init, login and user processes      |
| 9       | Process Control                                  | fork, vfork, wait, exit, kill, exec operations. traps and signal handling                                                                                                                               |
| 10      | Process Synchronization and Communication        | Signals, pipes, semaphores, messages and shared memory segments; sockets                                                                                                                                |
| 11      | Concurrent Programming                           | Threads and parallel programming                                                                                                                                                                        |
| 12      | Networking                                       | Introduction to Internet; host, address resolution, routing; protocols, client and server; ftp, rlogin, nfs, and nis, socket programming                                                                |

## Statement of Reasonable Accommodation

Reasonable accommodations are available for students with a documented disability. If you have a disability and need accommodations to fully participate in this class, please either visit or call the Access Center (Washington Building 217; 509-335-3417) to schedule an appointment with an Access Advisor. All accommodations MUST be approved through the Access Center. for more information contact a Disability Specialist @ 509-335-3417, [http://accesscenter.wsu.edu](http://accesscenter.wsu.edu]), `Access.Center@wsu.edu`.

## Campus Safety Information

Review the Campus Safety Plan <http://safetyplan.wsu.edu/> and visit the Office of Emergency Management website <http://oem.wsu.edu/> for a comprehensive listing of university policies, procedures, statistics, and information related to campus safety, emergency management, and the health and welfare of the campus community.

## Cheating Policy

Limited cooperation among students on homework assignments and programming projects is encouraged. Students may discuss meaning of the assignments and possible directions on how to solve the problems. However, any written portion of an assignment MUST be the student’s work. Copying from other students or allowing other students to copy your work is considered to be cheating and will result in a reduced or a failing grade.

## Grading Policy

* Programming assignments 30%
* Homework assignments 10%
* Midterm 30%
* Project 30%

Letter grades are calculated according to the following table:

| **Percentage grade threshold** | **Letter grade** |
| ------------------------------ | ---------------- |
| 90 (total points >= 90)        | A                |
| 87                             | A-               |
| 83                             | B+               |
| 80                             | B                |
| 77                             | B-               |
| 73                             | C+               |
| 70                             | C                |
| 67                             | C-               |
| 63                             | D+               |
| 60                             | D                |
| < 60                           | F                |

## Assignments

A late penalty of 10% will be assessed for late submissions within the next 24 hours (i.e., until midnight of the next day after the submission deadline). After this one-time late submission, no submissions will be accepted.

## Grades

Grades will be posted on WSU Blackboard approximately two weeks after the due date for each assignment.

## Announcements

* 01/21/2021: HW1 and L1 are posted.
* 01/21/2021: “01 - Logistics and Introduction” slides are posted.
* 01/26/2021: L2 is posted.
* 02/01/2021: L3 is posted.
* 02/04/2021: “02 - Program Development” slides are posted.
* 02/04/2021: L4 is posted.
* 02/11/2021: L5 is posted.
* 02/18/2021: HW2 is posted.
* 02/18/2021: “03 - Process Management” slides are posted.
* 02/19/2021: L6 is posted.
* 02/23/2021: “04 - Concurrent Programming” slides are posted.
* 03/06/2021: L7 is posted.
* 03/07/2021: L8 is posted.
* 03/12/2021: L9 is posted.

## Course Schedule

| **Week of** | **Topics**                                                                       | **Readings**                                                                                                           | **Comments**                           |
| ----------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| Jan. 18     | \- Introduction to Unix/Linux <br> - Operating Systems<br> - Program development | Systems Programming:<br>  - (1.8, 1.9, 1.15, 2.3, 2.4)                                                                 | HW1 and L1 are posted.                 |
| Jan. 25     | \- Program development                                                           | Systems Programming: <br>  - (2.5, 2.9, 2.10)                                                                          | L2 is posted.                          |
| Feb. 1      | \- Program development<br> - Process management                                  | Systems Programming: <br>  - (2.7, 2.8, 2.13, 3.1, 3.2)<br> Operating System Concepts: <br>  - (3.1)                   | L3 and L4 are posted.                  |
| Feb. 8      | \-Process management                                                             | Systems Programming: <br>  - (3.4, 3.5, 3.7, 3.8) <br> Operating System Concepts: <br>  - (3.3)                        | L5 is posted.                          |
| Feb. 15     | \- Process management<br> - Concurrent programming                               | Systems Programming: <br> - (3.9, 3.10, 4.1, 4.2, 4.3, 4.4, 4.5) <br> Operating System Concepts:<br> - (4.1, 4.2, 4.4) | HW2 is posted. L6 is posted.           |
| Feb. 22     | \- Concurrent programming                                                        | Systems Programming:<br> - (4.5, 4.6.1) <br> Operating System Concepts:<br> - (6.1, 6.2, 6.5)                          | No class on Thursday Feb. 25           |
| Mar. 1      | \- Concurrent programming                                                        | Systems Programming: <br>  - (4.6.6, 4.6.7)                                                                            | Midterm on March 4th during class time |
| Mar. 8      | \- Concurrent programming<br> - Network programming                              | Systems Programming: <br>  - (4.6.2, 4.6.3, 4.6.4, 4.6.5, 13.1-13.15)                                                  | L7, L8, L9 are posted.                 |
| Mar. 15     |                                                                                  |                                                                                                                        |                                        |
| Mar. 22     |                                                                                  |                                                                                                                        |                                        |
| Mar. 29     |                                                                                  |                                                                                                                        |                                        |
| Apr. 1      |                                                                                  |                                                                                                                        |                                        |
| Apr. 12     |                                                                                  |                                                                                                                        |                                        |
| Apr. 19     |                                                                                  |                                                                                                                        |                                        |
| Apr. 26     |                                                                                  |                                                                                                                        |                                        |
| May 3       |                                                                                  |                                                                                                                        |                                        |