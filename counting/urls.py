from django.contrib import admin
from django.urls import path,include
from users.views import LoginPage,Logout,RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('login/',LoginPage.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('register/',RegisterView.as_view(),name='register')
]

