import json
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from task_manager_ui import Ui_MainWindow
from task_manager_ui import task_block

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.retranslateUi(MainWindow)

with open('data/tasks.json') as task_file:
	tasks_dict = json.load(task_file)
	ui.sort_tasks(tasks_dict)

ui.retranslateUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
