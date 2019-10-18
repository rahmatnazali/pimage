__author__ = 'rahmat'
# 08 December 2016 10:01 AM

"""
Important: This script is no longer maintained.
"""


from Tkinter import Frame, Label, Tk, BOTH, Text, Menu, INSERT, END
from ttk import Frame, Button, Style
import tkFileDialog
import tkMessageBox as mbox
from PIL import Image, ImageTk

import copy_move_detection_python_2

class aFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.imageName = ""
        self.initUI()

    def initUI(self):
        self.parent.title("Image Copy-Move Detection")
        self.style = Style().configure("TFrame", background="#333")
        # self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Open File", command=self.onFilePicker)
        quitButton.place(x=10, y=10)

        printButton = Button(self, text="Detect", command=self.onDetect)
        printButton.place(x=10, y=40)

        self.textBoxFile = Text(self, state='disabled', width=80, height = 1)
        self.textBoxFile.place(x=90, y=10)

        self.textBoxLog = Text(self, state='disabled', width=40, height=3)
        self.textBoxLog.place(x=90, y=40)

        # absolute image widget
        imageLeft = Image.open("resource/empty.png")
        imageLeftLabel = ImageTk.PhotoImage(imageLeft)
        self.labelLeft = Label(self, image=imageLeftLabel)
        self.labelLeft.image = imageLeftLabel
        self.labelLeft.place(x=5, y=100)

        imageRight = Image.open("resource/empty.png")
        imageRightLabel = ImageTk.PhotoImage(imageRight)
        self.labelRight = Label(self, image=imageRightLabel)
        self.labelRight.image = imageRightLabel
        self.labelRight.place(x=525, y=100)

        self.centerWindow()

    def centerWindow(self):
            w = 1045
            h = 620

            sw = self.parent.winfo_screenwidth()
            sh = self.parent.winfo_screenheight()

            x = (sw - w)/2
            y = (sh - h)/2
            self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def onFilePicker(self):

        ftypes = [('PNG Files', '*.png'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, initialdir='../testcase_image/', filetypes = ftypes)
        choosedFile = dlg.show()

        if choosedFile != '':
            print choosedFile
            self.imageName = str(choosedFile).split("/")[-1]
            self.imagePath = str(choosedFile).replace(self.imageName, '')

            self.textBoxFile.config(state='normal')
            self.textBoxFile.delete('1.0', END)
            self.textBoxFile.insert(END, choosedFile)
            self.textBoxFile.config(state='disabled')

            newImageLeft = Image.open(choosedFile)
            imageLeftLabel = ImageTk.PhotoImage(newImageLeft)
            self.labelLeft = Label(self, image=imageLeftLabel)
            self.labelLeft.image = imageLeftLabel
            self.labelLeft.place(x=5, y=100)

            imageRight = Image.open("resource/empty.png")
            imageRightLabel = ImageTk.PhotoImage(imageRight)
            self.labelRight = Label(self, image=imageRightLabel)
            self.labelRight.image = imageRightLabel
            self.labelRight.place(x=525, y=100)

        pass

    def onDetect(self):
        if self.imageName == "":
            mbox.showerror("Error", 'No image selected\nSelect an image by clicking "Open File"')
        else:

            self.textBoxLog.config(state='normal')
            self.textBoxLog.insert(END, "Detecting: "+self.imageName+"\n")
            self.textBoxLog.see(END)
            self.textBoxLog.config(state='disabled')

            imageResultPath = copy_move_detection_python_2.detect(self.imagePath, self.imageName, '../testcase_result/', blockSize=32)
            newImageRight = Image.open(imageResultPath)
            imageRightLabel = ImageTk.PhotoImage(newImageRight)
            self.labelRight = Label(self, image=imageRightLabel)
            self.labelRight.image = imageRightLabel
            self.labelRight.place(x=525, y=100)

            self.textBoxLog.config(state='normal')
            self.textBoxLog.insert(END, "Done.")
            self.textBoxLog.see(END)
            self.textBoxLog.config(state='disabled')

if __name__ == '__main__':
    root = Tk()
    app = aFrame(root)
    root.mainloop()
