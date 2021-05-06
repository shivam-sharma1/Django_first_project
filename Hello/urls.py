from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "Ice cream Admin"
admin.site.site_title = "ice cream Admin Portal"
admin.site.index_title = "Welcome to Ice-cream Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
]
