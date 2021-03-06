"""indaba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin


admin.site.site_header = "PyConZim 2017"
admin.site.site_title = "PyComZIm 2017"
admin.site.index_title = "PyConZim 2017"


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('website.urls', namespace='website')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    url(r'^talks/', include('talks.urls', namespace='talks')),
    url(r'^schedule/', include('schedule.urls', namespace='schedule')),
]

