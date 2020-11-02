# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task manager_3.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from add_task_dialogue_ui import Ui_Dialog

add_task_details = {}

class task_block():

	def __init__(self, uimw, task_details: dict=None, n=0):
		#uimw = Ui_MainWindow object
		# self.uimw = uimw
		self.task_details = task_details
		self.task_block_frame = QtWidgets.QFrame(uimw.scrollAreaWidgetContents)
		self.task_block_frame.setGeometry(QtCore.QRect(10, 0, 741, 50))
		self.task_block_frame.setMinimumSize(741, 50)
		self.task_block_frame.setMaximumSize(741, 50)
		# print(uimw.task_block_frame.rect().getCoords()[0])
		self.task_block_frame.setStyleSheet("QFrame{"
											"background-color: rgb(138, 226, 52);"
											"border-radius: 25px;"
											"}")
		self.task_block_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.task_block_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.task_block_frame.setObjectName("task_block_frame")

		self.task_title_label = QtWidgets.QLabel(self.task_block_frame)
		self.task_title_label.setGeometry(QtCore.QRect(50, 10, 231, 30))
		# self.task_title_label.setMinimumSize(231, 30)
		font = QtGui.QFont()
		font.setFamily("Google Sans")
		self.task_title_label.setFont(font)
		self.task_title_label.setStyleSheet("QLabel {"
								"    border-radius: 15px;"
								"    background-color: rgb(229, 255, 203);"
								"}")
		self.task_title_label.setAlignment(QtCore.Qt.AlignCenter)
		self.task_title_label.setObjectName("task_title_label")

		self.checkBox = QtWidgets.QCheckBox(self.task_block_frame)
		self.checkBox.setGeometry(QtCore.QRect(15, 12, 26, 26))
		self.checkBox.setStyleSheet("QCheckBox {"
									"background-color: rgb(229, 255, 203);"
									"border-radius: 13px;"
									"padding: 6px;}")
		self.checkBox.setText("")
		self.checkBox.setObjectName("checkBox")
		self.checkBox.clicked.connect(self.toggle_subwidgets)
		self.date_label = QtWidgets.QLabel(self.task_block_frame)
		self.date_label.setGeometry(QtCore.QRect(300, 10, 111, 30))
		font = QtGui.QFont()
		font.setFamily("Google Sans")
		self.date_label.setFont(font)
		self.date_label.setStyleSheet("QLabel {"
								"    border-radius: 15px;"
								"    background-color: rgb(229, 255, 203);"
								"}")
		self.date_label.setAlignment(QtCore.Qt.AlignCenter)
		self.date_label.setObjectName("date_label")
		self.priority_label = QtWidgets.QLabel(self.task_block_frame)
		self.priority_label.setGeometry(QtCore.QRect(430, 10, 111, 30))
		font = QtGui.QFont()
		font.setFamily("Google Sans")
		self.priority_label.setFont(font)
		self.priority_label.setStyleSheet("QLabel {"
									"    border-radius: 15px;"
									"    background-color: rgb(229, 255, 203);"
									"}")
		self.priority_label.setAlignment(QtCore.Qt.AlignCenter)
		self.priority_label.setObjectName("priority_label")
		self.subject_label = QtWidgets.QLabel(self.task_block_frame)
		self.subject_label.setGeometry(QtCore.QRect(560, 10, 151, 30))
		font = QtGui.QFont()
		font.setFamily("Google Sans")
		self.subject_label.setFont(font)
		self.subject_label.setStyleSheet("QLabel {"
									"    border-radius: 15px;"
									"    background-color: rgb(229, 255, 203);"
									"}")
		self.subject_label.setAlignment(QtCore.Qt.AlignCenter)
		self.subject_label.setObjectName("subject_label")

	def toggle_subwidgets(self):
		checked = not self.checkBox.isChecked()
		self.task_title_label.setEnabled(checked)
		self.date_label.setEnabled(checked)
		self.priority_label.setEnabled(checked)
		self.subject_label.setEnabled(checked)

	def retranslateUi(self):
		_translate = QtCore.QCoreApplication.translate
		self.task_title_label.setText(self.task_details["title"])
		self.date_label.setText(self.task_details["date"])
		self.priority_label.setText(self.task_details["priority"])
		self.subject_label.setText(self.task_details["subject"])

