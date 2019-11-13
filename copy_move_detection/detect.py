import os
import time
import copy_move_detection.image_object

def detect_dir(source_directory, output_directory, block_size=32):
    """
    Detects all images under a directory
    :param source_directory: directory that contains images to be detected
    :param output_directory: output directory
    :param block_size: the block size of the image pointer (eg. 32, 64, 128)
    The smaller the block size, the more accurate the result is, but takes more time, vice versa.
    :return: None
    """

    timestamp = time.strftime("%Y%m%d_%H%M%S")  # get current timestamp
    os.makedirs(output_directory + timestamp)    # create a folder named as the current timestamp

    if not os.path.exists(source_directory):
        print("Error: Source Directory did not exist.")
        return
    elif not os.path.exists(output_directory):
        print("Error: Output Directory did not exist.")
        return

    for fileName in os.listdir(source_directory):
        anImage = copy_move_detection.image_object.ImageObject(source_directory, fileName, block_size, output_directory + timestamp + '/')
        anImage.run()

    print("Done.")


def detect(source_directory, filename, output_directory, block_size=32):
    """
    Detects an image under a specific directory
    :param source_directory: directory that contains images to be detected
    :param filename: name of the image file to be detected
    :param output_directory: output directory
    :param block_size: the block size of the image pointer (eg. 32, 64, 128)
    The smaller the block size, the more accurate the result is, but takes more time, vice versa.
    :return: None
    """

    if not os.path.exists(source_directory):
        print("Error: Source Directory did not exist.")
        return
    elif not os.path.exists(source_directory + filename):
        print("Error: Image file did not exist.")
        return
    elif not os.path.exists(output_directory):
        print("Error: Output Directory did not exist.")
        return

    single_image = copy_move_detection.image_object.ImageObject(source_directory, filename, block_size, output_directory)
    image_result_path = single_image.run()

    print("Done.")
    return image_result_path
