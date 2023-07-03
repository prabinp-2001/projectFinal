"""education URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url('accounts/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('',views.base,name='base'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('course/',views.course,name='course'),
    path('login1/',views.user_login,name='login1'),
    path('signup/',views.signup,name='signup'),
    path('logout1/',views.logout1,name='logout1'),
    path('profile/',views.profile,name='profile'),
    path('form1/',views.form1,name='form1'),
    path('edit/<int:p>',views.edit_profile,name='edit_profile'),
    path('popup/',views.popup,name='popup'),

]

if (settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
