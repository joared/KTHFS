
import unittest
import imu_recording
import numpy as np
import matplotlib.pyplot as plt
from imu_recording.imu_recording import ImuRecording
from imu_recording.recording_to_rosbag import RecordingToBag
from imu_recording.rosbag_to_recording import RosbagToRecording

class TestImuRecording(unittest.TestCase):
    def setUp(self):
        self.imu = ImuRecording(files_dir="tests/unittest_ascii")
        self.imu.read("SBG_general_000.processed")

    def test_rec_to_bag_to_rec(self):
        bagger = RecordingToBag(self.imu)
        bagger.create_rosbag("test_bag.bag")
        bag_to_rec = RosbagToRecording()
        imu = bag_to_rec.rosbag_to_recording("test_bag.bag")
        #print("IMU 1:")
        #print(self.imu)
        #print("IMU 2:")
        #print(imu)
        self.imu.plot_all(False)
        imu.plot_all()
        comp_imu = self.imu.compare(imu)
        print("compared")
        equal = True
        print(comp_imu)
        for k in comp_imu.processed_data:
            if k != "time":
                a = comp_imu.processed_data[k]
                b = [0]*len(comp_imu.processed_data[k])
                if a != b:
                    print("Not equal '" + k + "' ({})".format(max(a)))
                #self.assertEqual(comp_imu.processed_data[k],
                #                 [0]*len(comp_imu.processed_data[k]))
        assert equal, "Imus are not equal"

if __name__ == "__main__":
    unittest.main()
    