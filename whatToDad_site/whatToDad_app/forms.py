from django.forms import ModelForm

from whatToDad_app.models import Post
class PostForm(ModelForm):

    class Meta:
        model = Post
        fields =['title', 'slug','author','content']