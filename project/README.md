# Final: Kalman Filter SLAM
#### Code Due: 5/4/18 @ 11:59 PM, Written Responses Due: 5/10 @ 11:59 PM

Please complete the code in `kfslam.py`. All directions are in there.

You can test your code with `python sim3.py` when in the virtual environment.

## Questions (Written Response)
1. Define loop closure and give an example.
2. What advantages does KF SLAM have over FastSLAM for loop closure?
3. Notice how all of the covariances visualized seem to be ellipses with major and minor axes parallel to the x and y axes. Why is it that these ellipses are never oblique?
4. What happens to the quality of the solution to the SLAM problem when the car spawns far away from any observable landmarks and has to move to see the first one? Why does this happen? How could this behavior be fixed?
5. Observe the following map (where the green dots are landmarks and the red ellipses are covariances):  
![Imgur](https://i.imgur.com/mp3yCSr.png)  
How certain could the robot possibly be about its location if it used this map to localize? In other words, what is the lower bound for the covariance, and why?
6. Given sufficient time and under the correct conditions, KF SLAM will be equally certain about the locations of all landmarks. Given the map above, what is the lower bound on how certain each landmark can be?
7. When the robot first observes a new landmark, what is the lower bound on how certain the robot can be of the landmark's position?
8. Tradional SLAM algorithms are passive, meaning they just process the information the robot has available and don't influence the robot's motion decisions. Explain how an "active" SLAM algorithm, in which the sense steps actually influence how the robot moves, could improve the time it would take the algorithm to obtain a reasonable estimate for all the landmarks.


## Grading
35% Code Inspection

35% Visual Inspection

30% Written Responses

## Submission
Please turn in a `submission.zip` of your code and a pdf (or other text file) of your written responses on ELMS.
