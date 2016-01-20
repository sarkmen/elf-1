from django import forms
from .models import Store, Review, Comment


class StoreForm(forms.ModelForm):

    class Meta:
        model = Store
        fields = ('name', 'address', 'tel', 'photo', 'website', 'intro', 'hours', 'area', 'sub_area', 'category', 'sub_category', )





class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('user_rating', 'content', 'photo', 'n_like', )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', )