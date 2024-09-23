# from django.urls import path
# from .views import register, user_login, user_logout

# urlpatterns = [
#     path('register/', register, name='register'),
#     path('login/', user_login, name='login'),
#     path('logout/', user_logout, name='logout'),
# ]
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/', include('accounts.urls')),
#     path('', include('home')),  # Example for a home app if you have one
# ]
from django.urls import path
from test_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',user_login,name='login'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('index',index,name='index'),
    path('profile/',profile,name="profile")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
