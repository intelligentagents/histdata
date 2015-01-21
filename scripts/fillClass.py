import django
django.setup()
from core.models import Entity

entities = Entity.objects.all()

for e in entities:
	cn = 'None'
	if e.typeOfEntity == 'p':
		cn = ''
	elif e.typeOfEntity == 'c':
		cn = e.code	
	if e.typeOfEntity == 'm':
		if '(' in e.code:
			if '.' in e.code.split('(')[-1]:
				cn = '.'.join(e.code.split('.')[:-2])
			else:
				cn = '.'.join(e.code.split('.')[:-1])
		else:
			cn = '.'.join(e.code.split('.')[:-1])
	Entity.objects.filter(code=e.code).update(className=cn)
		

