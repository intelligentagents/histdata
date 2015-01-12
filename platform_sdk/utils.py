from datetime import datetime

def formatDate(dateCommit):	
	if not isinstance(dateCommit, str):
		dateCommit = dateCommit.strftime('%Y-%m-%d %H:%M:%S')
	dateCommit = ' '.join(dateCommit.split(' ')[:2])
	return datetime.strptime(dateCommit, '%Y-%m-%d %H:%M:%S')
	
def getState(state):
	if state.lower() == 'true':
		return True
	return False

def getType(description, choices):
	for choice in choices:
		if choice[1] in description:
			return choice[0]
	return 'n'