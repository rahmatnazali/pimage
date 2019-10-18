__author__ = 'rahmat'
# 10 September 2016 6:41 PM

import os
import time
import ImageObject

def detect_dir(sourceDirectory, outputDirectory, blockSize=32):
    """
    Detects all images under a directory
    :param sourceDirectory: directory that contains images to be detected
    :param outputDirectory: output directory
    :param blockSize: the block size of the image pointer (eg. 32, 64, 128)
    The smaller the block size, the more accurate the result is, but takes more time, vice versa.
    :return: None
    """

    timeStamp = time.strftime("%Y%m%d_%H%M%S")  # get current timestamp
    os.makedirs(outputDirectory + timeStamp)    # create a folder named as the current timestamp

    if not os.path.exists(sourceDirectory):
        print "Error: Source Directory did not exist."
        return
    elif not os.path.exists(outputDirectory):
        print "Error: Output Directory did not exist."
        return

    for fileName in os.listdir(sourceDirectory):
        anImage = ImageObject.ImageObject(sourceDirectory, fileName, blockSize, outputDirectory + timeStamp + '/')
        anImage.run()

    print "Done."


def detect(sourceDirectory, fileName, outputDirectory, blockSize=32):
    """
    Detects an image under a specific directory
    :param sourceDirectory: directory that contains images to be detected
    :param fileName: name of the image file to be detected
    :param outputDirectory: output directory
    :param blockSize: the block size of the image pointer (eg. 32, 64, 128)
    The smaller the block size, the more accurate the result is, but takes more time, vice versa.
    :return: None
    """

    if not os.path.exists(sourceDirectory):
        print "Error: Source Directory did not exist."
        return
    elif not os.path.exists(sourceDirectory + fileName):
        print "Error: Image file did not exist."
        return
    elif not os.path.exists(outputDirectory):
        print "Error: Output Directory did not exist."
        return

    singleImage = ImageObject.ImageObject(sourceDirectory, fileName, blockSize, outputDirectory)
    imageResultPath = singleImage.run()

    print "Done."
    return imageResultPath
