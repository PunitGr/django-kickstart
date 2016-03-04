from django.conf.urls import url
from iplauction import views


urlpatterns = [
    url(r'^teams/$', views.team_list),
    url(r'^players/$', views.player_list),
    url(r'^team/(?P<t_id>[0-9]+)/$', views.team_details),
]
