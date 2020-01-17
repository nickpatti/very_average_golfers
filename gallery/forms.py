from django import forms
from PIL import Image
from comments.models import ImageComments


class ImageFileInput(forms.ClearableFileInput):

    def validate(self, value):
        return super.validate(value)


class ImageCreateForm(forms.Form):
    data = forms.FileField(widget=forms.FileInput(attrs={'multiple': True}))

    class Meta:
        model = Image
        fields = ['data']


class ImageCommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), label="New Comment")

    class Meta:
        model = ImageComments
        fields = ('content', )