class add_task_dialogue(QtWidgets.QDialog):

	def __init__(self):
		super().__init__()
		self.bt = QtWidgets.QDialogButtonBox.Save | QtWidgets.QDialogButtonBox.Cancel
		self.btbox = QtWidgets.QDialogButtonBox(self.bt)

		self.layout = QtWidgets.QVBoxLayout()
		self.layout.addWidget(self.bt)
		self.setLayout(self.layout)

		# self.bt.setGeometry(0, 0, 30, 20)


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		self.task_block_list = []
		self.vbox = QtWidgets.QVBoxLayout()
		self.vbox.setSpacing(-60)
		# self.vbox.setMargin(10)
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 600)
		MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setStyleSheet("QWidget {"
"background-color: rgb(229, 255, 203);"
"}")
		self.centralwidget.setObjectName("centralwidget")
		self.Tasks_head_label = QtWidgets.QLabel(self.centralwidget)
		self.Tasks_head_label.setGeometry(QtCore.QRect(-70, 30, 311, 80))
		font = QtGui.QFont()
		font.setFamily("Google Sans")
		font.setPointSize(20)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(7)
		self.Tasks_head_label.setFont(font)
		self.Tasks_head_label.setStyleSheet("QLabel{"
"font: 57 20pt \"Google Sans\";"
"color: rgb(72, 115, 35);"
"border-radius: 40px;"
"background-color: rgb(138, 226, 52);"
"padding: 0px 0px 0px 40px;"
"}"
"QLabel::hover{"
"color: rgb(32, 74, 135);"
"background-color: rgb(114, 159, 207);"
"}")
		self.Tasks_head_label.setAlignment(QtCore.Qt.AlignCenter)
		self.Tasks_head_label.setObjectName("Tasks_head_label")
		self.active_tasks_label = QtWidgets.QLabel(self.centralwidget)
		self.active_tasks_label.setGeometry(QtCore.QRect(330, 30, 141, 80))
		font = QtGui.QFont()
		font.setFamily("Google Sans")
		font.setPointSize(14)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(7)
		self.active_tasks_label.setFont(font)
		self.active_tasks_label.setStyleSheet("QLabel{"
"font: 57 14pt \"Google Sans\";"
"color: rgb(52, 101, 164);"
"border-radius: 40px;"
"background-color: rgb(159, 216, 243);"
"}")
		self.active_tasks_label.setAlignment(QtCore.Qt.AlignCenter)
		self.active_tasks_label.setObjectName("active_tasks_label")
		self.competed_label = QtWidgets.QLabel(self.centralwidget)
		self.competed_label.setGeometry(QtCore.QRect(490, 30, 131, 80))
		font = QtGui.QFont()
		font.setFamily("Google Sans")
		font.setPointSize(14)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(7)
		self.competed_label.setFont(font)
		self.competed_label.setStyleSheet("QLabel{"
"font: 57 14pt \"Google Sans\";"
"border-radius: 40px;"
"color: rgb(72, 115, 35);"
"background-color: rgb(169, 229, 110);"
"}")
		self.competed_label.setAlignment(QtCore.Qt.AlignCenter)
		self.competed_label.setObjectName("competed_label")
		self.overdue_label = QtWidgets.QLabel(self.centralwidget)
		self.overdue_label.setGeometry(QtCore.QRect(640, 30, 131, 80))
		font = QtGui.QFont()
		font.setFamily("Google Sans")
		font.setPointSize(14)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(7)
		self.overdue_label.setFont(font)
		self.overdue_label.setStyleSheet("QLabel{"
"font: 57 14pt \"Google Sans\";"
"border-radius: 40px;"
"color: rgb(143, 89, 2);"
"background-color: rgb(252, 233, 79);"
"}")
		self.overdue_label.setAlignment(QtCore.Qt.AlignCenter)
		self.overdue_label.setObjectName("overdue_label")	
		self.add_task_label = QtWidgets.QLabel(self.centralwidget)
		self.add_task_label.setGeometry(QtCore.QRect(650, 480, 231, 151))
		font = QtGui.QFont()
		font.setFamily("Google Sans")
		font.setPointSize(18)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(7)
		self.add_task_label.setFont(font)
		self.add_task_label.mousePressEvent = self.add_task
		self.add_task_label.setStyleSheet("QLabel{"
"font: 57 18pt \"Google Sans\";"
"color: rgb(72, 115, 35);"
"border-radius: 50px;"
"background-color: rgb(138, 226, 52);"
"padding: 0px 70px 70px 0px;"
"}"
"QLabel::hover{"
"color: rgb(32, 74, 135);"
"border-radius: 50px;"
"background-color: rgb(114, 159, 207);"
"}<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
"<ui version=\"4.0\">"
" <widget name=\"__qt_fake_top_level\">"
"  <widget class=\"QLabel\" name=\"label_8\">"
"   <property name=\"geometry\">"
"    <rect>"
"     <x>330</x>"
"     <y>20</y>"
"     <width>131</width>"
"     <height>80</height>"
"    </rect>"
"   </property>"
"   <property name=\"font\">"
"    <font>"
"     <family>Google Sans</family>"
"     <pointsize>14</pointsize>"
"     <weight>7</weight>"
"     <italic>false</italic>"
"     <bold>false</bold>"
"    </font>"
"   </property>"
"   <property name=\"styleSheet\">"
"    <string notr=\"true\">QLabel{"
"font: 57 14pt &quot;Google Sans&quot;;"
"color: rgb(72, 115, 35);"
"border-radius: 40px;"
"background-color: rgb(138, 226, 52);"
"}"
"QLabel::hover{"
"color: rgb(32, 74, 135);"
"background-color: rgb(114, 159, 207);"
"}</string>"
"   </property>"
"   <property name=\"text\">"
"    <string>Active Tasks"
"0</string>"
"   </property>"
"   <property name=\"alignment\">"
"    <set>Qt::AlignCenter</set>"
"   </property>"
"  </widget>"
" </widget>"
" <resources/>"
"</ui>"
"")
		self.add_task_label.setAlignment(QtCore.Qt.AlignCenter)
		self.add_task_label.setObjectName("add_task_label")
		self.date_select_frame = QtWidgets.QFrame(self.centralwidget)
		self.date_select_frame.setGeometry(QtCore.QRect(-90, 470, 251, 171))
		self.date_select_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.date_select_frame.setFrameShadow(QtWidgets.QFrame.Plain)
		self.date_select_frame.setObjectName("date_select_frame")
		self.date_select_label = QtWidgets.QLabel(self.date_select_frame)
		self.date_select_label.setGeometry(QtCore.QRect(10, 10, 231, 151))
		font = QtGui.QFont()
		font.setFamily("Google Sans")
		font.setPointSize(18)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(7)
		self.date_select_label.setFont(font)
		self.date_select_label.setStyleSheet("QLabel{"
"font: 57 18pt \"Google Sans\";"
"color: rgb(72, 115, 35);"
"border-radius: 50px;"
"background-color: rgb(138, 226, 52);"
"padding: 0px 0px 70px 70px;"
"}"
"QLabel::hover{"
"color: rgb(32, 74, 135);"
"border-radius: 50px;"
"background-color: rgb(114, 159, 207);"
"}<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
"<ui version=\"4.0\">"
" <widget name=\"__qt_fake_top_level\">"
"  <widget class=\"QLabel\" name=\"label_8\">"
"   <property name=\"geometry\">"
"    <rect>"
"     <x>330</x>"
"     <y>20</y>"
"     <width>131</width>"
"     <height>80</height>"
"    </rect>"
"   </property>"
"   <property name=\"font\">"
"    <font>"
"     <family>Google Sans</family>"
"     <pointsize>14</pointsize>"
"     <weight>7</weight>"
"     <italic>false</italic>"
"     <bold>false</bold>"
"    </font>"
"   </property>"
"   <property name=\"styleSheet\">"
"    <string notr=\"true\">QLabel{"
"font: 57 14pt &quot;Google Sans&quot;;"
"color: rgb(72, 115, 35);"
"border-radius: 40px;"
"background-color: rgb(138, 226, 52);"
"}"
"QLabel::hover{"
"color: rgb(32, 74, 135);"
"background-color: rgb(114, 159, 207);"
"}</string>"
"   </property>"
"   <property name=\"text\">"
"    <string>Active Tasks"
"0</string>"
"   </property>"
"   <property name=\"alignment\">"
"    <set>Qt::AlignCenter</set>"
"   </property>"
"  </widget>"
" </widget>"
" <resources/>"
"</ui>"
"")
		self.date_select_label.setAlignment(QtCore.Qt.AlignCenter)
		self.date_select_label.setObjectName("date_select_label")
		self.date_select_combox = QtWidgets.QComboBox(self.date_select_frame)
		self.date_select_combox.setGeometry(QtCore.QRect(108, 80, 111, 28))
		font = QtGui.QFont()
		font.setFamily("Google Sans")
		font.setPointSize(11)
		self.date_select_combox.setFont(font)
		self.date_select_combox.setStyleSheet("QComboBox {"
"    text-align: center;"
"}"
""
"QListView {"
"    background-color: rgb(175, 235, 114);"
"}")
		self.date_select_combox.setObjectName("date_select_combox")
		self.date_select_combox.addItem("")
		self.date_select_combox.addItem("")
		self.sub_select_frame = QtWidgets.QFrame(self.centralwidget)
		self.sub_select_frame.setGeometry(QtCore.QRect(200, 470, 191, 171))
		self.sub_select_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.sub_select_frame.setFrameShadow(QtWidgets.QFrame.Plain)
		self.sub_select_frame.setObjectName("sub_select_frame")
		self.sub_select_label = QtWidgets.QLabel(self.sub_select_frame)
		self.sub_select_label.setGeometry(QtCore.QRect(10, 10, 171, 151))
		font = QtGui.QFont()
		font.setFamily("Google Sans")
		font.setPointSize(16)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(7)
		self.sub_select_label.setFont(font)
		self.sub_select_label.setStyleSheet("QLabel{"
"font: 57 16pt \"Google Sans\";"
"color: rgb(72, 115, 35);"
"border-radius: 50px;"
"background-color: rgb(138, 226, 52);"
"padding: 0px 0px 70px 0px;"
"}"
"QLabel::hover{"
"color: rgb(32, 74, 135);"
"border-radius: 50px;"
"background-color: rgb(114, 159, 207);"
"}<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
"<ui version=\"4.0\">"
" <widget name=\"__qt_fake_top_level\">"
"  <widget class=\"QLabel\" name=\"label_8\">"
"   <property name=\"geometry\">"
"    <rect>"
"     <x>330</x>"
"     <y>20</y>"
"     <width>131</width>"
"     <height>80</height>"
"    </rect>"
"   </property>"
"   <property name=\"font\">"
"    <font>"
"     <family>Google Sans</family>"
"     <pointsize>14</pointsize>"
"     <weight>7</weight>"
"     <italic>false</italic>"
"     <bold>false</bold>"
"    </font>"
"   </property>"
"   <property name=\"styleSheet\">"
"    <string notr=\"true\">QLabel{"
"font: 57 14pt &quot;Google Sans&quot;;"
"color: rgb(72, 115, 35);"
"border-radius: 40px;"
"background-color: rgb(138, 226, 52);"
"}"
"QLabel::hover{"
"color: rgb(32, 74, 135);"
"background-color: rgb(114, 159, 207);"
"}</string>"
"   </property>"
"   <property name=\"text\">"
"    <string>Active Tasks"
"0</string>"
"   </property>"
"   <property name=\"alignment\">"
"    <set>Qt::AlignCenter</set>"
"   </property>"
"  </widget>"
" </widget>"
" <resources/>"
"</ui>"
"")
		self.sub_select_label.setAlignment(QtCore.Qt.AlignCenter)
		self.sub_select_label.setObjectName("sub_select_label")
		self.sub_select_combox = QtWidgets.QComboBox(self.sub_select_frame)
		self.sub_select_combox.setGeometry(QtCore.QRect(30, 80, 131, 28))
		font = QtGui.QFont()
		font.setFamily("Google Sans")
		font.setPointSize(11)
		self.sub_select_combox.setFont(font)
		self.sub_select_combox.setStyleSheet("QComboBox {"
"    text-align: center;"
"}"
""
"QListView {"
"    background-color: rgb(175, 235, 114);"
"}")
		self.sub_select_combox.setObjectName("sub_select_combox")
		self.sub_select_combox.addItem("")
		self.sub_select_combox.addItem("")
		self.sub_select_combox.addItem("")
		self.sub_select_combox.addItem("")
		self.sub_select_combox.addItem("")
		self.sub_select_combox.addItem("")
		self.priority_select_frame = QtWidgets.QFrame(self.centralwidget)
		self.priority_select_frame.setGeometry(QtCore.QRect(410, 470, 191, 171))
		self.priority_select_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.priority_select_frame.setFrameShadow(QtWidgets.QFrame.Plain)
		self.priority_select_frame.setObjectName("priority_select_frame")
		self.priority_select_label = QtWidgets.QLabel(self.priority_select_frame)
		self.priority_select_label.setGeometry(QtCore.QRect(10, 10, 171, 151))
		font = QtGui.QFont()
		font.setFamily("Google Sans")
		font.setPointSize(16)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(7)
		self.priority_select_label.setFont(font)
		self.priority_select_label.setStyleSheet("QLabel{"
"font: 57 16pt \"Google Sans\";"
"color: rgb(72, 115, 35);"
"border-radius: 50px;"
"background-color: rgb(138, 226, 52);"
"padding: 0px 0px 70px 0px;"
"}"
"QLabel::hover{"
"color: rgb(32, 74, 135);"
"border-radius: 50px;"
"background-color: rgb(114, 159, 207);"
"}<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
"<ui version=\"4.0\">"
" <widget name=\"__qt_fake_top_level\">"
"  <widget class=\"QLabel\" name=\"label_8\">"
"   <property name=\"geometry\">"
"    <rect>"
"     <x>330</x>"
"     <y>20</y>"
"     <width>131</width>"
"     <height>80</height>"
"    </rect>"
"   </property>"
"   <property name=\"font\">"
"    <font>"
"     <family>Google Sans</family>"
"     <pointsize>14</pointsize>"
"     <weight>7</weight>"
"     <italic>false</italic>"
"     <bold>false</bold>"
"    </font>"
"   </property>"
"   <property name=\"styleSheet\">"
"    <string notr=\"true\">QLabel{"
"font: 57 14pt &quot;Google Sans&quot;;"
"color: rgb(72, 115, 35);"
"border-radius: 40px;"
"background-color: rgb(138, 226, 52);"
"}"
"QLabel::hover{"
"color: rgb(32, 74, 135);"
"background-color: rgb(114, 159, 207);"
"}</string>"
"   </property>"
"   <property name=\"text\">"
"    <string>Active Tasks"
"0</string>"
"   </property>"
"   <property name=\"alignment\">"
"    <set>Qt::AlignCenter</set>"
"   </property>"
"  </widget>"
" </widget>"
" <resources/>"
"</ui>"
"")
		self.priority_select_label.setAlignment(QtCore.Qt.AlignCenter)
		self.priority_select_label.setObjectName("priority_select_label")
		self.priority_select_combox = QtWidgets.QComboBox(self.priority_select_frame)
		self.priority_select_combox.setGeometry(QtCore.QRect(50, 80, 81, 28))
		font = QtGui.QFont()
		font.setFamily("Google Sans")
		font.setPointSize(11)
		self.priority_select_combox.setFont(font)
		self.priority_select_combox.setStyleSheet("QComboBox {"
"    text-align: center;"
"}"
""
"QListView {"
"    background-color: rgb(175, 235, 114);"
"}")
		self.priority_select_combox.setObjectName("priority_select_combox")
		self.priority_select_combox.addItem("")
		self.priority_select_combox.addItem("")
		self.priority_select_combox.addItem("")
		self.priority_select_combox.addItem("")
		self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
		self.scrollArea.setGeometry(20, 120, 770, 311)
		self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
		self.scrollArea.setWidgetResizable(True)
		# self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
		self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		# self.scrollArea.setFixedWidth(800)
		self.scrollArea.setObjectName("scrollArea")
		self.scrollAreaWidgetContents = QtWidgets.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 771, 311))
		self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

		# self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		self.scrollArea.raise_()
		self.priority_select_frame.raise_()
		self.sub_select_frame.raise_()
		self.Tasks_head_label.raise_()
		self.active_tasks_label.raise_()
		self.competed_label.raise_()
		self.overdue_label.raise_()
		self.add_task_label.raise_()
		self.date_select_frame.raise_()
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
		self.menubar.setObjectName("menubar")
		self.menuFile = QtWidgets.QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.actionHome = QtWidgets.QAction(MainWindow)
		self.actionHome.setObjectName("actionHome")
		self.menuFile.addAction(self.actionHome)
		self.menubar.addAction(self.menuFile.menuAction())

		# self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def add_task(self, event):
		Dialog = QtWidgets.QDialog()
		uid = Ui_Dialog()
		uid.setupUi(Dialog)
		Dialog.exec_()
		self.add_task_blocks({"0":uid.get_details()})


	def add_task_blocks(self, tasks_dict):
		tasks = tasks_dict.values()
		for n, task in enumerate(tasks):
			task_block_obj = task_block(self, task, n)
			self.task_block_list.append(task_block_obj)
			task_block_obj.retranslateUi()
			self.vbox.addWidget(task_block_obj.task_block_frame)
		self.scrollAreaWidgetContents.setLayout(self.vbox)
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)

	# def add_task_blocks(self):
	# 	# print('entered add task blocks')
	# 	for n in range(40):
	# 		x = QtWidgets.QLabel("hello")
	# 		self.vbox.addWidget(x)
	# 	self.scrollAreaWidgetContents.setLayout(self.vbox)
	# 	self.scrollArea.setWidget(self.scrollAreaWidgetContents)
			
	# def add_task_block():
	# 	task_block_obj

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.Tasks_head_label.setText(_translate("MainWindow", "Tasks"))
		self.active_tasks_label.setText(_translate("MainWindow", "Active Tasks"
"\n0"))
		self.competed_label.setText(_translate("MainWindow", "Completed"
"\n0"))
		self.overdue_label.setText(_translate("MainWindow", "Overdue"
"\n0"))
		self.add_task_label.setText(_translate("MainWindow", "Add Task"))
		self.date_select_label.setText(_translate("MainWindow", "Today"))
		self.date_select_combox.setItemText(0, _translate("MainWindow", "Today"))
		self.date_select_combox.setItemText(1, _translate("MainWindow", "Tomorrow"))
		self.sub_select_label.setText(_translate("MainWindow", "All Subjects"))
		self.sub_select_combox.setItemText(0, _translate("MainWindow", "All"))
		self.sub_select_combox.setItemText(1, _translate("MainWindow", "Physics"))
		self.sub_select_combox.setItemText(2, _translate("MainWindow", "Chemistry"))
		self.sub_select_combox.setItemText(3, _translate("MainWindow", "Maths"))
		self.sub_select_combox.setItemText(4, _translate("MainWindow", "Computer Science"))
		self.sub_select_combox.setItemText(5, _translate("MainWindow", "Biology"))
		self.priority_select_label.setText(_translate("MainWindow", "All Priority"))
		self.priority_select_combox.setItemText(0, _translate("MainWindow", "All"))
		self.priority_select_combox.setItemText(1, _translate("MainWindow", "Low"))
		self.priority_select_combox.setItemText(2, _translate("MainWindow", "Medium"))
		self.priority_select_combox.setItemText(3, _translate("MainWindow", "High"))
		self.menuFile.setTitle(_translate("MainWindow", "File"))
		self.actionHome.setText(_translate("MainWindow", "Home"))

		for i, tb in enumerate(self.task_block_list):
			tb.retranslateUi()
			# tb.setGeometry(QtCore.QRect(10, (i*60)+20, 741, 50))
			# tb.setText('abcd')



if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
