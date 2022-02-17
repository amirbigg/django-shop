from django.shortcuts import render
from django.views import View
from .forms import UserRegistrationForm


class UserRegisterView(View):
	form_class = UserRegistrationForm

	def get(self, request):
		form = self.form_class
		return render(request, 'accounts/register.html', {'form':form})

	def post(self, request):
		pass
