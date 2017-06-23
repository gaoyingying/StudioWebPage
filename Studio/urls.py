"""Studio URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from web import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', views.sign_up, name='sign_up'),
    url(r'^login/$', views.sign_in, name='log_in'),
    url(r'^logout/$', views.log_out, name='log_out'),
    url(r'^profile/$', views.user_profile, name='profile'),
    url(r'^user_info/$', views.user_info, name='user_info'),
    url(r'^add_post/$', views.add_post, name='add_post'),
    url(r'^category/$', views.manage_category, name='category'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^del_category/$', views.del_category, name='del_category'),
    url(r'^c/(?P<category_id>\d+)/$', views.index_page, name='category'),
    url(r'^p/(?P<post_id>\d+)/$', views.post_page, name='post'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^posts/$', views.post_manage, name='posts'),
    url(r'^change_info/$', views.change_info, name='change_info'),
    url(r'^$', views.index, name='home'),
]
