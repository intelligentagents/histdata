from django.db import models
from utils import getType, formatDate, getState
from datetime import datetime

class Commit(models.Model):
	snapshot = models.CharField(max_length=100, primary_key=True, unique=True)
	commited = models.DateTimeField()

NONE = 'n'
	
ENTITY_METHOD = 'm'
ENTITY_CLASS = 'c'
ENTITY_SOURCE_PATH = 'p'
ENTITY_CHOICES = (
	(ENTITY_METHOD, 'METHOD'),
	(ENTITY_CLASS, 'CLASS'),
	(ENTITY_SOURCE_PATH, 'SOURCE_PATH'),
	(NONE, 'NONE'),
)
class Entity(models.Model):
	code = models.CharField(max_length=255)
	isPublic = models.BooleanField(default=True)
	typeOfEntity = models.CharField(
		max_length=1,
		default=ENTITY_METHOD,
		choices=ENTITY_CHOICES,
		)

	class Meta:
		unique_together = (('code', 'isPublic'),)
		
ADDED = 'a'
BODY_MODIFIED = 'b'
CHANGED_RETURN_TYPE = 'c'
DELETED = 'd'
INCREASED_VISIBILITY = 'i'
PARAMETER_ADDED = 'p'
PARAMETER_REMOVED = 'q'
REMOVED_THROWN_EXCEPTION = 'u'
RENAMED = 'r'
REDUCED_VISIBILITY = 'v'
THROWS_NEW_EXCEPTIONS = 't'
CHANGE_CHOICES = (
	(ADDED, 'ADDED'),
	(BODY_MODIFIED, 'BODY_MODIFIED'),
	(CHANGED_RETURN_TYPE, 'CHANGED_RETURN_TYPE'),
	(DELETED, 'DELETED'),
	(INCREASED_VISIBILITY, 'INCREASED_VISIBILITY'),
	(PARAMETER_ADDED, 'PARAMETER_ADDED'),
	(PARAMETER_REMOVED, 'PARAMETER_REMOVED'),
	(REMOVED_THROWN_EXCEPTION, 'REMOVED_THROWN_EXCEPTION'),
	(RENAMED, 'RENAMED'),
	(REDUCED_VISIBILITY, 'REDUCED_VISIBILITY'),
	(THROWS_NEW_EXCEPTIONS, 'THROWS_NEW_EXCEPTIONS'),
	(NONE, 'NONE'),
)
class Change(models.Model):
	commit_obj = models.ForeignKey(Commit)
	entity_obj = models.ForeignKey(Entity)
	desc = models.CharField(
		max_length=1,
		default=ADDED,
		choices=CHANGE_CHOICES,
		)
	isBugFix = models.BooleanField(default=True)
	
	class Meta:
		unique_together = (('commit_obj', 'entity_obj', 'desc'),)
		
	def getCommit(self):
		return self.commit_obj.snapshot
		
	def getEntity(self):
		return self.entity_obj.code