from django.shortcuts import render, redirect
from django.views.generic import ListView
from whatToDad_app.models import Post, Author, Activity, ActivityComments
from django.views import View
from whatToDad_app.forms import PostForm, ActivityForm, ActivityCommentForm



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
        post_form = PostForm()

        html_data = {
            'form': post_form
        }

        return render(
            request=request,
            template_name='forum.html',
            context= html_data
        )

    def post(self, request):
        post_form = PostForm(request.POST)
        post_form.save()

        return redirect('home')

class ActivityPage(View):
    def get(self, request):
        activities = Activity.objects.all()
        activity_form = ActivityForm()

        activity_comments = ActivityComments.objects.all()
        activity_comment_form = ActivityCommentForm()

        # print('activities', activities)
        # print('activity_comments', activity_comments)

        html_data = {
            'activities': activities,
            'form': activity_form,
            'activity_comments': activity_comments,
            'activity_comment_form': activity_comment_form
        }

        return render(
            request=request,
            template_name='activity.html',
            context= html_data
        )

    def post(self, request):
        if request.method == 'POST': 
             activity_form = ActivityForm(request.POST) 
             activity_form.is_valid()
             activity_form.save() 
             
        activities = Activity.objects.all()

        activity_comments = ActivityComments.objects.all()
        activity_comment_form = ActivityCommentForm()

        html_data = {
            'activities': activities,
            'form': activity_form,
            'activity_comments': activity_comments,
            'activity_comment_form': activity_comment_form
        }

        return render(
            request=request,
            template_name='activity.html',
            context= html_data
        )

        
class ActivityDetailView(View):
    def get(self, request, activity_id):
        activity = Activity.objects.get(id=activity_id)
        # come back to look at the filter method
        activity_comments = ActivityComments.objects.filter(activity_id=activity_id)
        
        html_data={
            'activity': activity,
            'activity_comment_list': activity_comments
        }

        return render(
            request=request,
            template_name='activity_detail.html',
            context= html_data
        )

    def post(self, request, activity_id):
        activity = Activity.objects.get(id=activity_id)
        activity_comment_form = ActivityCommentForm(request.POST)