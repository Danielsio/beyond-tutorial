from django.contrib import admin
from django.urls import path
from msgboard import views as msgboard_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', msgboard_views.board, name='board')
]