"""elf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'legolas.views.index'),
    url(r'^storelist/(?P<pk>[0-9]+)/$', 'legolas.views.storelist', name="storelist"),
    url(r'^store/(?P<pk>[0-9]+)/$', 'legolas.views.a_store', name="a_store"),
    url(r'^store/new/$', 'legolas.views.store_new', name='store_new'),
    url(r'^user/(?P<pk>[0-9]+)/$', 'legolas.views.a_user', name='a_user'),
]
