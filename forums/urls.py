from django.urls import path
from . import views
from .views import PostAdd, PostDeleteView

urlpatterns = [
    path('', views.TopicList.as_view(), name='homepage'),
    path('topic/<str:name>/', views.TopicDetail.as_view(), name='topic_detail'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('add-post/', PostAdd.as_view(), name='add_post'),
    path('edit-post/<slug:slug>/', views.PostEdit.as_view(), name='edit_post'),
    path('delete-post/<slug:slug>/', PostDeleteView, name='delete_post'),
]
