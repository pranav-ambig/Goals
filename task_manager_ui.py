# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task manager.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):

    def __init__(self):
        self.task_rows = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setGeometry(QtCore.QRect(10, 520, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.homeButton.setFont(font)
        self.homeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homeButton.setFlat(True)
        self.homeButton.setObjectName("homeButton")
        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(300, 20, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.heading.setFont(font)
        self.heading.setStyleSheet("")
        self.heading.setObjectName("heading")
        self.tasksLabel = QtWidgets.QLabel(self.centralwidget)
        self.tasksLabel.setGeometry(QtCore.QRect(40, 80, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tasksLabel.setFont(font)
        self.tasksLabel.setObjectName("tasksLabel")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 120, 751, 341))
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 741, 311))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 739, 309))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab, "")

        self.add_task_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_task_button.setGeometry(QtCore.QRect(300, 520, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.add_task_button.setFont(font)
        self.add_task_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_task_button.setFlat(True)
        self.add_task_button.setObjectName("add_task_button")
        self.add_task_button.clicked.connect(self.add_task)

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def add_task(self):
        task_row(self).groupBox.show()
        self.scrollArea.show()
        
        _translate = QtCore.QCoreApplication.translate
        for tr in self.task_rows:
            tr.comboBox.setItemText(0, _translate("MainWindow", "Low"))
            tr.comboBox.setItemText(1, _translate("MainWindow", "Medium"))
            tr.comboBox.setItemText(2, _translate("MainWindow", "High"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.homeButton.setText(_translate("MainWindow", "< Home"))
        self.add_task_button.setText(_translate("MainWindow", "Add task"))
        self.heading.setText(_translate("MainWindow", "Task Manager"))
        self.tasksLabel.setText(_translate("MainWindow", "Tasks"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Today"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tommorow"))


class task_row:
    def __init__(self, uimw: Ui_MainWindow):
        if not len(uimw.task_rows):
            y = 0
        else:
            y = len(uimw.task_rows)*45

        self.groupBox = QtWidgets.QGroupBox(uimw.scrollAreaWidgetContents)
        self.groupBox.setGeometry(QtCore.QRect(0, y, 700, 61))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 30, 113, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 30, 21, 26))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(170, 30, 110, 29))
        self.dateEdit.setObjectName("dateEdit")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(290, 30, 91, 28))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(400, 30, 101, 28))
        self.comboBox_2.setObjectName("comboBox_2")
        uimw.task_rows.append(self)


if __name__ == "__main__":
    import sys
    global MainWindow
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
