from django import forms
from .models import Post
from users.models import Profile
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

class CreateForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
	class Meta:
		model = Post
		fields = ['content']


