__author__ = 'rahmat'
# 14 November 2016 5:08 PM

class Container(object):
    """
    Objek kontainer data untuk menyimpan hasil komputasi
    """

    def __init__(self):
        """
        Fungsi konstruktor untuk menginisialisasi list
        :return: none
        """
        self.container = []
        return

    def getLength(self):
        """
        Fungsi untuk mengambil panjang dari objek kontainer data
        :return: Panjang kontainer data
        """
        return self.container.__len__()

    def addBlock(self, blockData):
        """
        Fungsi untuk memasukkan sebuah blok data pada kontainer data
        :param blockData: list yang akan dimasukkan kedalam kontainer data
        :return: None
        """
        self.container.append(blockData)
        return

    def sortFeatures(self):
        """
        Fungsi sorting untuk mengurutkan kontainer data
        :return: None
        """
        self.container = sorted(self.container, key=lambda x:(x[1], x[2]))
        return

    """
    Fungsi debug
    """
    def printAllContainer(self):
        """
        Fungsi untuk mencetak isi kontainer data secara keseluruhan
        :return: None
        """
        for index in range(0, self.container.__len__()):
            print self.container[index]
        return

    def printContainer(self, i):
        """
        Fungsi untuk mencetak sebagian isi kontainer
        :param i: jumlah baris yang tercetak dihitung dari indeks ke-0
        :return: None
        """
        print "index container:", self.container.__len__()
        if i > self.container.__len__():
            self.printAllContainer()
        else:
            for index in range(0, i):
                print self.container[index]
        return