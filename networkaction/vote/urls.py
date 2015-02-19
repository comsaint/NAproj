from django.conf.urls import patterns, url

from vote import views

# urlpatterns = patterns('',
#     # ex: /vote/
#     url(r'^$', views.index, name='index'),
#     # ex: /vote/5/
#     url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
#     # ex: /vote/5/results/
#     url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
#     # ex: /vote/5/vote/
#     url(r'^(?P<question_id>\d+)/voting/$', views.voting, name='voting'),
# )

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/voting/$', views.voting, name='voting'),
)