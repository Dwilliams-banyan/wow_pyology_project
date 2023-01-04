from django.urls import path
from whatToDad_app.views import PostList, PostDetail, ForumBoard

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('fatherlybonds/', ForumBoard.as_view(), name='forumboard'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]