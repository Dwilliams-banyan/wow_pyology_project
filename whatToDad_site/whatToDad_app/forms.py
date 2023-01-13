from django.forms import ModelForm

from whatToDad_app.models import Post, Activity, ActivityComments, Author

class AuthorForm(ModelForm):
    class Meta:
        model= Author
        fields=['first_name', 'last_name']
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

    def __init__(self, *args, **kwargs):
        activity = kwargs.pop('activity_object')
        super().__init__(*args, **kwargs)

        self.instance.activity = activity