from django.shortcuts import render, redirect
from django.views.generic import ListView
from whatToDad_app.models import Post, Author
from django.views import View
from whatToDad_app.forms import PostForm



class PostList(ListView):
    queryset = Post.objects.order_by('-created_on')[:3]
    template_name = 'index.html'


class PostDetail(View):
    def get(self,request):
        return render(
            model = Post,
            template_name = 'post_detail.html'
        )

class ForumBoard(View):
    def get(self, request):
        post_form = PostForm()

        html_data = {
            'form': post_form,
            'post_list': Post.objects.order_by('-created_on').all()
        }
        print(html_data)

        return render(
            request=request,
            template_name='forum.html',
            context= html_data
        )

    def post(self, request):
        post_form = PostForm(request.POST)
        post_form.save()

        return redirect('home')