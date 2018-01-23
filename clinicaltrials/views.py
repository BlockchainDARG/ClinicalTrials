from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, DocumentForm
from django.utils.encoding import smart_str

# from django.contrib.auth.forms import UserCreationForm
import hashlib
import os

from .models import clinicaltrial, file  
# Create your views here.

def index(request):
    all_trials = clinicaltrial.objects.all()
    # template = loader.get_template('clinicaltrials/index.html')
    context = {'all_trials': all_trials }
    return render(request, 'clinicaltrials/index.html', context)

def detail(request, clinicaltrial_id):
    try:
        trial = clinicaltrial.objects.get(pk = clinicaltrial_id)
        # allFiles = file.objects.all(clinicaltrial = clinicaltrial_id) #why doesnt this work?
        allFiles = trial.file_set.all()
    except:
        raise Http404("trial does not exist")
    return render(request, 'clinicaltrials/detail.html', {'trial': trial, 'allFiles': allFiles})

class UserFormView(View):
    form_class = UserForm
    template_name = 'clinicaltrials/registration_form.html'
    
    #display blank form 
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})
        pass

    #process form data
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #return User objects if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('clinicaltrial:index')
        return render(request, self.template_name, {'form' :form})

# Could write this like UserFormView.
# Written differently to serve as an example of more verbose form usage.
def userlogin(request): 
    if request.method == 'GET':
        return render(request, 'clinicaltrials/login.html')
    
    if request.method == 'POST':
        print("AAAAAA", request.POST)
        username = request.POST.get("name", "")
        input_password = request.POST.get("input_password", "") 
        user = authenticate(username=username, password=input_password)
        if user is not None:
            if user.is_active:
                login(request, user)                    
                return redirect('clinicaltrial:index')
        return render(request, 'clinicaltrials/login.html') 

def userlogout(request):
    logout(request)
    all_trials = clinicaltrial.objects.all()
    context = {'all_trials': all_trials }
    return render(request, 'clinicaltrials/index.html', context)

def hash(file):
    string = file.read()
    hash_object = hashlib.sha256(string)
    hex_dig = hash_object.hexdigest()
    return hex_dig

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        
        ##==========================================================
        ##perform hash validation stuff here in blockchain
        
        # print("FFFFFF", request.FILES['data'])
        # print("GGGG", type(request.FILES['data'])) #django.core.files.uploadedfile.InMemoryUploadedFile
        file = request.FILES['data']
        hashString = hash(file)
        print(hashString)
        ##==========================================================

        
        if form.is_valid():
            doc = form.save(commit=False)
            doc.sender = request.user
            doc.filename = request.FILES['data'].name #filename = 'data'?
            # print("AAA", request.FILES)  
            # print("NNNNNNN", doc.filename)
            doc.save()
        return render(request, 'clinicaltrials/index.html', {'all_trials': clinicaltrial.objects.all() })
    else:
        form = DocumentForm()
        return render(request, 'clinicaltrials/model_form_upload.html', {'form': form})
    
def userhome(request):
    ownedFiles = file.objects.all().filter(owner=request.user)
    context = {"ownedFiles" : ownedFiles}
    return render(request, 'clinicaltrials/user_home.html', context)


def download(request, path):
    # print("PPPPP", path)
    # print("PPPPP", path.name)
    # print("OSOSOSOS", os.getcwd())
    file_name = path[path.index("media/") + 6:] #hacky - django appends random string to filename if a file already exists in media with the same name 
    path_to_file = path[path.index("media"):] #get the path of desired file, current directory: /Users/student/Desktop/ButteLab/clinicalnetwork
    response = HttpResponse(open(path_to_file, "rb"), content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    response['X-Sendfile'] = smart_str(path_to_file)
    return response













