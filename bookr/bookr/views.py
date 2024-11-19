from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
def is_staff_user(user):
 return user.is_staff
@user_passes_test(is_staff_user)
def profile(request):
 return render(request, 'profile.html')