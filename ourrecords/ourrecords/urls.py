"""ourrecords URL Configuration

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
from posts import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.RecordListView.as_view(), name="records_list"),
    url(r'^(?P<pk>\d+)/$', views.RecordDetailView.as_view(), name="record_detail"),
    url(r'^(?P<pk>\d+)/update/$', views.RecordUpdateView.as_view(), name="record_update"),
	# url(r'^(?P<pk>\d+)/delete/$', views.RecordDeleteView.as_view(), name='record_delete'),
	url(r'^create/$', views.RecordCreateView.as_view(), name="records_create"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)






