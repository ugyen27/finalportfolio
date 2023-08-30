from django.contrib import admin
from .models import Contact
# Register your models here.
admin.site.site_header = "Ugyen portfolio"
admin.site.site_title = "UgyenAdmin"
admin.site.index_title = "Manage Projects"

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','project','message')
    search_fields = ('name','project')

admin.site.register(Contact,ContactAdmin)




