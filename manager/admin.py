from django.contrib import admin
from .models import Lagou

# Register your models here.
@admin.register(Lagou)
class LagouAdmin(admin.ModelAdmin):
    list_display = ('url', 'company', 'position', 'minimum_wage', 'maximum_wage', 'location', 'minimum_experience',
                    'maximum_experience', 'education_requirements', 'type', 'address', 'publish_time', 'status',
                    'crawl_created_time')

