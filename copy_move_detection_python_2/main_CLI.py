__author__ = 'rahmat'
# 22 November 2016 5:06 AM

import copy_move_detection_python_2

"""
Main Code
"""

# to detect all images under a directory, use detect_dir
# copy_move_detection_python_2.detect_dir('../testcase_image/', '../testcase_result/', 32)

# to detect single image, use detect
# copy_move_detection_python_2.detect('../testcase_image/', '01_barrier_copy.png', '../testcase_result/', blockSize=32)

# example
copy_move_detection_python_2.detect('../testcase_image/', '06_horses_copy.png', '../testcase_result/', blockSize=32)
