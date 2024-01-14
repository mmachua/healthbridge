
from django.contrib import admin

from .models import Contact, Privacy , Terms
#from django.contrib.gis import admin
from .models import Post, Homepage, Aboutpage, Newsletter
from .models import Contact
# Register your models here.
from django.contrib import admin
from .models import Aboutpage, Aboutpagee
#admin.site.register(Post)
#admin.site.register(Homepage)
#admin.site.register(Aboutpage)
#admin.site.register(Newsletter)
#admin.site.register(Rental)
from django.contrib import admin

#admin.site.register(Coordenadas)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post']
    search_fields = ['post']


@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    list_display = ['title', 'title1']
    search_fields = ['title', 'title1']



class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','content','user']
admin.site.register(Contact, ContactAdmin)


class PrivacyAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Privacy, PrivacyAdmin)


class TermsAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Terms, TermsAdmin)



class AboutpageeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'content', 'ourvision', 'ourmission')
    list_filter = ('title',)

    fieldsets = (
        ('Main Information', {
            'fields': ('title', 'content', 'image', 'image1')
        }),
        ('Our Vision and Mission', {
            'fields': ('ourvision', 'ourmission')
        }),
        ('Expert Team', {
            'fields': ('expertteam', 'teammember1', 'teammember2', 'teammember3')
        }),
        ('Community Engagement', {
            'fields': ('communityengagement', 'communityimage')
        }),
        ('Quality and Safety', {
            'fields': ('qualityandsafety',)
        }),
        ('Your Trusted Partner', {
            'fields': ('yourtrusted',)
        }),
    )

admin.site.register(Aboutpagee, AboutpageeAdmin)
