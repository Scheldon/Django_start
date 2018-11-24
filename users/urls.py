from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^abc/$',views.Users.as_view()),
    url(r'^users/$', views.CommentView.as_view()),
    url(r'^user/$', views.CreateCommentView.as_view()),
]