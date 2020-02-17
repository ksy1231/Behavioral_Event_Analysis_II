# -*- coding: utf-8 -*-
# Icon made by Freepik from www.flaticon.com

import sys
from functools import partial

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from neuralynx import *
from program import *

if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)


class rangeDialog(QDialog):
    def __init__(self):
        super(rangeDialog, self).__init__()
        self.setupUI()

        self.baseFrom = None
        self.baseTo = None
        self.stimFrom = None
        self.stimTo = None
        self.stimSplit = None
        self.postFrom = None
        self.postTo = None
        self.robotFrom = None
        self.robotTo = None

    def setupUI(self):
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QIcon(scriptDir + os.path.sep + 'rat.ico'))

        self.resize(480, 360)

        self.gridLayoutWidget = QWidget(self)
        self.gridLayoutWidget.setGeometry(QRect(20, 20, 440, 260))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stimGroupBox = QGroupBox(self.gridLayoutWidget)

        font = QFont()
        font.setPointSize(18)
        self.stimGroupBox.setFont(font)
        self.stimGridLayoutWidget = QWidget(self.stimGroupBox)
        self.stimGridLayoutWidget.setGeometry(QRect(0, 30, 180, 80))
        self.stimGridLayout = QGridLayout(self.stimGridLayoutWidget)
        self.stimGridLayout.setContentsMargins(0, 0, 0, 0)
        self.stimFromLabel = QLabel(self.stimGridLayoutWidget)

        font = QFont()
        font.setPointSize(15)
        self.stimFromLabel.setFont(font)
        self.stimFromLabel.setAlignment(Qt.AlignCenter)
        self.stimGridLayout.addWidget(self.stimFromLabel, 0, 0, 1, 1)
        self.stimSplitLabel = QLabel(self.stimGridLayoutWidget)

        font = QFont()
        font.setPointSize(15)
        self.stimSplitLabel.setFont(font)
        self.stimSplitLabel.setAlignment(Qt.AlignCenter)
        self.stimGridLayout.addWidget(self.stimSplitLabel, 2, 0, 1, 1)
        self.stimToLabel = QLabel(self.stimGridLayoutWidget)

        font = QFont()
        font.setPointSize(15)
        self.stimToLabel.setFont(font)
        self.stimToLabel.setAlignment(Qt.AlignCenter)
        self.stimGridLayout.addWidget(self.stimToLabel, 1, 0, 1, 1)
        self.stimToSpinBox = QSpinBox(self.stimGridLayoutWidget)
        self.stimToSpinBox.setMaximum(100000)
        self.stimGridLayout.addWidget(self.stimToSpinBox, 1, 1, 1, 1)
        self.stimFromSpinBox = QSpinBox(self.stimGridLayoutWidget)
        self.stimFromSpinBox.setMaximum(100000)
        self.stimGridLayout.addWidget(self.stimFromSpinBox, 0, 1, 1, 1)
        self.stimSplitSpinBox = QSpinBox(self.stimGridLayoutWidget)
        self.stimGridLayout.addWidget(self.stimSplitSpinBox, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.stimGroupBox, 0, 1, 1, 1)
        self.BaseGroupBox = QGroupBox(self.gridLayoutWidget)

        font = QFont()
        font.setPointSize(18)
        self.BaseGroupBox.setFont(font)
        self.baseGridLayoutWidget = QWidget(self.BaseGroupBox)
        self.baseGridLayoutWidget.setGeometry(QRect(0, 30, 180, 80))
        self.baseGridLayout = QGridLayout(self.baseGridLayoutWidget)
        self.baseGridLayout.setContentsMargins(0, 0, 0, 0)
        self.baseToLabel = QLabel(self.baseGridLayoutWidget)

        font = QFont()
        font.setPointSize(15)
        self.baseToLabel.setFont(font)
        self.baseToLabel.setAlignment(Qt.AlignCenter)
        self.baseGridLayout.addWidget(self.baseToLabel, 1, 0, 1, 1)
        self.baseFromLabel = QLabel(self.baseGridLayoutWidget)

        font = QFont()
        font.setPointSize(15)
        self.baseFromLabel.setFont(font)
        self.baseFromLabel.setAlignment(Qt.AlignCenter)
        self.baseGridLayout.addWidget(self.baseFromLabel, 0, 0, 1, 1)
        self.baseFromSpinBox = QSpinBox(self.baseGridLayoutWidget)
        self.baseFromSpinBox.setMaximum(100000)
        self.baseGridLayout.addWidget(self.baseFromSpinBox, 0, 1, 1, 1)
        self.baseToSpinBox = QSpinBox(self.baseGridLayoutWidget)
        self.baseToSpinBox.setMaximum(100000)
        self.baseGridLayout.addWidget(self.baseToSpinBox, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.BaseGroupBox, 0, 0, 1, 1)
        self.postGroupBox = QGroupBox(self.gridLayoutWidget)

        font = QFont()
        font.setPointSize(18)
        self.postGroupBox.setFont(font)
        self.postGridLayoutWidget = QWidget(self.postGroupBox)
        self.postGridLayoutWidget.setGeometry(QRect(0, 30, 180, 80))
        self.postGridLayout = QGridLayout(self.postGridLayoutWidget)
        self.postGridLayout.setContentsMargins(0, 0, 0, 0)
        self.postFromLabel = QLabel(self.postGridLayoutWidget)

        font = QFont()
        font.setPointSize(15)
        self.postFromLabel.setFont(font)
        self.postFromLabel.setAlignment(Qt.AlignCenter)
        self.postGridLayout.addWidget(self.postFromLabel, 0, 0, 1, 1)
        self.postToLabel = QLabel(self.postGridLayoutWidget)

        font = QFont()
        font.setPointSize(15)
        self.postToLabel.setFont(font)
        self.postToLabel.setAlignment(Qt.AlignCenter)
        self.postGridLayout.addWidget(self.postToLabel, 1, 0, 1, 1)
        self.postFromSpinBox = QSpinBox(self.postGridLayoutWidget)
        self.postFromSpinBox.setMaximum(100000)
        self.postGridLayout.addWidget(self.postFromSpinBox, 0, 1, 1, 1)
        self.postToSpinBox = QSpinBox(self.postGridLayoutWidget)
        self.postToSpinBox.setMaximum(100000)
        self.postGridLayout.addWidget(self.postToSpinBox, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.postGroupBox, 1, 0, 1, 1)
        self.robotGroupBox = QGroupBox(self.gridLayoutWidget)

        font = QFont()
        font.setPointSize(18)
        self.robotGroupBox.setFont(font)
        self.robotGridLayoutWidget = QWidget(self.robotGroupBox)
        self.robotGridLayoutWidget.setGeometry(QRect(0, 30, 180, 80))
        self.robotGridLayout = QGridLayout(self.robotGridLayoutWidget)
        self.robotGridLayout.setContentsMargins(0, 0, 0, 0)
        self.robotFromLabel = QLabel(self.robotGridLayoutWidget)

        font = QFont()
        font.setPointSize(15)
        self.robotFromLabel.setFont(font)
        self.robotFromLabel.setAlignment(Qt.AlignCenter)
        self.robotGridLayout.addWidget(self.robotFromLabel, 0, 0, 1, 1)
        self.robotToLabel = QLabel(self.robotGridLayoutWidget)

        font = QFont()
        font.setPointSize(15)
        self.robotToLabel.setFont(font)
        self.robotToLabel.setAlignment(Qt.AlignCenter)
        self.robotGridLayout.addWidget(self.robotToLabel, 1, 0, 1, 1)

        self.robotFromSpinBox = QSpinBox(self.robotGridLayoutWidget)
        self.robotFromSpinBox.setMaximum(100000)
        self.robotGridLayout.addWidget(self.robotFromSpinBox, 0, 1, 1, 1)
        self.robotToSpinBox = QSpinBox(self.robotGridLayoutWidget)
        self.robotToSpinBox.setMaximum(100000)
        self.robotGridLayout.addWidget(self.robotToSpinBox, 1, 1, 1, 1)

        self.gridLayout.addWidget(self.robotGroupBox, 1, 1, 1, 1)

        self.horizontalLayoutWidget = QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QRect(150, 300, 310, 40))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.exitPushButton = QPushButton(self.horizontalLayoutWidget)
        font = QFont()
        font.setPointSize(14)
        self.exitPushButton.setFont(font)
        self.horizontalLayout.addWidget(self.exitPushButton)
        self.exitPushButton.clicked.connect(self.close)

        self.clearPushButton = QPushButton(self.horizontalLayoutWidget)
        font = QFont()
        font.setPointSize(14)
        self.clearPushButton.setFont(font)
        self.horizontalLayout.addWidget(self.clearPushButton)
        self.clearPushButton.clicked.connect(self.baseFromSpinBox.clear)
        self.clearPushButton.clicked.connect(self.baseToSpinBox.clear)
        self.clearPushButton.clicked.connect(self.stimFromSpinBox.clear)
        self.clearPushButton.clicked.connect(self.stimToSpinBox.clear)
        self.clearPushButton.clicked.connect(self.stimSplitSpinBox.clear)
        self.clearPushButton.clicked.connect(self.postFromSpinBox.clear)
        self.clearPushButton.clicked.connect(self.postToSpinBox.clear)
        self.clearPushButton.clicked.connect(self.robotFromSpinBox.clear)
        self.clearPushButton.clicked.connect(self.robotToSpinBox.clear)

        self.okPushButton = QPushButton(self.horizontalLayoutWidget)
        font = QFont()
        font.setPointSize(14)
        self.okPushButton.setFont(font)
        self.horizontalLayout.addWidget(self.okPushButton)
        self.okPushButton.clicked.connect(self.ok_clicked)

        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.baseFromSpinBox, self.baseToSpinBox)
        self.setTabOrder(self.baseToSpinBox, self.stimFromSpinBox)
        self.setTabOrder(self.stimFromSpinBox, self.stimToSpinBox)
        self.setTabOrder(self.stimToSpinBox, self.stimSplitSpinBox)
        self.setTabOrder(self.stimSplitSpinBox, self.postFromSpinBox)
        self.setTabOrder(self.postFromSpinBox, self.postToSpinBox)
        self.setTabOrder(self.postToSpinBox, self.robotFromSpinBox)
        self.setTabOrder(self.robotFromSpinBox, self.robotToSpinBox)
        self.setTabOrder(self.robotToSpinBox, self.clearPushButton)
        self.setTabOrder(self.clearPushButton, self.okPushButton)

    def ok_clicked(self):
        self.baseFrom = self.baseFromSpinBox.value()
        self.baseTo = self.baseToSpinBox.value()
        self.stimFrom = self.stimFromSpinBox.value()
        self.stimTo = self.stimToSpinBox.value()
        self.stimSplit = self.stimSplitSpinBox.value()
        self.postFrom = self.postFromSpinBox.value()
        self.postTo = self.postToSpinBox.value()
        self.robotFrom = self.robotFromSpinBox.value()
        self.robotTo = self.robotToSpinBox.value()
        self.close()

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Range"))
        self.stimGroupBox.setTitle(_translate("Dialog", "Stimulation"))
        self.stimFromLabel.setText(_translate("Dialog", "From:"))
        self.stimSplitLabel.setText(_translate("Dialog", "Split:"))
        self.stimToLabel.setText(_translate("Dialog", "To:"))
        self.BaseGroupBox.setTitle(_translate("Dialog", "Base (Pre-Robot)"))
        self.baseToLabel.setText(_translate("Dialog", "To:"))
        self.baseFromLabel.setText(_translate("Dialog", "From:"))
        self.postGroupBox.setTitle(_translate("Dialog", "Post (Post-Robot)"))
        self.postFromLabel.setText(_translate("Dialog", "From:"))
        self.postToLabel.setText(_translate("Dialog", "To:"))
        self.robotGroupBox.setTitle(_translate("Dialog", "Robot"))
        self.robotFromLabel.setText(_translate("Dialog", "From:"))
        self.robotToLabel.setText(_translate("Dialog", "To:"))
        self.exitPushButton.setText(_translate("Dialog", "Exit"))
        self.clearPushButton.setText(_translate("Dialog", "Clear"))
        self.okPushButton.setText(_translate("Dialog", "OK"))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUI()

        self.df = None

    def setupUI(self):
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QIcon(scriptDir + os.path.sep + 'rat.ico'))

        self.resize(440, 240)

        self.horizontalLayoutWidget = QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QRect(20, 40, 400, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(self.horizontalLayoutWidget)
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget)
        font = QFont()
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit.textChanged.connect(self.getFilePath)

        self.toolButton = QToolButton(self.horizontalLayoutWidget)
        font = QFont()
        font.setPointSize(18)
        self.toolButton.setFont(font)
        self.toolButton.clicked.connect(self.toolButton_clicked)
        self.horizontalLayout.addWidget(self.toolButton)

        self.horizontalLayoutWidget_2 = QWidget(self)
        self.horizontalLayoutWidget_2.setGeometry(QRect(150, 110, 270, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.exitPushButton = QPushButton(self.horizontalLayoutWidget_2)
        font = QFont()
        font.setPointSize(14)
        self.exitPushButton.setFont(font)
        self.horizontalLayout_2.addWidget(self.exitPushButton)
        self.exitPushButton.clicked.connect(self.close)

        self.okPushButton = QPushButton(self.horizontalLayoutWidget_2)
        font = QFont()
        font.setPointSize(14)
        self.okPushButton.setFont(font)
        self.horizontalLayout_2.addWidget(self.okPushButton)
        self.okPushButton.clicked.connect(self.okButton_clicked)

        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)

    def toolButton_clicked(self):
        # fname = QFileDialog.getOpenFileName(self, "Open File", "", "Nev File (*.nev)")
        # filename = QFileDialog.getOpenFileName(self, 'Open File', '', 'Nev File (*.nev)', None, QFileDialog.DontUseNativeDialog)
        dialog = QFileDialog(self)
        dialog.setWindowTitle('Open File')
        dialog.setNameFilter('Nev File (*.nev)')
        dialog.setFileMode(QFileDialog.ExistingFile)
        if dialog.exec_() == QDialog.Accepted:
            filename = dialog.selectedFiles()[0]
            if filename:
                self.lineEdit.setText(filename)
        # if fname:
        #     self.lineEdit.setText(fname[0])

    def getFilePath(self, text):
        self.df = Neuralynx.read_nev(text)

    def okButton_clicked(self):
        dig = rangeDialog()
        dig.exec_()
        if dig.baseFrom is not None and dig.baseTo is not None:
            Pre_robot = Program.base(self.df, dig.baseFrom, dig.baseTo)  # 829 1567

            if dig.stimFrom is not None and dig.stimTo is not None and dig.stimSplit is not None:
                Stim = Program.stim(self.df, dig.stimFrom, dig.stimTo, dig.stimSplit)  # 1567 1880

                if dig.postFrom is not None and dig.postTo is not None:
                    Post_robot = Program.post(self.df, dig.postFrom, dig.postTo)  # 2242 2790

                    if dig.robotFrom is not None and dig.robotTo is not None:
                        Robot = Program.robot(self.df, dig.robotFrom, dig.robotTo)  # 2790 3820

                        Stim_all = Program.stim_all(self.df)
                        Program.toExcel(Pre_robot, Stim, Post_robot, Robot, Stim_all)
        self.close()

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "KIM LAB"))
        self.label.setText(_translate("Dialog", "File:"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.exitPushButton.setText(_translate("Dialog", "Exit"))
        self.okPushButton.setText(_translate("Dialog", "OK"))


# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook

def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # app.exec_()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
