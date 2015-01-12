from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from models import Commit, Entity, Change

class AdminCommit(ModelAdmin):
	list_display = ('snapshot', 'commited')

admin.site.register(Commit, AdminCommit)

class AdminEntity(ModelAdmin):
	list_display = ('code', 'isPublic', 'typeOfEntity')

admin.site.register(Entity, AdminEntity)

class AdminChange(ModelAdmin):
	list_display = ('getCommit', 'getEntity', 'desc', 'isBugFix')

admin.site.register(Change, AdminChange)