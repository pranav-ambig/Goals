from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPropertyAnimation, QEvent
from add_task_dialogue_ui import Ui_Dialog
import datetime
from playsound import playsound
import json

tasks_dict = {}
current_date = datetime.date.today()

class task_block():

	def __init__(self, uimw, task_details: dict=None, index="0"):
		#uimw = Ui_MainWindow object
		self.uimw = uimw
		self.index = index
		self.task_details = task_details
		self.task_block_frame = QtWidgets.QFrame(uimw.scrollAreaWidgetContents)
		self.task_block_frame.setGeometry(QtCore.QRect(10, 0, 741, 50))
		self.task_block_frame.setMinimumSize(741, 50)
		self.task_block_frame.setMaximumSize(741, 50)
		self.task_block_frame.setStyleSheet("QFrame{"
											"background-color: rgb(138, 226, 52);"
											"border-radius: 25px;"
											"}")
		self.task_block_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.task_block_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.task_block_frame.setObjectName("task_block_frame")

		self.task_title_label = QtWidgets.QLabel(self.task_block_frame)
		self.task_title_label.setGeometry(QtCore.QRect(50, 10, 231, 30))

		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
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
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		self.date_label.setFont(font)
		self.date_label.setStyleSheet("QLabel {"
								"    border-radius: 15px;"
								"    background-color: rgb(229, 255, 203);"
								"}")
		self.date_label.setAlignment(QtCore.Qt.AlignCenter)
		self.date_label.setObjectName("date_label")
		self.priority_label = QtWidgets.QLabel(self.task_block_frame)
		self.priority_label.setGeometry(QtCore.QRect(430, 10, 111, 30))
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		self.priority_label.setFont(font)
		self.priority_label.setStyleSheet("QLabel {"
									"    border-radius: 15px;"
									"    background-color: rgb(229, 255, 203);"
									"}")
		self.priority_label.setAlignment(QtCore.Qt.AlignCenter)
		self.priority_label.setObjectName("priority_label")
		self.subject_label = QtWidgets.QLabel(self.task_block_frame)
		self.subject_label.setGeometry(QtCore.QRect(560, 10, 151, 30))
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
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
		if not checked:
			tasks_dict[self.index]["checked"] = "T"
			playsound("Task_done.ogg")
		else:
			tasks_dict[self.index]["checked"] = "F"
		self.uimw.sort_tasks()

	def toggle_subwidgets_only(self):
		self.checkBox.setChecked(True)
		self.task_title_label.setEnabled(False)
		self.date_label.setEnabled(False)
		self.priority_label.setEnabled(False)
		self.subject_label.setEnabled(False)

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

class select_date_dialogue(QtWidgets.QDialog):

	def __init__(self, uimw):
		super().__init__()

		self.lbl = QtWidgets.QLabel("Select Date")
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		self.lbl.setFont(font)

		self.setWindowTitle("Select Date")

		self.de = QtWidgets.QDateEdit()
		self.bt = QtWidgets.QDialogButtonBox.Ok
		self.btbox = QtWidgets.QDialogButtonBox(self.bt)

		self.layout = QtWidgets.QVBoxLayout()
		self.layout.addWidget(self.lbl)
		self.layout.addWidget(self.de)
		self.layout.addWidget(self.btbox)
		self.setLayout(self.layout)
		self.btbox.accepted.connect(lambda: self.update_date_label(uimw))

	def update_date_label(self, uimw):
		print(self.de)
		d = self.de.date()
		d = '/'.join((str(d.day()), str(d.month()), str(d.year())))
		uimw.selected_date = d
		self.close()

