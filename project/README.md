# Project 1: Histogram Filter
![](https://i.imgur.com/N6srxnr.png)
## Introduction
In this project you will write a Histogram Filter for a 2D simulated environment. The simulation consists of a car, a maze to navigate through, and randomly distributed landmarks (shown in green) that the robot can use to localize. The robot's belief distribution is drawn over the simulation (shown above in red). Once the simulation is started you can control the robot's motion with the arrow keys. Once you correctly implement the Histogram Filter your robot should be able to localize itself as you navigate through the maze with the arrow keys. Public tests are provided to help you develop the filter.

## Your Task
All simulation code has been provided and should not be modified. If you find a problem, please make a piazza post to notify us. Skeleton code for the Histogram Filter has been provided in `histfilter.py`; make all your modifications in this file. You can run the simulation by executing `python sim.py` in the main project directory. Below you will find the specifications for the motion and sensor models to use in the project. Though you could come up with your own, perfectly valid models, it is important that you implement the models the way they are specified below so you pass the public tests and your project is graded correctly.

### Prediction Update
The robot is equiped with sensors that can detect changes in its (x, y) location. The robot automatically integrates this information into the variables robot.x_odom and robot.y_odom to create the odometry coordinate frame. This "coordinate frame" represents the robots location calculated only through odometry (integrating distance moved). Each change in x and y is independently corrupted with gaussian noise with a standard deviation of |displacement| \* c. So the model is:
<!--- x_{observed} &= x_{true} + \mathcal{N}(0, |x_{true}|*c_x) \\ --->
<!--- y_{observed} &= y_{true} + \mathcal{N}(0, |y_{true}|*c_y) --->

![equation](http://quicklatex.com/cache3/94/ql_300dda2293cf9d58928b2096f735a594_l3.png)  

where c_x and c_y are constants. These constants are provided for you in the constructor of Histogram Filter as x_noise and y_noise. It is recommended that you implement the prediction update as a shift and a convolution. For the shift portion of the update you will have cells along the border of the histogram that don't have any values to shift into them; fill these cells with 0's. Don't do any kind of interpolation on the histogram, just shift the cells as close to the corresponding distance as you can. You are welcome to use any functions in the SciPy library to accomplish this. For the convolution portion, again pad the outside of the histogram with zeros so the belief histogram retains the same size. Use "scipy.ndimage.filters.gaussian_filter" to accomplish this.

### Measurement update
The robot is equiped with sensors that can detect the (x, y) positions of landmarks *with respect to the robot's odometry.* This means in order to get the position of a detected landmark relative to the center of the robot, you have to first subtract the robot's x_odom and y_odom from the landmark's position. The detected (x, y) location of the robot is corrupted with gaussian noise with a standard devation of z_noise. So the model is:  
<!--- (y_{observed} &= y_{true} + \mathcal{N}(0, z_{noise}) --->
![Equation](http://quicklatex.com/cache3/c9/ql_d17bef13145f5c9e6976b974c6b11bc9_l3.png)

where z_noise is a constant provided to you in histfilter.py. It should follow from the above equations that the difference between x_observed and x_true should be normally distributed with a mean of 0 and a standard deviation of z_noise. Note that the probability density function of the gaussian with 0 mean is  
<!--- f(x | \sigma^2) = \frac{1}{{\sqrt {2\pi\sigma^2 } }}e^{{{ - \left( {x} \right)^2 } \mathord{\left/ {\vphantom {{ - \left( {x - \mu } \right)^2 } {2\sigma ^2 }}} \right. \kern-\nulldelimiterspace} {2\sigma ^2 }}} --->
![Equation](http://quicklatex.com/cache3/40/ql_a84e9ae2baa944fe9b81ae7fca5e3d40_l3.png)  
Which we will now denote as prob(x, sigma). Since the x and y direction are corrupted independently, it follows that
<!--- P(z | x_t) = prob(z_{x_{true}} - z_{x_{observed}}, z_{noise}) * prob(z_{y_{true}} - z_{y_{observed}}, z_{noise}) --->
![Equation](http://quicklatex.com/cache3/68/ql_99ac667c7648495d055aac0e6a7f4168_l3.png)  
Note that prob(x, sigma) is a probability *density* not a probability, which means it is proportional to the correct probability. This is ok because at the end of the measurement update we normalize, effectively multiplying by the correct factor. 

However, in addition to not being able to determine the precise location of these landmarks, the robot only detects a landmark with probability *phit*. Whats more, with probability *pfalse* the robot will detect dubious landmarks that are not in our map. When detected these dubious landmarks are uniformly distributed in a circle around the robot's location with radius equal to *max_sense_dist*. The constants *phit*, *pfalse*, and *max_sense_dist* are provided to you in *histfilter.py*. Assume independence between different landmark observations. This means that  
<!--- P(z_1, z_2, ..., z_3|x_t) = \prod P(z_i|x_t) --->
![Equation](http://quicklatex.com/cache3/9f/ql_26c042fbd5c88ff571fcee9048a35b9f_l3.png)  
where z_1 through z_n are different landmark observations.

## Questions for When You're Done
1. Move the robot around with the arrow keys until it is sufficiently localized. Now move into an area of the maze where it cannot see any landmarks. As you continue to move in this region without landmarks, what happens to the belief? Why?
2. Restart the simulation until you get a randomly get a maze where the robot can only see one landmark. What does the belief look like after only a couple observations of that one landmark (hint: if things are going to fast for you to see, in sim.py change `clock.tick(10)` to something like `clock.tick(1)` to make time go slower)? Why does this happen? Would this still happen if our correspondence function was able to uniquely identify each landmark? Why?
3. You should notice that the filter sometimes loses the robot. Can you identify any weakenesses in the measurement model or the map that can explain this?
4. In `sim.py`, comment out `hfilter.motion_update(odom)` so that the filter only performs the measurement update. Move around the maze and try to get the robot to localize. What do you notice? Why is the motion update important?

## Grading
* 50% score on the public tests
* 40% answers to the questions
* 10% visual verifcation by running the simulation

Equations by http://quicklatex.com/
