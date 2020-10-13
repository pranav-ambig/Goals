import json
from constants import tasks_dict
# from task_manager import tasks_dict

class Task:

	def __init__(self, name, date, priority, task_id):
		self.name = name
		self.date = date
		self.priority = priority
		self.task_id = task_id
		self.done = False

	def save(self):
		tasks_dict[self.task_id] = self.name, self.date, self.priority, self.done

		with open('data/tasks.json', 'w') as task_file:
			json.dump(tasks_dict, task_file)

			