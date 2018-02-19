# CMSC389M: SLAM: Why Robots Don't Crash
![Particle Filter Localization](https://i.imgur.com/EGzbpMn.png?1)

## Course Description

Students will be provided with a practical and lightly theoretical understanding of the most popular algorithms that solve the Simultaneous Localization and Mapping (SLAM) problem to enable self driving car technology. An emphasis will be placed on the probabilistic methods that underpin the SLAM problem.

## Learning Objectives

By the end of the course, students will understand
- the challenges of noisy measurement
- probability as a way to quantify uncertainty
- the different approaches to the SLAM problem and thier tradeoffs
- how to program the basics of SLAM algorithms using Python

## Course Topics

- Probability Review
    + Total Probability
    + Bayes' Rule
    + Conditional Probability
- Localization with Bayesian Filters
    + Histogram Filter
    + Kalman Filter
    + Particle Filter
- Simultaneous Localization and Mapping
    + FastSlam
    + EKF Slam

## Course Details

- **Course:** CMSC389M
- **Prerequisites:** CMSC216 and CMSC330
- **Credits:** 1
- **Seats:** 30
- **Location:** CSI 3118
- **Semester:** Spring 2018
- **Textbook:** None
- **Extra Reading:** [Probabilistic Robotics](http://www.probabilistic-robotics.org/) by Thrun, Burgard, and Fox
- **Course Facilitators:** [Michael Stevens](https://www.linkedin.com/in/michael-stevens-268074123/), [Ishaan Parikh](https://www.linkedin.com/in/iparikh/)
- **Office Hours:** Wednesdays, 3:30 - 5PM in Sandbox (3rd floor CSIC)
- **Faculty Advisor:** [Dr. Larry Davis](https://www.cs.umd.edu/people/lsdavis)
- **Links**: \[[Piazza](https://piazza.com/class/jblmlyocd2x7x)\]\[[Testudo](https://ntst.umd.edu/soc/search?courseId=CMSC389M&sectionId=&termId=201801&_openSectionsOnly=on&creditCompare=&credits=&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on)\]

## Schedule
| Week | Topic                               | Homework | Project Checkpoints Due|
| ---- | ----------------------------------- | -------- | -------                |
| 1    | Introduction + Probability Intuition |         |                        |
| 2    | Probability Theory + Python Setup | 1 OUT   | |              |           
| 3    | Codelab + 2D Monte Carlo     | 1 DUE   |          |
| 4    | Project Intro + Motion Models              |         |    OUT          |
| 5    | Kalman Filter 1                     | 2 OUT       |      |
| 6    | Kalman Filter 2                     |          |             Part 1   |
| 7    | Particle Filter 1                   | 2 DUE, 3 OUT |            |
| 8    | Particle Filter 2 + Review          |  3 DUE|    Part 2     |
| 9    | Midterm                             |           |         |
| 10   | SLAM Overview + Correspondence Problem | 4 OUT   | Part 3 |
| 11   | Extended Kalman Filter SLAM 1       | 4 DUE, 5 OUT        |      |
| 12   | Extended Kalman Filter SLAM 2       |          |         |
| 13   | Extended Kalman Filter SLAM 3       |          |         |
| 14   | FastSLAM 1                          | 5 DUE        |         |
| 15   | FastSLAM 2                          |          | Part 4 |

## Project

The project for the semester is implementing the algorithms described in class in a 2D simulated environment. As we continue in the class, we will build on the project. The four parts are broken up into the following:

- Part 1: 2D Histogram Location
- Part 2: Kalman Filter Tracking
- Part 3: 3D Particle Filter
- Part 4: SLAM (TBD)

The checkpoints are due at 11:59 PM on the day of the class listed on the above schedule. Please zip up your project folder and turn it into the submit server.

## Grading
| % Total | Assignment            | Description                               |
| ------- | --------------------- | ----------------------------------------- |
| 10%      | In-class Worksheets    | Designed to engage students during slideshow presentations. Graded for completion |
| 25%     | Homeworks             | Short writen assignments. Graded for accuracy |
| 45%     | Project               | There will be one semester long four part project covering the topics learned in class. |
| 20%     | Midterm               | Will cover material from the first 8 weeks |

## Administrivia

### Project Submission

Projects must be submitted electronically following the instructions given in each project assignment. Projects may not be submitted by any other means (e.g., please do not email your projects to us). It is your responsibility to test your program and verify that it works properly before submitting. All projects are due at 11:59:59 PM on the day indicated on the schedule above.

Projects may be submitted up to 24 hours late for a 20% penalty. If you submit both on-time and late, your project will receive the maximum of the penalty-adjusted scores. Only the last on-time and last late projects will be graded.

### Course Staff Communications

Students can interact with the instructors in two ways: in-person during office hours and online via Piazza. Email should only be used for emergencies and not class related questions (e.g., projects).

### Excused Absence and Academic Accommodations

See the section titled "Attendance, Absences, or Missed Assignments" available at [Course Related Policies](http://www.ugst.umd.edu/courserelatedpolicies.html).

### Disability Support Accommodations

See the section titled "Accessibility" available at [Course Related Policies](http://www.ugst.umd.edu/courserelatedpolicies.html).

### Academic Integrity

Note that academic dishonesty includes not only cheating, fabrication, and plagiarism, but also includes helping other students commit acts of academic dishonesty by allowing them to obtain copies of your work. In short, all submitted work must be your own. Cases of academic dishonesty will be pursued to the fullest extent possible as stipulated by the Office of Student Conduct.

It is very important for you to be aware of the consequences of cheating, fabrication, facilitation, and plagiarism. For more information on the Code of Academic Integrity or the Student Honor Council, please visit: http://www.shc.umd.edu.

### Course Evaluations

If you have a suggestion for improving this class, don't hesitate to tell the course staff during the semester in-person, over email/Piazza, or through the weekly feedback surveys. At the end of the semester, please don't forget to provide your feedback using the campus-wide CourseEvalUM system. Your comments will help make this class better.
