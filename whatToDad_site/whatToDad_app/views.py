from django.shortcuts import render, redirect
from django.views.generic import ListView
from whatToDad_app.models import Post
from django.views import View



class PostList(ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'


class PostDetail(View):
    def get(self,request):
        return render(
            model = Post,
            template_name = 'post_detail.html'
        )

class ForumBoard(View):
    def get(self, request):
        return render(
            request=request,
            template_name='forum.html',
            context= {}
        )