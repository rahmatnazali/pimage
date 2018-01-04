__author__ = 'rahmat'
# 14 November 2016 5:08 PM

class Container(object):
    """
    Object to contains the computation result
    """

    def __init__(self):
        """
        List initialization
        :return: none
        """
        self.container = []
        return

    def getLength(self):
        """
        To return the current container's length
        :return: length of the container
        """
        return self.container.__len__()

    def addBlock(self, newData):
        """
        Insert a data block to the container
        :param newData: data to be inserted into the block
        :return: None
        """
        self.container.append(newData)
        return

    def sortFeatures(self):
        """
        Sort all the container's data based on certain key
        :return: None
        """
        self.container = sorted(self.container, key=lambda x:(x[1], x[2]))
        return

    """
    Functions for debug purpose
    """
    def printAllContainer(self):
        """
        Prints all the elements inside the container
        :return: None
        """
        for index in range(0, self.container.__len__()):
            print self.container[index]
        return

    def printContainer(self, count):
        """
        Prints certain elements inside the container
        :param count: amount to be printed
        :return: None
        """
        print "Element's index:", self.container.__len__()
        if count > self.container.__len__():
            self.printAllContainer()
        else:
            for index in range(0, count):
                print self.container[index]
        return