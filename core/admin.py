from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from models import Developer, Commit, Entity, Change

class AdminDeveloper(ModelAdmin):
	list_display = ('name', )
	
admin.site.register(Developer, AdminDeveloper)

class AdminCommit(ModelAdmin):
	list_display = ('snapshot', 'commited', 'developer')

admin.site.register(Commit, AdminCommit)

class AdminEntity(ModelAdmin):
	list_display = ('code', 'isPublic', 'className', 'typeOfEntity')

admin.site.register(Entity, AdminEntity)

class AdminChange(ModelAdmin):
	list_display = ('commit_obj', 'entity_obj', 'desc', 'isBugFix')

admin.site.register(Change, AdminChange)
