# Project 1: Histogram Filter
![](https://i.imgur.com/N6srxnr.png)
## Introduction
In this project you will write a Histogram Filter for a 2D simulated environment. The simulation consists of a car, a maze to navigate through, and randomly distributed landmarks (shown in green) that the robot can use to localize. The robot's belief distribution is drawn over the simulation (shown above in red). Once the simulation is started you can control the robot's motion with the arrow keys. Once you correctly impliment the Histogram Filter your robot should be able to localize itself as you navigate through the maze with the arrow keys. Public tests are provided to help you develop the filter.

## Your Task
All simulation code has been provided and should not be modified. If you find a problem, please make a piazza post to notify us. Skeleton code for the Histogram Filter has been provided in 'histfilter.py'; make all your modifications in this file. Below you will find the specifications for the motion and sensor models to use in the project. Though you could come up with your own, perfectly valid models, it is important that you impliment the models the way they are specified below so you pass the public tests and your project is graded correctly.

### Prediction Update
The robot is equiped with sensors that can detect changes in its (x, y) location. The robot automatically integrates this information into the variables x_odom and y_odom to create the odometry coordinate frame. Each change in x and y is independently corrupted with gaussian noise with a standard deviation of |displacement| \* c. So the model is:
![equation](http://bit.ly/2BrASwF)  
![equation](http://bit.ly/2BSCwsd)  
where c_x and c_y are constants. These constants are provided for you in the constructor of Histogram Filter as x_noise and y_noise. It is recommended that you implement the prediction update as a shift and a convolution. For the shift portion of the update you will have cells along the border of the histogram that don't have any values to shift into them; fill these cells with 0's. Don't do any kind of interpolation on the histogram, just shift the cells as close to the corresponding distance as you can. You are welcome to use any functions in the SciPy library to accomplish this. For the convolution portion, again pad the outside of the histogram with zeros so the belief histogram retains the same size. Use "scipy.ndimage.filters.gaussian_filter" to accomplish this.

### Sense update
The robot is equiped with sensors that can detect the (x, y) positions of landmarks *with respect to the robot's odometry.* This means in order to get the position of a detected landmark relative to the center of the robot, you have to first subtract the robot's x_odom and y_odom from the landmark's position. The detected (x, y) location of the robot is corropted with gaussian noise with a standard devation of z_noise. So the model is:  
![Equation](http://bit.ly/2BrOLuP)  
![Equation](http://bit.ly/2Bot6TY)  
where z_noise is a constant provided to you. It should follow from the above equations that the difference between x_observed and x_true should be normally distributed with a standard deviation of z_noise. Note that the probability density function of the gaussian with 0 mean is   ![Equation](http://bit.ly/2BVxcE6)  
Which we will now denote as prob(x). It follows that  
![Equation](http://bit.ly/2Br0RnN)

However, in addition to not being able to determine the precise location of these landmarks, the robot only detects a landmark with probability *phit*. Whats more, with probability *pfalse* the robot will detect dubious landmarks that are not in our map. When detected these dubious landmarks are uniformly distributed in a circle around the robot's location with radius equal to *max_sense_dist*. The constants *phit*, *pfalse*, and *max_sense_dist* are provided to you in *histfilter.py*. Assume independence between different landmark observations (This means that ![Equation](http://bit.ly/2BSZob3)) where z_1 through z_n are different landmark observations.

## Questions for When You're Done
1. Why'd it do this?
2. Why do that

## Grading
How the grading will work
