from django.shortcuts import render, redirect
from django.views.generic import ListView
from whatToDad_app.models import Post, Author, Activity, ActivityComments
from django.views import View
from whatToDad_app.forms import PostForm, ActivityForm, ActivityCommentForm

class PostList(ListView):
    queryset = Post.objects.order_by('-created_on')[:3]
    template_name = 'index.html'

class PostDetail(View):
    def get(self,request):
        return render(
            model = Post,
            template_name = 'post_detail.html'
        )

class PostAction(View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        post_form = PostForm(instance=post)

        html_data = {
            'post':post,
            'form':post_form
        }

        return render(
            request,
            template_name = 'post_action.html',
            context= html_data
        )

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)

        if 'delete' in request.POST:
            post.delete()
            return redirect('forumboard')

        elif 'update' in request.POST:
            post_form = PostForm(request.POST, instance=post)
            post_form.is_valid()
            post_form.save()
 
        return redirect('post_action', post_id)

        

class ForumBoard(View):
    def get(self, request):
        post_form = PostForm()
        html_data = {
            'form': post_form,
            'post_list': Post.objects.order_by('-created_on').all()
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
        html_data = {
            'activities': activities,
            'form': activity_form,
        }

        return render(
            request=request,
            template_name='activity.html',
            context= html_data
        )

    def post(self, request):
        activity_form = ActivityForm(request.POST) 
        if activity_form.is_valid():
            activity_form.save() 

        return redirect('activity')

        
class ActivityDetailView(View):
    def get(self, request, activity_id):
        activity = Activity.objects.get(id=activity_id)
        # come back to look at the filter method
        activity_comments = ActivityComments.objects.filter(activity_id=activity_id)
        activity_comment_form = ActivityCommentForm(activity_object=activity)
        activity_form = ActivityForm(instance=activity)    
        html_data={
            'activity': activity,
            'activity_comment_list': activity_comments,
            'comment_form': activity_comment_form,
            'activity_form': activity_form,
        }

        return render(
            request=request,
            template_name='activity_detail.html',
            context= html_data
        )

    def post(self, request, activity_id):
        activity = Activity.objects.get(id=activity_id)
        if 'add' in request.POST:
             activity_comment_form = ActivityCommentForm(request.POST, activity_object=activity) 
             activity_comment_form.is_valid()
             activity_comment_form.save()

        elif 'delete' in request.POST:
            activity.delete()
            return redirect('activity')

        elif 'update' in request.POST:
            activity_form = ActivityForm(request.POST, instance=activity)
            activity_form.is_valid()
            activity_form.save()
 
        return redirect('activity_detail', activity_id)
