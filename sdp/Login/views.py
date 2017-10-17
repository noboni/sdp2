from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.views.generic import TemplateView,UpdateView
from .forms import LoginForm
from .models import Student
from django.template import loader

def index (request):
    return render_to_response('signup.html')


def index2 (request):
    return render_to_response('signin.html')


class LoginRequest(TemplateView):
    form_class = LoginForm
    template_name = 'signin.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name, {'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():

            name = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password')

            myTable = Student.objects.all();
            template = loader.get_template('profile.html')
            for lala in myTable :
                if lala.name == name :
                    if lala.password==password :
                        print(name)
                        print(password)
                        context = {
                            'student': lala,

                        }
                        return HttpResponse(template.render(context,request))

        return render(request, self.template_name, {'form': form})

class UpdateProfile(UpdateView):
        model = Student
        fields = ['name', 'user_id', 'mail_id', 'dob', 'batch', 'profile_pic']