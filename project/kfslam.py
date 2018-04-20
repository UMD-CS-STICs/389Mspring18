import numpy as np


class KFSlam(object):
    # Our state vector is going to look like the following
    # [ [robot_x],
    #   [robot_y],
    #   [landmark_i_x],
    #   [landmark_i_y],
    #   [landmark_j_x],
    #   [landmark_j_y],
    #   [landmark_k_x],
    #   [landmark_k_y],
    #   [landmark_l_x],
    #   [landmark_l_y],
    #       ...
    #               ]
    # and will grow whenever we observe a new landmark. Keep in mind
    # that even though each landmark has a unique id that we observe,
    # we may not observe them in order of the their unique ids. For
    # example, we may observe landmark 10 first and need to insert that
    # at spots [2,0] and [3,0]. Because of this, we need to track of where
    # we insert each landmark in our state. We have created a hash
    # landmark_id_to_index for this purpose, but you are welcome to do
    # this however you want!

    def __init__(self, robot):
        self.landmark_id_to_index = {}
        self.covariance = np.array([[0, 0], [0, 0]])
        self.state = np.array([[robot.x], [robot.y]])
        self.x_noise = robot.x_noise
        self.y_noise = robot.y_noise

    # STEP 1: A
    # Remember that A is not constant because the dimensions of your state/covariance
    # matrices will be changing! This means that you should create a function that
    # you can call (with self.A()) to return to you the matrix you need. Remember in
    # other examples in class, we had velocity and position in our state, but now we
    # just have the position. So, how does the state changed just based on the
    # knowledge of the previous state? Remember that you can get the size of your
    # current state vector as slef.state.
    def A(self):
        pass

    # STEP 2: B
    # B is how you translate your control signal into a change for your state. In this
    # case, the control signal will be velocity (2x1 vector). Think about how this affects
    # all the values in your state vector.
    def B(self):
        pass

    # We have implemented R for you. Just call self.R(control_signal) when you
    # need it.
    def R(self, control_signal):
        n = self.state.shape[0] - 2
        result = np.diag(
            np.hstack(([self.x_noise, self.y_noise], np.zeros(n))))
        result[0, 0] *= abs(control_signal[0, 0])
        result[1, 1] *= abs(control_signal[1, 0])
        return result

    # We have also implemented I for you. Just call self.I() when you need it.
    def I(self):
        return np.identity(self.state.shape[0])

    # Step 3: Prediction Update
    # Your prediction update should look almost identical to how it looked in the
    # previous project. Remember that when you call A or B, you need to call it
    # using self.A() or self.B().
    def prediction(self, control_signal):
        pass

    # Step 4: Measurement Update
    # The measurements array looks like:
    # [ { 10: (x,y) }, { 8: (x,y) }, { 2: (x,y) }]
    # and Q is a 2x2 matrix we just give to you.
    def measurement(self, measurements, Q):
        # Step 4a: Adding new landmarks
        # For the first part of the measurement update, you need to add all of the
        # new landmarks to our state and covariance matrices to be tracked. Remember,
        # we need to keep track of where we insert them into our state vector. Why?
        # Because we will need to constuct C later.
        #
        # We suggest looking up the following functions:
        # np.concatenate(), np.append()
        for measurement in measurements:
            pass

        # Step 4b: Update
        # For each of the measurements, we want to perform the updates. The C matrix
        # here is going to change based on the id of the landmark (and its position
        # in your state vector), and so make sure you are using that!
        for measurement in measurements:
            pass
