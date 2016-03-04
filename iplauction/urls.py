from django.conf.urls import url
from iplauction import views


urlpatterns = [
    url(r'^teams/$', views.team_list),
    url(r'^players/$', views.player_list),
]
