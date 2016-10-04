# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore
import numpy
import sys

class Gui(QtGui.QWidget):

    IMAGE_COLS_MAX=640
    IMAGE_ROWS_MAX=360
    updGUI=QtCore.pyqtSignal()

    def __init__(self, parent=None):

        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle("CamaraReal")
        #self.imgLabel=QtGui.QLabel(self)
        self.resize(6000,6000)
        #self.imgLabel.show()
        self.updGUI.connect(self.update)


        TestButton=QtGui.QPushButton("Evaluar")
        TestButton.move(20, 20)
        TestButton.resize(100,50)
        TestButton.setParent(self)
        TestButton.clicked.connect(self.effect)

        self.imgLabel=QtGui.QLabel(self)
        self.imgLabel.resize(self.IMAGE_COLS_MAX,self.IMAGE_ROWS_MAX)
        self.imgLabel.move(100,100)
        self.imgLabel.show()


    def setControl(self,control):
        self.control=control

    def update(self):
        print 'updgui'
        image = self.control.getImage()
        if image != None:
            img = QtGui.QImage(image.data, image.shape[1], image.shape[0], QtGui.QImage.Format_RGB888)
            size=QtCore.QSize(image.shape[1],image.shape[0])
            self.imgLabel.resize(size)
            self.resize(size)
            self.imgLabel.setPixmap(QtGui.QPixmap.fromImage(img))
            print 'printimg'

    def effect(self):
        self.control.effect()

