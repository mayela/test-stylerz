from django.conf.urls import url, include

from dates.views import create_date_view

urlpatterns = [
    url(r'^crear/', create_date_view),
] 
