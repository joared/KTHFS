#!/usr/bin/env python
import glob
import unittest
import sys, os
from tests.test_rosbagging import *
from tests.test_imu_recording import *



if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(__file__)) # not necessary if run in root
    unittest.main()
