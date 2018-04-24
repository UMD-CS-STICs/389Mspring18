# Final: Kalman Filter SLAM
#### Due: 5/4/18 @ 11:59 PM

Please complete the code in `kfslam.py`. All directions are in there.

You can test your code with `python sim3.py` when in the virtual environment.

## Questions (Written Response)
1. Notice how all of the covariances visualized seem to be ellipses with major and minor axes parallel to the x and y axes. Why is it that these ellipses are never oblique? 
2. What happens when the car spawns far away from any observable landmarks and has to move to see the first one? Why does this happen? How could this behavior be fixed?
3. Observe the following map (where the green dots are landmarks and the red ellipses are covariances):
![Imgur](https://i.imgur.com/mp3yCSr.png)

How certain could the robot possibly be about its location? In other words, what is the lower bound for the covariance, and why? Your claim could look something like "larger than the top landmark's covariance" or "as small as the left landmark's covariance."


## Grading
35% Code Inspection
35% Visual Inspection
30% Written Responses

## Submission
Please turn in a `submission.zip` on ELMS that contains a pdf of your written responses, and `kfslam.py`.
