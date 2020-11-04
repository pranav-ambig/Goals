from PyQt5 import QtCore, QtGui, QtWidgets
import datetime


class Ui_Dialog(QtWidgets.QDialog):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(277, 212)
		self.dict = None
		self.Dialog = Dialog
		self.formLayoutWidget = QtWidgets.QWidget(Dialog)
		self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 261, 141))
		self.formLayoutWidget.setObjectName("formLayoutWidget")
		self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
		self.formLayout.setContentsMargins(0, 0, 0, 0)
		self.formLayout.setObjectName("formLayout")
		self.label = QtWidgets.QLabel(self.formLayoutWidget)
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
		self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
		self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		self.label_3.setFont(font)
		self.label_3.setObjectName("label_3")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
		self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		self.label_4.setFont(font)
		self.label_4.setObjectName("label_4")
		self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
		self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		self.lineEdit.setFont(font)
		self.lineEdit.setObjectName("lineEdit")
		self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
		self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		self.dateEdit.setFont(font)
		self.dateEdit.setObjectName("dateEdit")

		cd = str(datetime.date.today())
		cd = cd.split('-')
		cd = QtCore.QDate(int(cd[0]), int(cd[1]), int(cd[2]))

		self.dateEdit.setDate(cd)
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
		self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		self.comboBox.setFont(font)
		self.comboBox.setObjectName("comboBox")
		self.comboBox.addItem("")
		self.comboBox.addItem("")
		self.comboBox.addItem("")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
		self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		self.comboBox_2.setFont(font)
		self.comboBox_2.setObjectName("comboBox_2")
		self.comboBox_2.addItem("")
		self.comboBox_2.addItem("")
		self.comboBox_2.addItem("")
		self.comboBox_2.addItem("")
		self.comboBox_2.addItem("")
		self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
		self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(50, 160, 166, 28))
		font = QtGui.QFont("Baloo2")
		font.setFamily("Baloo2")
		self.buttonBox.setFont(font)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
		self.buttonBox.setObjectName("buttonBox")

		self.buttonBox.accepted.connect(self.save_btn)
		self.buttonBox.rejected.connect(self.Dialog.close)

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def save_btn(self):
		title = self.lineEdit.text()
		date = self.dateEdit.date()
		date = '/'.join((str(date.day()), str(date.month()), str(date.year())))
		priority = str(self.comboBox.currentText())
		subject  = str(self.comboBox_2.currentText())
		
		title = 'Untitled' if title == '' else title

		self.dict = {"title":title, "date":date, "priority":priority, "subject":subject, "checked": "F"}
		self.Dialog.close()

	def get_details(self):
		return self.dict

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Add Task"))
		self.label.setText(_translate("Dialog", "Title:"))
		self.label_2.setText(_translate("Dialog", "Date:"))
		self.label_3.setText(_translate("Dialog", "Priority:"))
		self.label_4.setText(_translate("Dialog", "Subject:"))
		self.comboBox.setItemText(0, _translate("Dialog", "Low"))
		self.comboBox.setItemText(1, _translate("Dialog", "Medium"))
		self.comboBox.setItemText(2, _translate("Dialog", "High"))
		self.comboBox_2.setItemText(0, _translate("Dialog", "Physics"))
		self.comboBox_2.setItemText(1, _translate("Dialog", "Chemistry"))
		self.comboBox_2.setItemText(2, _translate("Dialog", "Maths"))
		self.comboBox_2.setItemText(3, _translate("Dialog", "CS"))
		self.comboBox_2.setItemText(4, _translate("Dialog", "Biology"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)

	font_db = QtGui.QFontDatabase()
	font_id = font_db.addApplicationFont("Baloo2-Regular.ttf")

	Dialog = QtWidgets.QDialog()
	ui = Ui_Dialog()
	ui.setupUi(Dialog)
	Dialog.show()
	sys.exit(app.exec_())
