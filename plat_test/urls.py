"""plat_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
# from django.contrib.auth.views import logout
from first_app.views import index,upload,index_register,index_login,softwares,services,software_info

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^index/', index, name="index"),
    url(r'^upload/', upload, name="upload"),
    url(r'^softwares/',softwares, name="softwares"),
    url(r'^software_info/',software_info, name="software_info"),
    url(r'^services/',services, name="services"),
    url(r'^register/$', index_register, name="register"),
    url(r'^login/$', index_login, name="login"),
    # url(r'^logout/', logout, {'next_page': '/index'}, name="logout")
]
