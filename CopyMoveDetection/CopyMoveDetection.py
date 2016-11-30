__author__ = 'rahmat'
# 10 September 2016 6:41 PM

# import library
import os
import time

# import script
import ImageObject


def detect_dir(sourceDir, destinationDir, blockSize=32):
    """
    Fungsi untuk melakukan deteksi copy-move pada semua citra yang berada di sebuah direktori
    :param sourceDir: direktori masukan
    :param destinationDir: direktori keluaran
    :param blockSize: ukuran block citra (misal 32, 64, 128)
    :return: None
    """

    timestr = time.strftime("%Y%m%d_%H%M%S")
    os.makedirs(destinationDir+timestr)

    if not os.path.exists(sourceDir):
        print "Error: Direktori masukan salah."
        return
    elif not os.path.exists(destinationDir):
        print "Error: Direktori keluaran salah."
        return

    for filename in os.listdir(sourceDir):
        singleImage = ImageObject.ImageObject(sourceDir, filename, blockSize, destinationDir+timestr+'/')
        singleImage.run()

    print "Selesai."

def detect(sourceDir, fileName, destinationDir, blockSize):
    """
    Fungsi untuk melakukan deteksi copy-move pada satu citra
    :param sourceDir: direktori citra
    :param filename: nama citra
    :param destinationDir: direktori hasil
    :param blockSize: ukuran blok citra (misal 32, 64, 128)
    :return: None
    """
    if not os.path.exists(sourceDir):
        print "Error: Direktori masukan salah."
        return
    elif not os.path.exists(sourceDir+fileName):
        print "Error: Nama file salah."
        return
    elif not os.path.exists(destinationDir):
        print "Error: Direktori keluaran salah."
        return

    singleImage = ImageObject.ImageObject(sourceDir, fileName, blockSize, destinationDir+'/')
    singleImage.run()
    print "Selesai."
