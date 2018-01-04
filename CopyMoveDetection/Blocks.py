__author__ = 'rahmat'
# 14 November 2016 5:13 PM

import numpy as np
from sklearn.decomposition import PCA

class Blocks(object):
    """
    Contains a single image block and handle the calculation of characteristic features
    """

    def __init__(self, grayscaleImageBlock, rgbImageBlock, x, y, blockDimension):
        """
        Initializing the input image
        :param grayscaleImageBlock: grayscale image block
        :param rgbImageBlock: rgb image block
        :param x: x coordinate (upper-left)
        :param y: y coordinate (upper-left)
        :return: None
        """
        self.imageGrayscale = grayscaleImageBlock  # block of grayscale image
        self.imageGrayscalePixels = self.imageGrayscale.load()

        if rgbImageBlock is not None:
            self.imageRGB = rgbImageBlock
            self.imageRGBPixels = self.imageRGB.load()
            self.isImageRGB = True
        else:
            self.isImageRGB = False

        self.coor = (x, y)
        self.blockDimension = blockDimension

    def computeBlock(self):
        """
        Create a representation of the image block
        :return: image block representation data
        """
        blockDataList = []
        blockDataList.append(self.coor)
        blockDataList.append(self.computeCharaFeatures(4))
        blockDataList.append(self.computePCA(6))
        return blockDataList

    def computePCA(self, precision):
        """
        Compute Principal Component Analysis from the image block
        :param precision: characteristic features precision
        :return: Principal Component from the image block
        """
        PCAModule = PCA(n_components=1)
        if self.isImageRGB:
            imageArray = np.array(self.imageRGB)
            r = imageArray[:, :, 0]
            g = imageArray[:, :, 1]
            b = imageArray[:, :, 2]

            concatenatedArray = np.concatenate((r, np.concatenate((g, b), axis=0)), axis=0)
            PCAModule.fit_transform(concatenatedArray)
            principalComponents = PCAModule.components_
            preciseResult = [round(element, precision) for element in list(principalComponents.flatten())]
            return preciseResult
        else:
            imageArray = np.array(self.imageGrayscale)
            PCAModule.fit_transform(imageArray)
            principalComponents = PCAModule.components_
            preciseResult = [round(element, precision) for element in list(principalComponents.flatten())]
            return preciseResult

    def computeCharaFeatures(self, precision):
        """
        Compute 7 characteristic features from every image blocks
        :param precision: feature characteristic precision
        :return: None
        """

        characteristicFeaturesList = []

        # variable to compute characteristic features
        c4_part1 = 0
        c4_part2 = 0
        c5_part1 = 0
        c5_part2 = 0
        c6_part1 = 0
        c6_part2 = 0
        c7_part1 = 0
        c7_part2 = 0

        """ Compute c1, c2, c3 according to the image block's colorspace """

        if self.isImageRGB:
            sumOfRedPixelValue = 0
            sumOfGreenPixelValue = 0
            sumOfBluePixelValue = 0
            for yCoordinate in range(0, self.blockDimension):  # compute sum of the pixel value
                for xCoordinate in range(0, self.blockDimension):
                    tmpR, tmpG, tmpB = self.imageRGBPixels[xCoordinate, yCoordinate]
                    sumOfRedPixelValue += tmpR
                    sumOfGreenPixelValue += tmpG
                    sumOfBluePixelValue += tmpB

            sumOfPixels = self.blockDimension * self.blockDimension
            sumOfRedPixelValue = sumOfRedPixelValue / (sumOfPixels)  # mean from each of the colorspaces
            sumOfGreenPixelValue = sumOfGreenPixelValue / (sumOfPixels)
            sumOfBluePixelValue = sumOfBluePixelValue / (sumOfPixels)

            characteristicFeaturesList.append(sumOfRedPixelValue)
            characteristicFeaturesList.append(sumOfGreenPixelValue)
            characteristicFeaturesList.append(sumOfBluePixelValue)

        else:
            characteristicFeaturesList.append(0)
            characteristicFeaturesList.append(0)
            characteristicFeaturesList.append(0)

        """ Compute  c4, c5, c6 and c7 according to the pattern rule on the second paper"""
        for yCoordinate in range(0, self.blockDimension):  # compute the part 1 and part 2 of each feature characteristic
            for xCoordinate in range(0, self.blockDimension):
                # compute c4
                if yCoordinate <= self.blockDimension / 2:
                    c4_part1 += self.imageGrayscalePixels[xCoordinate, yCoordinate]
                else:
                    c4_part2 += self.imageGrayscalePixels[xCoordinate, yCoordinate]
                # compute c5
                if xCoordinate <= self.blockDimension / 2:
                    c5_part1 += self.imageGrayscalePixels[xCoordinate, yCoordinate]
                else:
                    c5_part2 += self.imageGrayscalePixels[xCoordinate, yCoordinate]
                # compute c6
                if xCoordinate - yCoordinate >= 0:
                    c6_part1 += self.imageGrayscalePixels[xCoordinate, yCoordinate]
                else:
                    c6_part2 += self.imageGrayscalePixels[xCoordinate, yCoordinate]
                # compute c7
                if xCoordinate + yCoordinate <= self.blockDimension:
                    c7_part1 += self.imageGrayscalePixels[xCoordinate, yCoordinate]
                else:
                    c7_part2 += self.imageGrayscalePixels[xCoordinate, yCoordinate]

        characteristicFeaturesList.append(float(c4_part1) / float(c4_part1 + c4_part2))
        characteristicFeaturesList.append(float(c5_part1) / float(c5_part1 + c5_part2))
        characteristicFeaturesList.append(float(c6_part1) / float(c6_part1 + c6_part2))
        characteristicFeaturesList.append(float(c7_part1) / float(c7_part1 + c7_part2))

        preciseResult = [round(element, precision) for element in characteristicFeaturesList]
        return preciseResult
