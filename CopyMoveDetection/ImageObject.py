__author__ = 'rahmat'
# 14 November 2016 5:28 PM

from PIL import Image
import scipy.misc
from math import pow
import numpy as np
import __builtin__
from tqdm import tqdm, trange
import time

import Container
import Blocks


class ImageObject(object):
    """
    Object to contains a single image, then detects a fraud in it
    """

    def __init__(self, imageDirectory, imageName, blockDimension, outputDirectory):
        """
        Constructor to initialize the algorithm's parameters
        :param imageDirectory: direktori file citra
        :param imageName: nama file citra
        :param blockDimension: ukuran blok dimensi (ex:32, 64, 128)
        :param outputDirectory: direktori untuk hasil deteksi
        :return: None
        """

        print imageName
        print "Step 1 of 4: Object and variable initialization",

        # image parameter
        self.imageOutputDirectory = outputDirectory
        self.imagePath = imageName
        self.imageData = Image.open(imageDirectory + imageName)
        self.imageWidth, self.imageHeight = self.imageData.size  # height = vertikal, width = horizontal

        if self.imageData.mode != 'L':  # L means grayscale
            self.isThisRGBImage = True
            self.imageData = self.imageData.convert('RGB')
            RGBImagePixels = self.imageData.load()
            self.imageGrayscale = self.imageData.convert(
                'L')  # creates a grayscale version of current image to be used later
            GrayscaleImagePixels = self.imageGrayscale.load()

            for yCoordinate in range(0, self.imageHeight):
                for xCoordinate in range(0, self.imageWidth):
                    redPixelValue, greenPixelValue, bluePixelValue = RGBImagePixels[xCoordinate, yCoordinate]
                    GrayscaleImagePixels[xCoordinate, yCoordinate] = int(0.299 * redPixelValue) + int(
                        0.587 * greenPixelValue) + int(0.114 * bluePixelValue)
        else:
            self.isThisRGBImage = False
            self.imageData = self.imageData.convert('L')

        # algorithm's parameters from the first paper
        self.N = self.imageWidth * self.imageHeight
        self.blockDimension = blockDimension
        self.b = self.blockDimension * self.blockDimension
        self.Nb = (self.imageWidth - self.blockDimension + 1) * (self.imageHeight - self.blockDimension + 1)
        self.Nn = 2  # amount of neighboring block to be evaluated
        self.Nf = 188  # minimum treshold of the offset's frequency
        self.Nd = 50  # minimum treshold of the offset's magnitude

        # algorithm's parameters from the second paper
        self.P = (1.80, 1.80, 1.80, 0.0125, 0.0125, 0.0125, 0.0125)
        self.t1 = 2.80
        self.t2 = 0.02

        print self.Nb, self.isThisRGBImage

        # container initialization to later contains several data
        self.featuresContainer = Container.Container()
        self.blockPairContainer = Container.Container()
        self.offsetDictionary = {}

    def run(self):
        """
        Run the created algorithm
        :return: None
        """

        # time logging (optional, for evaluation purpose)
        startTimestamp = time.time()
        self.compute()
        timestampAfterComputing = time.time()
        self.sort()
        timestampAfterSorting = time.time()
        self.analyze()
        timestampAfterAnalyze = time.time()
        imageResultPath = self.reconstruct()
        timestampAfterImageCreation = time.time()

        print "Computing time :", timestampAfterComputing - startTimestamp, "second"
        print "Sorting time   :", timestampAfterSorting - timestampAfterComputing, "second"
        print "Analyzing time :", timestampAfterAnalyze - timestampAfterSorting, "secon"
        print "Image creation :", timestampAfterImageCreation - timestampAfterAnalyze, "second"

        totalRunningTimeInSecond = timestampAfterImageCreation - startTimestamp
        totalMinute, totalSecond = divmod(totalRunningTimeInSecond, 60)
        totalHour, totalMinute = divmod(totalMinute, 60)
        print "Total time    : %d:%02d:%02d second" % (totalHour, totalMinute, totalSecond), '\n'
        return imageResultPath

    def compute(self):
        """
        To compute the characteristic features of image block
        :return: None
        """
        print "Step 2 of 4: Computing characteristic features"

        imageWidthOverlap = self.imageWidth - self.blockDimension
        imageHeightOverlap = self.imageHeight - self.blockDimension

        if self.isThisRGBImage:
            for i in tqdm(range(0, imageWidthOverlap + 1, 1)):
                for j in range(0, imageHeightOverlap + 1, 1):
                    imageBlockRGB = self.imageData.crop((i, j, i + self.blockDimension, j + self.blockDimension))
                    imageBlockGrayscale = self.imageGrayscale.crop(
                        (i, j, i + self.blockDimension, j + self.blockDimension))
                    imageBlock = Blocks.Blocks(imageBlockGrayscale, imageBlockRGB, i, j, self.blockDimension)
                    self.featuresContainer.addBlock(imageBlock.computeBlock())
        else:
            for i in range(imageWidthOverlap + 1):
                for j in range(imageHeightOverlap + 1):
                    imageBlockGrayscale = self.imageData.crop((i, j, i + self.blockDimension, j + self.blockDimension))
                    imageBlock = Blocks.Blocks(imageBlockGrayscale, None, i, j, self.blockDimension)
                    self.featuresContainer.addBlock(imageBlock.computeBlock())

    def sort(self):
        """
        To sort the container's elements
        :return: None
        """
        self.featuresContainer.sortFeatures()

    def analyze(self):
        """
        To analyze pairs of image blocks
        :return: None
        """
        print "Step 3 of 4:Pairing image blocks"
        z = 0
        time.sleep(0.1)
        featureContainerLength = self.featuresContainer.getLength()
        for i in tqdm(range(featureContainerLength)):
            for j in range(i + 1, featureContainerLength):
                result = self.isValid(i, j)
                if result[0]:
                    self.addDict(self.featuresContainer.container[i][0], self.featuresContainer.container[j][0],
                                 result[1])
                    z += 1
                else:
                    break

    def isValid(self, firstBlock, secondBlock):
        """
        To check the validity of the image block pairs and each of the characteristic features,
        also compute its offset, magnitude, and absolut value.
        :param firstBlock: the first block
        :param secondBlock: the second block
        :return: is the pair of i and j valid?
        """

        if abs(firstBlock - secondBlock) < self.Nn:
            iFeature = self.featuresContainer.container[firstBlock][1]
            jFeature = self.featuresContainer.container[secondBlock][1]

            # check the validity of characteristic features according to the second paper
            if abs(iFeature[0] - jFeature[0]) < self.P[0]:
                if abs(iFeature[1] - jFeature[1]) < self.P[1]:
                    if abs(iFeature[2] - jFeature[2]) < self.P[2]:
                        if abs(iFeature[3] - jFeature[3]) < self.P[3]:
                            if abs(iFeature[4] - jFeature[4]) < self.P[4]:
                                if abs(iFeature[5] - jFeature[5]) < self.P[5]:
                                    if abs(iFeature[6] - jFeature[6]) < self.P[6]:
                                        if abs(iFeature[0] - jFeature[0]) + abs(iFeature[1] - jFeature[1]) + abs(
                                                        iFeature[2] - jFeature[2]) < self.t1:
                                            if abs(iFeature[3] - jFeature[3]) + abs(iFeature[4] - jFeature[4]) + abs(
                                                            iFeature[5] - jFeature[5]) + abs(
                                                        iFeature[6] - jFeature[6]) < self.t2:

                                                # compute the pair's offset
                                                iCoordinate = self.featuresContainer.container[firstBlock][0]
                                                jCoordinate = self.featuresContainer.container[secondBlock][0]

                                                # Non Absolute Robust Detection Method
                                                offset = (
                                                    iCoordinate[0] - jCoordinate[0], iCoordinate[1] - jCoordinate[1])

                                                # compute the pair's magnitude
                                                magnitude = np.sqrt(pow(offset[0], 2) + pow(offset[1], 2))
                                                if magnitude >= self.Nd:
                                                    return 1, offset
        return 0,

    def addDict(self, firstCoordinate, secondCoordinate, pairOffset):
        """
        Add a pair of coordinate and its offset to the dictionary
        """
        if self.offsetDictionary.has_key(pairOffset):
            self.offsetDictionary[pairOffset].append(firstCoordinate)
            self.offsetDictionary[pairOffset].append(secondCoordinate)
        else:
            self.offsetDictionary[pairOffset] = [firstCoordinate, secondCoordinate]

    def reconstruct(self):
        """
        Reconstruct the image according to the fraud detectionr esult
        """
        print "Step 4 of 4: Image reconstruction"

        # create an array as the canvas of the final image
        groundtruthImage = np.zeros((self.imageHeight, self.imageWidth))
        linedImage = np.array(self.imageData.convert('RGB'))

        for key in sorted(self.offsetDictionary, key=lambda key: __builtin__.len(self.offsetDictionary[key]),
                          reverse=True):
            if self.offsetDictionary[key].__len__() < self.Nf * 2:
                break
            print key, self.offsetDictionary[key].__len__()
            for i in range(self.offsetDictionary[key].__len__()):
                # The original image (grayscale)
                for j in range(self.offsetDictionary[key][i][1],
                               self.offsetDictionary[key][i][1] + self.blockDimension):
                    for k in range(self.offsetDictionary[key][i][0],
                                   self.offsetDictionary[key][i][0] + self.blockDimension):
                        groundtruthImage[j][k] = 255

        # creating a line edge from the original image (for the visual purpose)
        for xCoordinate in range(2, self.imageHeight - 2):
            for yCordinate in range(2, self.imageWidth - 2):
                if groundtruthImage[xCoordinate, yCordinate] == 255 and \
                        (groundtruthImage[xCoordinate + 1, yCordinate] == 0 or groundtruthImage[
                                xCoordinate - 1, yCordinate] == 0 or
                                 groundtruthImage[xCoordinate, yCordinate + 1] == 0 or groundtruthImage[
                            xCoordinate, yCordinate - 1] == 0 or
                                 groundtruthImage[xCoordinate - 1, yCordinate + 1] == 0 or groundtruthImage[
                                xCoordinate + 1, yCordinate + 1] == 0 or
                                 groundtruthImage[xCoordinate - 1, yCordinate - 1] == 0 or groundtruthImage[
                                xCoordinate + 1, yCordinate - 1] == 0):

                    # creating the edge line, respectively left-upper, right-upper, left-down, right-down
                    if groundtruthImage[xCoordinate - 1, yCordinate] == 0 and \
                                    groundtruthImage[xCoordinate, yCordinate - 1] == 0 and \
                                    groundtruthImage[xCoordinate - 1, yCordinate - 1] == 0:
                        linedImage[xCoordinate - 2:xCoordinate, yCordinate, 1] = 255
                        linedImage[xCoordinate, yCordinate - 2:yCordinate, 1] = 255
                        linedImage[xCoordinate - 2:xCoordinate, yCordinate - 2:yCordinate, 1] = 255
                    elif groundtruthImage[xCoordinate + 1, yCordinate] == 0 and \
                                    groundtruthImage[xCoordinate, yCordinate - 1] == 0 and \
                                    groundtruthImage[xCoordinate + 1, yCordinate - 1] == 0:
                        linedImage[xCoordinate + 1:xCoordinate + 3, yCordinate, 1] = 255
                        linedImage[xCoordinate, yCordinate - 2:yCordinate, 1] = 255
                        linedImage[xCoordinate + 1:xCoordinate + 3, yCordinate - 2:yCordinate, 1] = 255
                    elif groundtruthImage[xCoordinate - 1, yCordinate] == 0 and \
                                    groundtruthImage[xCoordinate, yCordinate + 1] == 0 and \
                                    groundtruthImage[xCoordinate - 1, yCordinate + 1] == 0:
                        linedImage[xCoordinate - 2:xCoordinate, yCordinate, 1] = 255
                        linedImage[xCoordinate, yCordinate + 1:yCordinate + 3, 1] = 255
                        linedImage[xCoordinate - 2:xCoordinate, yCordinate + 1:yCordinate + 3, 1] = 255
                    elif groundtruthImage[xCoordinate + 1, yCordinate] == 0 and \
                                    groundtruthImage[xCoordinate, yCordinate + 1] == 0 and \
                                    groundtruthImage[xCoordinate + 1, yCordinate + 1] == 0:
                        linedImage[xCoordinate + 1:xCoordinate + 3, yCordinate, 1] = 255
                        linedImage[xCoordinate, yCordinate + 1:yCordinate + 3, 1] = 255
                        linedImage[xCoordinate + 1:xCoordinate + 3, yCordinate + 1:yCordinate + 3, 1] = 255

                    # creating the straigh line, respectively upper, down, left, right line
                    elif groundtruthImage[xCoordinate, yCordinate + 1] == 0:
                        linedImage[xCoordinate, yCordinate + 1:yCordinate + 3, 1] = 255
                    elif groundtruthImage[xCoordinate, yCordinate - 1] == 0:
                        linedImage[xCoordinate, yCordinate - 2:yCordinate, 1] = 255
                    elif groundtruthImage[xCoordinate - 1, yCordinate] == 0:
                        linedImage[xCoordinate - 2:xCoordinate, yCordinate, 1] = 255
                    elif groundtruthImage[xCoordinate + 1, yCordinate] == 0:
                        linedImage[xCoordinate + 1:xCoordinate + 3, yCordinate, 1] = 255

        timeStamp = time.strftime("%Y%m%d_%H%M%S")
        scipy.misc.imsave(self.imageOutputDirectory + timeStamp + "_" + self.imagePath, groundtruthImage)
        scipy.misc.imsave(self.imageOutputDirectory + timeStamp + "_lined_" + self.imagePath, linedImage)

        return self.imageOutputDirectory + timeStamp + "_lined_" + self.imagePath
