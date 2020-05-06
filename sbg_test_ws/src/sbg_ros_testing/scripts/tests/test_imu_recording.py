# imu_data_reader.py
import unittest
import imu_recording
import numpy as np
from imu_recording.imu_recording import ImuRecording

class TestImuRecording(unittest.TestCase):
    def setUp(self):
        self.imu = ImuRecording(files_dir="tests/unittest_ascii")

    def test_read(self):
        self.imu.read("SBG_general_000.processed")
        self.imu.verify_data()

    def test_save(self):
        pass

    def test_add_data(self):
        self.imu.vel_x.append(1)
        self.assertRaisesWithMessage("Data field 'vel_x' and time has different lengths", 
                                     self.imu.add_data,
                                     *["vel_x", 1])
        self.imu.read("SBG_general_000.processed")

    def test_diff(self):
        imu = ImuRecording(files_dir="tests/unittest_ascii")
        imu.read("SBG_general_000.processed")
        self.imu.read("SBG_general_000.processed")
        comp_imu = self.imu.compare(imu)
        for k in comp_imu.processed_data:
            if k != "time":
                self.assertEqual(comp_imu.processed_data[k],
                                 [0]*len(comp_imu.processed_data[k]))

        self.imu.reset()
        imu.reset()
        self.imu.add_data("roll", 180, 0)
        imu.add_data("roll", -179, 0)
        self.imu.add_data("roll", 180, 1)
        imu.add_data("roll", 179, 1)
        self.imu.add_data("roll", -180, 2)
        imu.add_data("roll", -179, 2)
        self.imu.add_data("roll", -179, 3)
        imu.add_data("roll", -180, 3)

        comp_imu = self.imu.compare(imu)
        self.assertEqual(comp_imu.roll[0], -1)
        self.assertEqual(comp_imu.roll[1], 1)
        self.assertEqual(comp_imu.roll[2], -1)
        self.assertEqual(comp_imu.roll[3], 1)

    def assertRaisesWithMessage(self, msg, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            self.assertFail()
        except Exception as inst:
            self.assertEqual(inst.message, msg)

if __name__ == "__main__":
    unittest.main()