import json
from task import Task
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from task_manager_ui import Ui_MainWindow
from task_manager_ui import task_block

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
# ui.add_task_blocks()
# ui.task_block_list.append(task_block(ui, {"title":"a", "priority":"b", "date":"c", "subject":"d"}))
# ui.task_block_list.append(task_block(ui, {"title":"e", "priority":"f", "date":"g", "subject":"h"}, 1))

with open('data/tasks.json') as task_file:
	tasks_dict = json.load(task_file)
	ui.update_task_blocks(tasks_dict)

# ui.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 771, 311))
# ui.scrollArea.setGeometry(QtCore.QRect(20, 120, 800, 311))
# ui.scrollArea.setWidget(ui.scrollAreaWidgetContents)
ui.retranslateUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
