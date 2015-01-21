from django.db import models
from utils import getType, formatDate, getState
from datetime import datetime

class Commit(models.Model):
	snapshot = models.CharField(max_length=100, primary_key=True, unique=True)
	commited = models.DateTimeField()

NONE = 'n'

ENTITY_METHOD = 'm'
ENTITY_CLASS = 'c'
ENTITY_SOURCE_FILE = 'p'
ENTITY_CHOICES = (
	(ENTITY_METHOD, 'METHOD'),
	(ENTITY_CLASS, 'CLASS'),
	(ENTITY_SOURCE_FILE, 'SOURCE_FILE'),
	(NONE, 'NONE'),
)
class Entity(models.Model):
	code = models.CharField(max_length=255)
	isPublic = models.BooleanField(default=True)
	className = models.CharField(max_length=100)
	typeOfEntity = models.CharField(
		max_length=1,
		default=ENTITY_METHOD,
		choices=ENTITY_CHOICES,
		)

	class Meta:
		unique_together = (('code', 'isPublic'),)

	def class_count_from_changes(self, changes):
		classes = []
		for change in changes:
			if change.entity_obj.className and (change.entity_obj.className not in classes):
				classes.append(change.entity_obj.className)
		return len(classes)

	def calculate_beta(self): #Feature Envy for Methods
		if not self.typeOfEntity == ENTITY_METHOD:
			return 0

		commits = Commit.objects.filter(change__entity_obj=self)
		beta = 0
		external_rate = 0
		internal_rate = 0
		for commit in commits:
			changes = Change.objects.filter(commit_obj=commit)
			if changes.count() <= 1:
				continue

			if self.class_count_from_changes(changes) < 2: #verifica quantas classes estao envolvidas
				continue

			external_changes = changes.filter(entity_obj__className=self.className).count()
			internal_changes = changes.exclude(entity_obj__className=self.className).count()



			if external_changes != internal_changes:
				if external_changes > internal_changes:
					external_rate += 1
				else:
					internal_rate += 1


		return 1.0*external_rate / (internal_rate + external_rate)

	def commit_class_dict(self):
		commit_classes = {}

		commits = Commit.objects.all()

		for commit in commits:			
			if commit not in commit_classes:
				commit_classes[commit] = []
				changes = Change.objects.filter(commit_obj=commit)
				for change in changes:
					if change.entity_obj.className not in commit_classes[commit]:
						commit_classes[commit].append(change.entity_obj.className)

			if len(commit_classes[commit]) < 2: del commit_classes[commit]

		return commit_classes

	def calculate_alfa(self): #Blob
		commit_qta = 0
		commits = self.commit_class_dict()
		for commit in commits:
			if self.className in commits[commit]:
				commit_qta += 1

		return (commit_qta*100.0)/len(commits) #retorna valor percentual do alfa, calculo ainda nao esta correto


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

	def get_commit(self):
		return self.commit_obj.snapshot

	def get_entity(self):
		return self.entity_obj.code
