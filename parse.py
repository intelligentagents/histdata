import os
import django
django.setup()
from platform_sdk.models import Commit, Entity, Change, ENTITY_CHOICES, CHANGE_CHOICES
from platform_sdk.utils import getType, formatDate, getState

def insertCommit(snapshot, commited):	
	c, c_created = Commit.objects.get_or_create(snapshot=snapshot, commited=formatDate(commited))		

def insertEntity(code, isPublic, typeOfEntity):	
	e = Entity(code=code, isPublic=isPublic, typeOfEntity=getType(typeOfEntity, ENTITY_CHOICES))
	try:
		Entity.objects.get(code=code, isPublic=isPublic)
	except:
		e.save()

def insertChange(idCommit, idEntity, isPublic, desc, isBugFix):
	c = Commit.objects.get(snapshot=idCommit)
	e = Entity.objects.get(code=idEntity, isPublic=isPublic)
	ch, ch_created = Change.objects.get_or_create(commit_obj=c, entity_obj=e, desc=getType(desc, CHANGE_CHOICES), isBugFix=getState(isBugFix))

with open('platform_sdk/platform-sdk.csv', 'r') as f:
	next(f)
	for line in f:
		line = line.split(';')
		p = getState(line[4])
		insertCommit(line[0], line[1])	
		insertEntity(line[5], p, line[3])
		insertChange(line[0], line[5], p, line[6].rstrip(os.linesep), line[2])