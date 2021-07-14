"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.conf import settings

from accounts import views, AdminView, MemberView
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('demo/',views.showDemoPage),
    # path('accounts/',include('django.contrib.auth.urls')),
    # path('login/',views.ShowLoginPage,name="show_login"),#admin login
    # path('get_user_details', views.GetUserDetails),#get admin users
    path('logout_user', views.logout_user,name="logout_user"),
    path('doLogin',views.doLogin,name="do_login"),

    path('admin_home/',AdminView.admin_home,name="admin_home"),
    path('member_home/',MemberView.member_home,name="member_home"),
    

    path('register/',views.do_member_signup,name="do_member_signup"),
    path('login/',views.ShowLoginPage,name="ShowLoginPage"),


    path('', include('nature_club.urls')),
    path('nature_club/blogs/', include('blog.urls')),


] + static(settings.STATIC_URL, documents=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