class Ui_MainWindow(QtWidgets.QWidget):
	def setupUi(self, MainWindow):
		self.task_block_list = []
		self.ac, self.comc, self.oc = 0, 0, 0
		self.vbox = QtWidgets.QVBoxLayout()
		self.vbox.setSpacing(-60)
		self.selected_date = "Today"
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
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		font.setPointSize(20)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(7)
		self.Tasks_head_label.setFont(font)
		self.Tasks_head_label.setStyleSheet("QLabel{"
"font: 57 20pt \"Baloo2\";"
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
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		font.setPointSize(14)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(7)
		self.active_tasks_label.setFont(font)
		self.active_tasks_label.setStyleSheet("QLabel{"
"font: 57 14pt \"Baloo2\";"
"color: rgb(52, 101, 164);"
"border-radius: 40px;"
"background-color: rgb(159, 216, 243);"
"}")
		self.active_tasks_label.setAlignment(QtCore.Qt.AlignCenter)
		self.active_tasks_label.setObjectName("active_tasks_label")
		self.completed_label = QtWidgets.QLabel(self.centralwidget)
		self.completed_label.setGeometry(QtCore.QRect(490, 30, 131, 80))
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		font.setPointSize(14)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(7)
		self.completed_label.setFont(font)
		self.completed_label.setStyleSheet("QLabel{"
"font: 57 14pt \"Baloo2\";"
"border-radius: 40px;"
"color: rgb(72, 115, 35);"
"background-color: rgb(169, 229, 110);"
"}")
		self.completed_label.setAlignment(QtCore.Qt.AlignCenter)
		self.completed_label.setObjectName("competed_label")
		self.overdue_label = QtWidgets.QLabel(self.centralwidget)
		self.overdue_label.setGeometry(QtCore.QRect(640, 30, 131, 80))
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		font.setPointSize(14)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(7)
		self.overdue_label.setFont(font)
		self.overdue_label.setStyleSheet("QLabel{"
"font: 57 14pt \"Baloo2\";"
"border-radius: 40px;"
"color: rgb(143, 89, 2);"
"background-color: rgb(252, 233, 79);"
"}")
		self.overdue_label.setAlignment(QtCore.Qt.AlignCenter)
		self.overdue_label.setObjectName("overdue_label")	
		self.add_task_label = QtWidgets.QLabel(self.centralwidget)
		self.add_task_label.setGeometry(QtCore.QRect(650, 500, 231, 151))
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		font.setPointSize(18)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(7)
		self.add_task_label.setFont(font)
		self.add_task_label.mousePressEvent = self.add_task
		self.add_task_label.setStyleSheet("QLabel{"
"font: 57 18pt \"Baloo2\";"
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
"     <family>Baloo2</family>"
"     <pointsize>14</pointsize>"
"     <weight>7</weight>"
"     <italic>false</italic>"
"     <bold>false</bold>"
"    </font>"
"   </property>"
"   <property name=\"styleSheet\">"
"    <string notr=\"true\">QLabel{"
"font: 57 14pt &quot;Baloo2&quot;;"
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
		self.date_select_frame.setGeometry(QtCore.QRect(-90, 495, 251, 171))
		self.date_select_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.date_select_frame.setFrameShadow(QtWidgets.QFrame.Plain)
		self.date_select_frame.setObjectName("date_select_frame")

		self.date_select_label = QtWidgets.QLabel(self.date_select_frame)
		self.date_select_label.setGeometry(QtCore.QRect(10, 10, 231, 151))
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		font.setPointSize(18)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(7)
		self.date_select_label.setFont(font)
		self.date_select_label.setStyleSheet("QLabel{"
"font: 57 18pt \"Baloo2\";"
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
"     <family>Baloo2</family>"
"     <pointsize>14</pointsize>"
"     <weight>7</weight>"
"     <italic>false</italic>"
"     <bold>false</bold>"
"    </font>"
"   </property>"
"   <property name=\"styleSheet\">"
"    <string notr=\"true\">QLabel{"
"font: 57 14pt &quot;Baloo2&quot;;"
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
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
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
		self.date_select_combox.addItem("")
		self.sub_select_frame = QtWidgets.QFrame(self.centralwidget)
		self.sub_select_frame.setGeometry(QtCore.QRect(200, 495, 191, 171))
		self.sub_select_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.sub_select_frame.setFrameShadow(QtWidgets.QFrame.Plain)
		self.sub_select_frame.setObjectName("sub_select_frame")
		self.sub_select_label = QtWidgets.QLabel(self.sub_select_frame)
		self.sub_select_label.setGeometry(QtCore.QRect(10, 10, 171, 151))
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		font.setPointSize(16)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(7)
		self.sub_select_label.setFont(font)
		self.sub_select_label.setStyleSheet("QLabel{"
"font: 57 16pt \"Baloo2\";"
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
"     <family>Baloo2</family>"
"     <pointsize>14</pointsize>"
"     <weight>7</weight>"
"     <italic>false</italic>"
"     <bold>false</bold>"
"    </font>"
"   </property>"
"   <property name=\"styleSheet\">"
"    <string notr=\"true\">QLabel{"
"font: 57 14pt &quot;Baloo2&quot;;"
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
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		font.setPointSize(11)
		self.sub_select_combox.setFont(font)
		self.sub_select_combox.setStyleSheet("QComboBox {"
"text-align: center;"
"}"
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
		self.priority_select_frame.setGeometry(QtCore.QRect(410, 495, 191, 171))
		self.priority_select_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.priority_select_frame.setFrameShadow(QtWidgets.QFrame.Plain)
		self.priority_select_frame.setObjectName("priority_select_frame")
		self.priority_select_label = QtWidgets.QLabel(self.priority_select_frame)
		self.priority_select_label.setGeometry(QtCore.QRect(10, 10, 171, 151))
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		font.setPointSize(16)
		font.setBold(False)
		font.setItalic(False)
		font.setWeight(7)
		self.priority_select_label.setFont(font)
		self.priority_select_label.setStyleSheet("QLabel{"
"font: 57 16pt \"Baloo2\";"
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
"     <family>Baloo2</family>"
"     <pointsize>14</pointsize>"
"     <weight>7</weight>"
"     <italic>false</italic>"
"     <bold>false</bold>"
"    </font>"
"   </property>"
"   <property name=\"styleSheet\">"
"    <string notr=\"true\">QLabel{"
"font: 57 14pt &quot;Baloo2&quot;;"
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
		self.priority_select_combox.setGeometry(QtCore.QRect(40, 80, 91, 28))
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
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
		self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.scrollArea.setObjectName("scrollArea")
		self.scrollAreaWidgetContents = QtWidgets.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 771, 311))
		self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

		self.scrollArea.raise_()
		self.priority_select_frame.raise_()
		self.sub_select_frame.raise_()
		self.Tasks_head_label.raise_()
		self.active_tasks_label.raise_()
		self.completed_label.raise_()
		self.overdue_label.raise_()
		self.add_task_label.raise_()
		self.date_select_frame.raise_()
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.actionDoc = QtWidgets.QAction(MainWindow)
		self.actionDoc.setObjectName("actionDoc")
	
		self.date_select_frame.installEventFilter(self)
		self.priority_select_frame.installEventFilter(self)
		self.sub_select_frame.installEventFilter(self)

		self.date_select_combox.currentTextChanged.connect(self.sort_tasks)
		self.sub_select_combox.currentTextChanged.connect(self.sort_tasks)
		self.priority_select_combox.currentTextChanged.connect(self.sort_tasks)

		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def add_task(self, event):
		Dialog = QtWidgets.QDialog()
		uid = Ui_Dialog()
		uid.setupUi(Dialog)
		Dialog.exec_()
		d = uid.get_details()
		if d:
			n = len(tasks_dict.values())
			tasks_dict[str(n)] = d
			self.sort_tasks()

	def sort_tasks(self):
		global tasks_dict
		self.empty_layout()

		tasks = tasks_dict.items()
		sorted_tasks = []

		self.selected_date = self.date_select_combox.currentText()
		self.date_select_label.setText(str(self.selected_date))

		if self.selected_date == 'Today':
			self.selected_date = current_date
			self.ac, self.comc, self.oc = 0, 0, 0 
		elif self.selected_date == 'Tomorrow':
			self.selected_date = current_date + datetime.timedelta(days=1)
		else:
			dlg = select_date_dialogue(self)
			dlg.exec_()
			if self.selected_date == "Select Date":
				self.selected_date = "Today"
				self.date_select_combox.setCurrentText(self.selected_date)
				return
			self.date_select_label.setText(self.selected_date)
			d = self.selected_date.split('/')
			self.selected_date = datetime.date(int(d[2]), int(d[1]), int(d[0]))

		self.selected_subject = self.sub_select_combox.currentText()
		if self.selected_subject == "All":
			self.sub_select_label.setText("All Subjects")
		else:	
			self.sub_select_label.setText(self.selected_subject)

		self.selected_priority = self.priority_select_combox.currentText()
		if self.selected_priority == "All":
			self.priority_select_label.setText("All Priority")
		else:	
			self.priority_select_label.setText(self.selected_priority)

		for index, task in tasks:
			dt, s, p = False, False, False
			pval = 0 #priority value

			d = task["date"].split('/')
			d = datetime.date(int(d[2]), int(d[1]), int(d[0]))
			if d == self.selected_date:
				if self.selected_date == current_date:
					self.ac += 1
				dt = True
				pval += 1
			elif d < self.selected_date:
				if self.selected_date == current_date:
					self.oc += 1
					dt = True
				pval += 3
			
			if self.selected_subject == "All":
				s = True
			else:
				if task["subject"] == self.selected_subject:
					s = True

			if self.selected_priority == "All":
				p = True
			else:
				if task["priority"] == self.selected_priority:
					p = True

			if task["priority"] == "High":
				pval += 2
			elif task["priority"] == "Medium":
				pval += 1
			else:
				pval += 0

			if dt and s and p:
				sorted_tasks.append((index, task, pval))

			dt, s, p = False, False, False


		sorted_tasks.sort(key=lambda t: t[2], reverse=True)

		self.ac, self.comc, self.oc = 0, 0, 0

		for index, task, pval in sorted_tasks:
			task_block_obj = task_block(self, task, index=index)

			d = task["date"].split('/')
			d = datetime.date(int(d[2]), int(d[1]), int(d[0]))

			if d < current_date:
				if task["checked"] == "T":
					self.comc += 1
				else:
					self.oc += 1
				task_block_obj.date_label.setStyleSheet("QLabel {"
						"    border-radius: 15px;"
						"    background-color: rgb(252, 233, 79);"
						"}")
			else:
				if self.selected_date == current_date:
					if task["checked"] == "T":
						self.comc += 1
					else:
						self.ac += 1
					task_block_obj.date_label.setStyleSheet("QLabel {"
							"    border-radius: 15px;"
							"    background-color: rgb(159, 216, 243);"
							"}")

			if task["priority"] == "High":
				task_block_obj.priority_label.setStyleSheet("QLabel {"
						"    border-radius: 15px;"
						"    background-color: rgb(255, 100, 100);"
						"}")
			elif task["priority"] == "Medium":
				task_block_obj.priority_label.setStyleSheet("QLabel {"
						"    border-radius: 15px;"
						"    background-color: rgb(255, 230, 128);"
						"}")
			else:
				task_block_obj.priority_label.setStyleSheet("QLabel {"
						"    border-radius: 15px;"
						"    background-color: rgb(179, 255, 128);"
						"}")

			if task["checked"] == "T":
				task_block_obj.toggle_subwidgets_only()
			self.task_block_list.append(task_block_obj)
			task_block_obj.retranslateUi()
			self.vbox.addWidget(task_block_obj.task_block_frame)

		self.scrollAreaWidgetContents.setLayout(self.vbox)
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		self.retranslateUi(self)
		if self.selected_date == current_date:
			self.update_number_labels()
		if not len(sorted_tasks):
			self.statusbar.showMessage("No tasks currently, click Add task to add one")
		else:
			self.statusbar.showMessage("")
			



	def move_animation(self, wdgt, dirn_up=True):
		self.anim = QPropertyAnimation(wdgt, b"geometry")
		self.anim.setDuration(100)
		temp = wdgt.rect()
		x = wdgt.x()
		y = wdgt.y()
		w = temp.width()
		h = temp.height()

		self.anim.setStartValue(QtCore.QRect(x, y, w, h))
		if dirn_up:
			self.anim.setEndValue(QtCore.QRect(x, 455, w, h))
		else:
			self.anim.setEndValue(QtCore.QRect(x, 495, w, h))
		self.anim.start()

	def eventFilter(self, object, event):
		if event.type() == QEvent.Enter:
			self.move_animation(object)
			return True
		elif event.type() == QEvent.Leave:
			self.move_animation(object, False)
		return False

	def empty_layout(self):

		for x in range(self.vbox.count()):
			self.vbox.itemAt(0).widget().close()
			self.vbox.takeAt(0)

		self.task_block_list = []

	def update_number_labels(self):
		self.active_tasks_label.setText("Active Tasks\n"+str(self.ac))
		self.completed_label.setText("Completed\n"+str(self.comc))
		self.overdue_label.setText("Overdue\n"+str(self.oc))

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.Tasks_head_label.setText(_translate("MainWindow", "Tasks"))
		self.add_task_label.setText(_translate("MainWindow", "Add Task"))
		self.date_select_combox.setItemText(0, _translate("MainWindow", "Today"))
		self.date_select_combox.setItemText(1, _translate("MainWindow", "Tomorrow"))
		self.date_select_combox.setItemText(2, _translate("MainWindow", "Select Date"))
		self.sub_select_combox.setItemText(0, _translate("MainWindow", "All"))
		self.sub_select_combox.setItemText(1, _translate("MainWindow", "Physics"))
		self.sub_select_combox.setItemText(2, _translate("MainWindow", "Chemistry"))
		self.sub_select_combox.setItemText(3, _translate("MainWindow", "Maths"))
		self.sub_select_combox.setItemText(4, _translate("MainWindow", "CS"))
		self.sub_select_combox.setItemText(5, _translate("MainWindow", "Biology"))
		self.priority_select_combox.setItemText(0, _translate("MainWindow", "All"))
		self.priority_select_combox.setItemText(1, _translate("MainWindow", "Low"))
		self.priority_select_combox.setItemText(2, _translate("MainWindow", "Medium"))
		self.priority_select_combox.setItemText(3, _translate("MainWindow", "High"))

		for i, tb in enumerate(self.task_block_list):
			tb.retranslateUi()

	def save_dict(self):
		td = {}
		c = 0
		for x in range(len(tasks_dict)):
			if tasks_dict[str(x)]["checked"] == "F":
				td[str(c)] = tasks_dict[str(x)]
				c += 1
		with open("data/tasks.json", 'r+') as task_file:
			json.dump(td, task_file)




if __name__ == "__main__":
	import sys

	app = QtWidgets.QApplication(sys.argv)

	font_db = QtGui.QFontDatabase()
	font_id = font_db.addApplicationFont("Baloo2-Regular.ttf")
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui.retranslateUi(MainWindow)

	with open('data/tasks.json') as task_file:
		tasks_dict = json.load(task_file)
		ui.sort_tasks()

	ui.retranslateUi(MainWindow)
	MainWindow.setWindowTitle("Goals!")
	MainWindow.setWindowIcon(QtGui.QIcon("logo.png"))
	MainWindow.show()
	app.exec_()
	sys.exit(ui.save_dict())
