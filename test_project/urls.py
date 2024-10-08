"""
URL configuration for test_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from test_app import views
# from django.conf.urls.static import static
# from django.conf import settings

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.home),
#     path('home',views.home),
#     path('register',views.register),
#     path('index',views.index),
#     path('logout_view',views.logout)
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# from django.urls import path
# from test_app.views import register, user_login, user_logout

# urlpatterns = [
#     # path('',register,name='home'),
#     path('register/', register, name='register'),
#     path('login/', user_login, name='login'),
#     path('logout/', user_logout, name='logout'),
# ]
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('test_app.urls')),
    path('', include('test_app.urls')),  # Example for a home app if you have one
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

