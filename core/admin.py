from django.contrib import admin
from core.models import *

# Register your models here.

class InlineSpec(admin.TabularInline):
	extra = 1
	model = Spec

class ProjecteAdmin(admin.ModelAdmin):
	inlines = [ InlineSpec ]

class SprintAdmin(admin.ModelAdmin):
	list_display=["projecte","data_inici","data_final","hores"]

class SpecAdmin(admin.ModelAdmin):
	list_display=["descripcio","projecte","sprint","developer"]

admin.site.register(Projecte,ProjecteAdmin)
admin.site.register(Sprint,SprintAdmin)
admin.site.register(Spec,SpecAdmin)