from django.contrib import admin
from django.urls import path
from myApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Issue_book.html', views.issue_book, name = 'issue_book'),
]
