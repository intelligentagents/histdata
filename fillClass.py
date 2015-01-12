import os
import django
django.setup()
from platform_sdk.models import Entity, ENTITY_CHOICES
from platform_sdk.utils import getType

entities = Entity.objects.all()

for e in entities:
	cn = 'None'
	if e.typeOfEntity == 'p':
		cn = e.code.split('.')[-2].split('/')[-1]
	elif e.typeOfEntity == 'c':
		cn = e.code.split('.')[-1]	
	if e.typeOfEntity == 'm':
		if '(' in e.code:
			if '.' in e.code.split('(')[-1]:
				cn = e.code.split('.')[-3]
			else:
				cn = e.code.split('.')[-2]
		else:
			cn = e.code.split('.')[-2]
	Entity.objects.filter(code=e.code).update(className=cn)
		

