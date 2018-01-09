from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm,EditProfileForm,FeedbackForm,ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from accounts.models import Feedback1,UserProfile
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request,'accounts/login.html')

def about(request):
    return render(request,'accounts/about.html')



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form = RegistrationForm()


    return render(request,'accounts/reg_form.html',{'form':form})

@login_required
def view_profile(request):
    base = UserProfile.objects.filter(user=request.user)
    args = {'user':request.user,'base':base}
    return render(request,'accounts/profile.html',args)

# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance = request.user)
#         profile = ProfileForm()
#         if form.is_valid():
#             form.save()
#             return redirect('/accounts/profile')
#     else:
#         form = EditProfileForm(instance = request.user)
#         args = {'form': form}
#         return render(request, 'accounts/edit_profile.html', args)



class HomeView(TemplateView):
    template_name = 'accounts/about.html'

    def get(self, request):
        feed = FeedbackForm()
        args = {'feed':feed}
        return render(request, self.template_name,args)


    def post(self,request):
        feed = FeedbackForm
        if request.method == 'POST':
            feed = FeedbackForm(request.POST)
            if feed.is_valid():
                post = feed.save(commit=False)
                post.user = request.user
                post.save()
                text = feed.cleaned_data['text']
                feed = FeedbackForm(request.GET)
                return redirect('/accounts/about')

            return render(request, self.template_name,{'feed': feed,'text':text })

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'accounts/edit_profile.html', {
        'form': form,
        'profile_form': profile_form
    })
