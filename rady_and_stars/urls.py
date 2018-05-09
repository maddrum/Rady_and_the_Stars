"""rady_and_stars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import include
from main_app import views
from django.contrib.auth import views as login_view
from . import settings

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'site/', include('main_app.urls')),
    url(r'userportal/', include('user_content.urls')),
    url(r'login/', login_view.LoginView.as_view(template_name='user_content/login.html'), name='user_login'),
    url(r'logout/', login_view.logout, name="logout", kwargs={'next_page': 'index'}),
    url(r'admin/', admin.site.urls),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'__debug__', include(debug_toolbar.urls)),
                  ] + urlpatterns
