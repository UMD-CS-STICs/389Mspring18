import sys
sys.path.append('./')
import numpy as np
from histfilter_sol import HistogramFilter
from robot import RobotBin
from landmark import Landmark


def test_move():
    robot = RobotBin(20, 175, 'car.png', None, [], [], None)
    hfilter = HistogramFilter(1, 6, 6, [Landmark(0, 0, None)], robot)
    hfilter.belief = np.array(
        [[1.,  1.,  1.,  1.,  1.,  1.],
         [1.,  1.,  1.,  1.,  2.,  4.],
         [1.,  6.,  7.,  4.,  1.,  1.],
         [1.,  6.5, 10.,  1.,  1.,  1.],
         [1.,  8.,  3.,  3.,  1.,  1.],
         [1.,  1.,  1.,  1.,  1.,  1.]]
    )

    hfilter.motion_update((0, 0))
    hfilter.motion_update((3, 2))

    correct = np.array(
        [[0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
         [0.00000000e+00, 0.00000000e+00, 5.59269337e-13,
             3.29315482e-09, 3.29371409e-09, 3.29315482e-09],
         [0.00000000e+00, 0.00000000e+00, 1.69798993e-04,
             9.99830198e-01, 9.99999997e-01, 9.99830198e-01],
         [0.00000000e+00, 0.00000000e+00, 1.69798994e-04,
             9.99830201e-01, 1.00000002e+00, 9.99830221e-01],
         [0.00000000e+00, 0.00000000e+00, 1.69798994e-04,
             1.00067920e+00, 5.99932079e+00, 6.99864160e+00],
         [0.00000000e+00, 0.00000000e+00, 1.69798993e-04, 1.00076409e+00, 6.49966038e+00, 9.99770767e+00]]
    )
    np.testing.assert_allclose(hfilter.belief, correct, rtol=1e-5)


def test_sense():
    landmarks = [Landmark(3, 3, None)]
    robot = RobotBin(0, 0, 'car.png', None, landmarks, [], None)
    hfilter = HistogramFilter(1, 10, 10, landmarks, robot)
    hfilter.belief = np.zeros((6, 6)) + (float(1) / 36)
    hfilter.z_noise = 0.5
    hfilter.sense_update([(0, 1)], (0, 0))

    correct = np.array(
        [[1.07307687e-06, 1.07126166e-04, 2.14493697e-03, 5.82993552e-03, 2.14493697e-03, 1.07126166e-04],
         [1.48037381e-05, 2.14493697e-03, 4.30754611e-02,
             1.17090636e-01, 4.30754611e-02, 2.14493697e-03],
         [3.96330630e-05, 5.82993552e-03, 1.17090636e-01,
             3.18284739e-01, 1.17090636e-01, 5.82993552e-03],
         [1.48037381e-05, 2.14493697e-03, 4.30754611e-02,
             1.17090636e-01, 4.30754611e-02, 2.14493697e-03],
         [1.07307687e-06, 1.07126166e-04, 2.14493697e-03,
             5.82993552e-03, 2.14493697e-03, 1.07126166e-04],
         [3.58496782e-07, 1.07307687e-06, 1.48037381e-05, 3.96330630e-05, 1.48037381e-05, 1.07307687e-06]]
    )
    np.testing.assert_allclose(hfilter.belief, correct, rtol=1e-5)

if __name__ == '__main__':
    test_move()
    test_sense()
    print 'All Tests Pass!'
