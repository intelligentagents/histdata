from django.db import models
from utils import getType, formatDate, getState
from datetime import datetime

class Developer(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class Commit(models.Model):
	snapshot = models.CharField(max_length=100, primary_key=True, unique=True)
	commited = models.DateTimeField()
	developer = models.ForeignKey(Developer, null=True)
	
	def __unicode__(self):
		return self.snapshot

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
		
	def __unicode__(self):
		return self.code

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

	def get_commits_involving_two_or_more_classes(self):
		filtered_commits = []

		commits = Commit.objects.all()

		for commit in commits:
			changes = Change.objects.filter(commit_obj=commit)
			if self.class_count_from_changes(changes) >= 2:
				filtered_commits.append(commit)

		return filtered_commits

	def calculate_alfa(self): #Blob
		commits = self.get_commits_involving_two_or_more_classes()

		commits_with_class = 0
		commits_without_class = 0

		if not commits:
			return 0

		for commit in commits:
			changes = Change.objects.filter(commit_obj=commit)
			changes_with_this_class = changes.filter(entity_obj__className=self.className).count()
			if not changes_with_this_class:
				commits_with_class += 1
			else:
				commits_without_class += 1

		return (1.0*commits_with_class) / len(commits)



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
