import json

with open('data/tasks.json') as task_file:
	tasks_dict = json.load(task_file)