__author__ = 'rahmat'
# 22 November 2016 5:06 AM

import CopyMoveDetection

"""
Main Code
"""

# to detect all images under a directory, use detect_dir
# CopyMoveDetection.detect_dir('../testcase_image/', '../testcase_result/', 32)

# to detect single image, use detect
# CopyMoveDetection.detect('../testcase_image/', '01_barrier_copy.png', '../testcase_result/', blockSize=32)

# example
CopyMoveDetection.detect('../testcase_image/', '06_horses_copy.png', '../testcase_result/', blockSize=32)
