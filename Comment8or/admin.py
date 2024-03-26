from django.contrib import admin
class c8admin(admin.AdminSite):
    title_header = 'c8admin'
    site_header = 'c8admin'
    index_title = 'c8admin'
    logout_template = 'comment8or/logged_out.html'

admin_site = c8admin(name='comment8or')