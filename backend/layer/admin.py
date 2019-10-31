from django.contrib import admin
from .models import Layer  # add this

# This is still just a test stub:
# username: danielshu
# password: password

class LayerAdmin(admin.ModelAdmin):  # add this
    list_display = ('title', 'description', 'year', 'area', 'latitude')  # add this

# Register your models here.
admin.site.register(Layer, LayerAdmin)  # add this
# Register your models here.
