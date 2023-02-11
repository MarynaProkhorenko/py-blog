from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Commentary


class CommentCreateForm(LoginRequiredMixin, forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        labels = {"content": "Add your comment:"}