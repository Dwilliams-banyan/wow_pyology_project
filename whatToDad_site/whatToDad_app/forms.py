from django.forms import ModelForm

from whatToDad_app.models import Post, Activity, ActivityComments
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields =['title', 'slug','author','content']
class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['detail', 'min_age', 'max_age', 'addressNumber', 'addressStreet', 'city', 'state', 'zip', 'user']
class ActivityCommentForm(ModelForm):

    class Meta:
        model = ActivityComments
        fields = ['content']