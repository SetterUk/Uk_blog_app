from django import forms
from .models import Post

choices = [
    ('DSA', 'DSA'),
    ('Machine Learning', 'Machine Learning'),
    ('Competitive Programming', 'Competitive Programming'), # Corrected this line
    ('General', 'General'),
    ('Web Development', 'Web Development'),
    ('Data Science', 'Data Science'),
    ('Artificial Intelligence', 'Artificial Intelligence')
]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author','category', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }