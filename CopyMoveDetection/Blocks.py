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
    def __init__(self, image, x, y, blockDimension):
        """
        Fungsi konstruktor untuk persiapan citra masukan
        :param image: Blok image yang akan diolah
        :param x: Koordinat ujung kiri blok citra pada sumbu x
        :param y: Koordinat ujung kiri blok citra pada sumbu y
        :return: None
        """
        self.image = image                                      # file image dari blok citra
        if self.image.mode != 'L':                              # jika image tidak grayscale, segera rubah ke RGB
            self.image = self.image.convert('RGB')

        self.pixels = self.image.load()                         # load piksel dari image tsb agar mudah di manipulasi
        self.coor = (x, y)                                      # koordinat kiri atas dari blok citra

        self.imageWidth, self.imageHeight = self.image.size   # variable properti blok gambar

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
        imageArray = np.array( self.image )
        pca = PCA(n_components=1)
        if imageArray.ndim == 2:
            pca.fit(imageArray)
            pca.transform(imageArray)
            return pca.explained_variance_ratio_
        else:
            r = imageArray[:,:,0]
            g = imageArray[:,:,1]
            b = imageArray[:,:,2]

            concat = np.concatenate((r, np.concatenate((g,b), axis=0)), axis=0)

            # reduced = pca.fit_transform(concat)
            # print "reduced:", reduced.shape()
            # print reduced

            pca.fit_transform(concat)
            principalComponents = pca.components_

            # print "components:", principalComponents.shape
            # print principalComponents

            # roundedResult = list(np.round(principalComponents, decimals=roundTo).flatten())
            roundedResult = [ round(elem, roundTo) for elem in list(principalComponents.flatten())]

            # print "pca result:", len(roundedResult)
            # print roundedResult

            return roundedResult

    def computeCharaFeatures(self, roundTo):
        """
        Menghitung 7 nilai fitur karakteristik dari setiap blok citra
        :return: None
        """

        # variable untuk Characteristics Features
        self.yImages = None                # file image untuk channel Y
        self.yPixels = None                # file piksel untuk channel Y

        self.charaFeature = [None] * 7    # list dengan 7 elemen kosong untuk menyimpan fitur karakteristik

        self.sumR = 0                      # variabel untuk menyimpan jumlah nilai piksel merah
        self.sumG = 0                      # variabel untuk menyimpan jumlah nilai piksel hijau
        self.sumB = 0                      # variabel untuk menyimpan jumlah nilai piksel biru

        self.c4_part1 = 0                   # variabel untuk menyimpan nilai part1 dan part2 setiap fitur karakteristik
        self.c4_part2 = 0
        self.c5_part1 = 0
        self.c5_part2 = 0
        self.c6_part1 = 0
        self.c6_part2 = 0
        self.c7_part1 = 0
        self.c7_part2 = 0

        """ Menghitung c1, c2, c3 sesuai jenis colorspace dari blok citra """
        if self.image.mode == 'L':
            self.charaFeature[0] = 0                              # jika citra hitam putih, maka c1-c3 diberi nilai 0
            self.charaFeature[1] = 0
            self.charaFeature[2] = 0
        elif self.image.mode == 'RGB':                                   # jika RGB, maka hitung c1-c3 dengan mencari rataan
            for y in range(0, self.imageHeight):                   # menghitung jumlah total nilai piksel
                for x in range(0, self.imageWidth):
                    tmpR, tmpG, tmpB = self.pixels[x,y]
                    self.sumR += tmpR
                    self.sumG += tmpG
                    self.sumB += tmpB

            sumR = self.sumR / (self.blockDimension*self.blockDimension)  # menghitung rata-rata dari tiap jenis warna
            sumG = self.sumG / (self.blockDimension*self.blockDimension)
            sumB = self.sumB / (self.blockDimension*self.blockDimension)

            self.charaFeature[0] = sumR                          # masukkan c1-c3
            self.charaFeature[1] = sumG
            self.charaFeature[2] = sumB

        """ Merubah colorspace blok menjadi Y Channel (YUV Channel, namun diambil Y nya saja) """
        if self.image.mode == 'RGB':
            self.yImages = self.image.convert('L')                 # membuat kanvas grayscale baru dari gambar lama
            self.yPixels = self.yImages.load()

            for y in range(0, self.imageHeight):
                for x in range(0, self.imageWidth):
                    tmpR, tmpG, tmpB = self.pixels[x,y]
                    self.yPixels[x,y] = int(0.299 * tmpR) + int(0.587 * tmpG) + int(0.114 * tmpB)

        """ Menghitung c4, c5, c6, c7 berdasarkan 4 blok berbeda arah"""
        if self.image.mode == 'L':
            for y in range(0, self.imageHeight):           # menghitung part 1 dan part 2 dari setiap fitur karakteristik
                for x in range(0, self.imageWidth):
                    # c4
                    if y <= self.imageHeight / 2:
                        self.c4_part1 += self.pixels[x,y]
                    else:
                        self.c4_part2 += self.pixels[x,y]
                    # c5
                    if x <= self.imageHeight / 2:
                        self.c5_part1 += self.pixels[x,y]
                    else:
                        self.c5_part2 += self.pixels[x,y]
                    # c6
                    if x-y >= 0:
                        self.c6_part1 += self.pixels[x,y]
                    else:
                        self.c6_part2 += self.pixels[x,y]
                    # c7
                    if x+y <= self.blockDimension:
                        self.c7_part1 += self.pixels[x,y]
                    else:
                        self.c7_part2 += self.pixels[x,y]

            self.charaFeature[3] = float(self.c4_part1) / float(self.c4_part1 + self.c4_part2)
            self.charaFeature[4] = float(self.c5_part1) / float(self.c5_part1 + self.c5_part2)
            self.charaFeature[5] = float(self.c6_part1) / float(self.c6_part1 + self.c6_part2)
            self.charaFeature[6] = float(self.c7_part1) / float(self.c7_part1 + self.c7_part2)

        elif self.image.mode == 'RGB':
            for y in range(0, self.imageHeight):           # menghitung part 1 dan part 2 dari setiap fitur karakteristik
                for x in range(0, self.imageWidth):
                    # c4
                    if y <= self.imageHeight / 2:
                        self.c4_part1 += self.yPixels[x,y]
                    else:
                        self.c4_part2 += self.yPixels[x,y]
                    # c5
                    if x <= self.imageHeight / 2:
                        self.c5_part1 += self.yPixels[x,y]
                    else:
                        self.c5_part2 += self.yPixels[x,y]
                    # c6
                    if x-y >= 1:
                        self.c6_part1 += self.yPixels[x,y]
                    else:
                        self.c6_part2 += self.yPixels[x,y]
                    # c7
                    if x+y <= self.blockDimension:
                        self.c7_part1 += self.yPixels[x,y]
                    else:
                        self.c7_part2 += self.yPixels[x,y]

            self.charaFeature[3] = float(self.c4_part1) / float(self.c4_part1 + self.c4_part2)
            self.charaFeature[4] = float(self.c5_part1) / float(self.c5_part1 + self.c5_part2)
            self.charaFeature[5] = float(self.c6_part1) / float(self.c6_part1 + self.c6_part2)
            self.charaFeature[6] = float(self.c7_part1) / float(self.c7_part1 + self.c7_part2)

        roundedResult = [round(elem, roundTo) for elem in self.charaFeature]
        return roundedResult
