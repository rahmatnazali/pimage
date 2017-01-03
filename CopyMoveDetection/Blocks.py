__author__ = 'rahmat'
# 14 November 2016 5:13 PM

"""
Import library
"""
import numpy as np
from sklearn.decomposition import PCA

class Blocks(object):
    """
    Objek blok untuk menampung sebuah blok citra dan mencari fitur karakteristiknya
    """
    def __init__(self, imageGrayscale, imageRGB, x, y, blockDimension):
        """
        Fungsi konstruktor untuk persiapan citra masukan
        :param imageGrayscale: Blok imageGrayscale yang akan diolah
        :param x: Koordinat ujung kiri blok citra pada sumbu x
        :param y: Koordinat ujung kiri blok citra pada sumbu y
        :return: None
        """
        self.imageGrayscale = imageGrayscale                                      # file imageGrayscale dari blok citra
        self.imageGrayscalePixels = self.imageGrayscale.load()

        if imageRGB is not None:
            self.imageRGB = imageRGB
            self.imageRGBPixels = self.imageRGB.load()
            self.isRGB = True
        else:
            self.isRGB = False

        self.coor = (x, y)
        self.blockDimension = blockDimension

    def computeBlock(self):
        """
        Fungsi untuk membentuk representasi data dari blok citra
        :return: Sebuah data yang merepresentasikan blok citra
        """
        blockData = []
        blockData.append(self.coor)
        blockData.append(self.computeCharaFeatures(4))
        blockData.append(self.computePCA(6))
        return blockData

    def computePCA(self, roundTo):
        """
        Fungsi untuk menghitung principal component dari blok citra
        :param roundTo: tingkat ketelitian dalam pembulatan fitur karakteristik
        :return: Principal component dari blok citra
        """
        pca = PCA(n_components=1)
        if self.isRGB:
            imageArray = np.array(self.imageRGB)
            r = imageArray[:,:,0]
            g = imageArray[:,:,1]
            b = imageArray[:,:,2]

            concat = np.concatenate((r, np.concatenate((g,b), axis=0)), axis=0)
            pca.fit_transform(concat)
            principalComponents = pca.components_
            roundedResult = [ round(elem, roundTo) for elem in list(principalComponents.flatten())]
            return roundedResult
        else:
            imageArray = np.array( self.imageGrayscale)
            pca.fit_transform(imageArray)
            principalComponents = pca.components_
            roundedResult = [ round(elem, roundTo) for elem in list(principalComponents.flatten())]
            return roundedResult

    def computeCharaFeatures(self, roundTo):
        """
        Menghitung 7 nilai fitur karakteristik dari setiap blok citra
        :return: None
        """

        charaFeature = []

        c4_part1 = 0                   # variabel untuk menyimpan nilai part1 dan part2 setiap fitur karakteristik
        c4_part2 = 0
        c5_part1 = 0
        c5_part2 = 0
        c6_part1 = 0
        c6_part2 = 0
        c7_part1 = 0
        c7_part2 = 0

        """ Menghitung c1, c2, c3 sesuai jenis colorspace dari blok citra """

        if self.isRGB:
            sumR = 0
            sumG = 0
            sumB = 0
            for y in range(0, self.blockDimension):                   # menghitung jumlah total nilai piksel
                for x in range(0, self.blockDimension):
                    tmpR, tmpG, tmpB = self.imageRGBPixels[x,y]
                    sumR += tmpR
                    sumG += tmpG
                    sumB += tmpB

            totalPixels = self.blockDimension * self.blockDimension
            sumR = sumR / (totalPixels)  # menghitung rata-rata dari tiap jenis warna
            sumG = sumG / (totalPixels)
            sumB = sumB / (totalPixels)

            charaFeature.append(sumR)
            charaFeature.append(sumG)
            charaFeature.append(sumB)

        else:
            charaFeature.append(0)
            charaFeature.append(0)
            charaFeature.append(0)

        """ Menghitung c4, c5, c6, c7 berdasarkan 4 blok berbeda arah"""
        for y in range(0, self.blockDimension):           # menghitung part 1 dan part 2 dari setiap fitur karakteristik
            for x in range(0, self.blockDimension):
                # c4
                if y <= self.blockDimension / 2:
                    c4_part1 += self.imageGrayscalePixels[x,y]
                else:
                    c4_part2 += self.imageGrayscalePixels[x,y]
                # c5
                if x <= self.blockDimension / 2:
                    c5_part1 += self.imageGrayscalePixels[x,y]
                else:
                    c5_part2 += self.imageGrayscalePixels[x,y]
                # c6
                if x-y >= 0:
                    c6_part1 += self.imageGrayscalePixels[x,y]
                else:
                    c6_part2 += self.imageGrayscalePixels[x,y]
                # c7
                if x+y <= self.blockDimension:
                    c7_part1 += self.imageGrayscalePixels[x,y]
                else:
                    c7_part2 += self.imageGrayscalePixels[x,y]

        charaFeature.append(float(c4_part1) / float(c4_part1 + c4_part2))
        charaFeature.append(float(c5_part1) / float(c5_part1 + c5_part2))
        charaFeature.append(float(c6_part1) / float(c6_part1 + c6_part2))
        charaFeature.append(float(c7_part1) / float(c7_part1 + c7_part2))

        roundedResult = [round(elem, roundTo) for elem in charaFeature]
        return roundedResult

