from django.contrib import admin
from .models import Todo  # add this

# This is still just a test stub:
# username: danielshu
# password: password

class TodoAdmin(admin.ModelAdmin):  # add this
    list_display = ('title', 'description', 'completed')  # add this

# Register your models here.
admin.site.register(Todo, TodoAdmin)  # add this
# Register your models here.
