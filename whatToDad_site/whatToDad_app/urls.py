from django.urls import path
from whatToDad_app.views import PostList, PostDetail, ForumBoard, ActivityPage, ActivityDetailView

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('activity', ActivityPage.as_view(), name='activity'),
    path('activity/<int:activity_id>', ActivityDetailView.as_view(), name='activity_detail'),
    path('fatherlybonds/', ForumBoard.as_view(), name='forumboard'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]