from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "Benjour Admin"  # Title at the top
admin.site.site_title = "Benjour Admin Portal"         # Title for the browser tab
admin.site.index_title = "Welcome to My Benjour Admin Dashboard"  # Subtitle on the homepage

admin.site.register(JournalName)
admin.site.register(Volume)
admin.site.register(Issue)
admin.site.register(Paper)


