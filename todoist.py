import requests
import json

def get_todoist():

	"""
	Exatracts all incomplete todos from todoist
	and saves it to todos.json
	"""

	url = 'https://beta.todoist.com/API/v8/tasks'
	token = '***********************************'

	todo_list = []
	todos = requests.get(url, headers={ "Authorization": "Bearer %s" % token }).json()
	for todo in todos:
		if todo['completed'] == False:
			temp = {}
			temp['content'] = todo['content']
			temp['date'] = todo['due']['string']
			todo_list.append(temp)

	return todo_list

# Save feeds to file
todos = get_todoist()
my_file = open('todos.json', 'w')
my_file.write(json.dumps(todos))
my_file.close()
