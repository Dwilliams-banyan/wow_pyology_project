from django.forms import ModelForm
from django import forms

from whatToDad_app.models import Post, Activity, ActivityComments, Author, Topic, PostComments

class AuthorForm(ModelForm):
    class Meta:
        model= Author
        fields=['first_name', 'last_name']
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields =['title','author','content']

class PostCommentForm(ModelForm):

    class Meta:
        model = PostComments
        fields = ['content']

    def __init__(self, *args, **kwargs):
        post = kwargs.pop('post_object')
        super().__init__(*args, **kwargs)

        self.instance.post = post
class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['detail', 'min_age', 'max_age', 'addressNumber', 'addressStreet', 'city', 'state', 'zip', 'author']
        widgets ={
            'detail': forms.Textarea(attrs={'class': 'form-control'}),
            'min_age': forms.TextInput(attrs={'class': 'form-control'}),
            'max_age': forms.TextInput(attrs={'class': 'form-control'}),
            'addressNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'addressStreet': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }
class ActivityCommentForm(ModelForm):

    class Meta:
        model = ActivityComments
        fields = ['content']

    def __init__(self, *args, **kwargs):
        activity = kwargs.pop('activity_object')
        super().__init__(*args, **kwargs)

        self.instance.activity = activity

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields =['name']

    def save(self, post, *args, **kwargs):
        topic_name = self.data['name']
        self.fields['name'].label=''

        try:
            topic = Topic.objects.get(name=topic_name)
        except Topic.DoesNotExist:
            topic = Topic.objects.create(name=topic_name)
            post.topics.add(topic)