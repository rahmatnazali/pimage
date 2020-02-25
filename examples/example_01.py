from copy_move_detection import detect

# detect original image with image block size of 16
# detect.detect('../assets/dataset_example.png', '../output/', block_size=16)

# detect original image with image block size of 32
# detect.detect('../assets/dataset_example.png', '../output/', block_size=32)

# detect attacked image with image block size of 16
# detect.detect('../assets/dataset_example_blur.png', '../output/', block_size=16)

# detect attacked image with image block size of 32
detect.detect('../assets/dataset_example_blur.png', '../output/', block_size=32)
