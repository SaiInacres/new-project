#from django.contrib.auth import authenticate
from django.db import connection
from django.db.models import query
from django.db.models.base import Model
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
#from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import NewRegistrationForm, NewProjectForm, DocumentForm, DocumentImageForm
#from django.views.generic import ListView
from app.models import New_project, New_registration, Document_details, PostImage
from django.conf import settings
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request = request, template_name="app/hello.html")
""""
def login_request(request):
    if request.method == 'POST':
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:

               # messages.info(request, f'you are now logged in as {username}')
                return redirect('app:sites')
                
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request = request, 
        template_name= "app/login.html", context={'form':form})
"""
@login_required
def site_names(request):
#    query = New_project.objects.all()
    if New_registration.project_name == 'VIKARABAD CSA':
        return redirect('app/user_details_vikarabad.html')
    if New_registration.project_name == 'ALERU CSA':
        return redirect('app/user_details_aleru.html')
    if New_registration.project_name == 'SHADNAGAR CSA':
        return redirect('app/user_details_shadnagar.html')
    if New_registration.project_name == 'BHUTHPUR CSA':
        return redirect('app/user_details_bhuthpur.html')
    if New_registration.project_name == 'MADDUR CSA':
        return redirect('app/user_details_maddur.html')
    return render(request, 'app/sites.html')

@login_required
def new_project(request):
    if request.method == 'POST':
        form = NewProjectForm(data=request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            messages.warning(request, 'Sorry, Something went wrong!', extra_tags='alert alert-warning')
    else:
        form = NewProjectForm() 
    return render(request, 'app/new_project.html', {'form': form})


#@login_required
#class NewSiteView(ListView):
#    queryset = New_project.objects.all()
#    template_name = 'app/sites.html'


@login_required
def new_registration(request):
    if request.method == 'POST':
        form = NewRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Plot Account Was Successfully Created.',
                             extra_tags='alert alert-success')
                            

        else:
            print(form.errors)
            messages.warning(request, 'Sorry, Something went wrong!', extra_tags='alert alert-warning')                     
            
    else:
        form= NewRegistrationForm()
    return render(request, 'app/new_registration.html',  {'form': form})

"""
if you wanted to add new project details create function like below user_details_newproject etc.
add new url in urls.py
create new project html page in templates


RAW QUERY BY USING ID

def user_details_aleru(request):
   farmid = '2'
   query = New_registration.objects.raw("select * from app_new_registration where farm_name_id=%s", [farmid])
   return render(request, 'app/user_details_aleru.html', {'query': query})

"""



@login_required
def user_details(request):
    query = request.GET.get('q', None)
    if query:
        first_name = query.split(' ')[0]
        last_name  = query.split(' ')[0]
        QuerySet = Document_details.objects.filter(Q(plot_no__plot_no__icontains=query) | Q(plot_no__mobile_no__icontains=query) 
                    | Q(plot_no__mail_id__icontains=query) | Q(project_name__project_name__icontains=query)
                    | Q(plot_no__first_name__icontains=first_name) | Q(plot_no__last_name__icontains=last_name)
                    | Q(plot_no__first_name__icontains=last_name) | Q(plot_no__last_name__icontains=first_name))
    return render(request, 'app/user_details.html', {'Queryset': QuerySet})

@login_required
def user_details_vikarabad(request):
    query = Document_details.objects.filter(project_name__project_name='VIKARABAD CSA')
    return render(request, 'app/user_details_vikarabad.html', {'query': query})


@login_required
def user_details_aleru(request):
   query = Document_details.objects.filter(project_name__project_name='ALERU CSA')
   return render(request, 'app/user_details_aleru.html', {'query': query})


@login_required
def user_details_shadnagar(request):
    query = Document_details.objects.filter(project_name__project_name="SHADNAGAR CSA")
    return render(request, 'app/user_details_shadnagar.html', {'query': query})
    


@login_required
def user_details_bhuthpur(request):
    query = Document_details.objects.filter(project_name__project_name="BHUTHPUR CSA")
    return render(request, 'app/user_details_bhuthpur.html', {'query': query})

@login_required
def user_details_maddur(request):
    query = Document_details.objects.filter(project_name__project_name="MADDUR CSA")
    return render(request, 'app/user_details_maddur.html', {'query': query})

@login_required
def plot_details(request, pk):
    #query = New_registration.objects.filter(pk=pk)
    query = Document_details.objects.filter(pk=pk)
    query1 = PostImage.objects.filter(post__in=query)
    
    return render(request, 'app/details.html', {'query': query, 'query1':query1, 'media_url':settings.MEDIA_URL})


@login_required
def document_register(request):

    if request.method =='POST':
        form = DocumentImageForm(request.POST or None, request.FILES)
        images = request.FILES.getlist('document_photos')
        if form.is_valid():
            project_name = form.cleaned_data.get('project_name')
            plot_no = form.cleaned_data.get('plot_no')
            katha_no = form.cleaned_data.get('katha_no')
            new_passbook_no = form.cleaned_data.get('new_passbook_no')
            document_no = form.cleaned_data.get('document_no')
            aadhar_no = form.cleaned_data.get('aadhar_no')
            pass_photo = form.cleaned_data.get('pass_photo')
            passbook_photo = form.cleaned_data.get('passbook_photo')
            Note = form.cleaned_data.get('Note')
            """
            object =Document_details.objects.create(

                project_name=project_name,
                plot_no=plot_no,
                katha_no=katha_no,
                new_passbook_no=new_passbook_no,                  
                document_no=document_no,
                aadhar_no=aadhar_no,
                pass_photo=pass_photo,
                passbook_photo=passbook_photo,
                Note=Note,     
            )
            for i in images:
                PostImage.objects.create(post=object, document_photos=i)
                """

            object = Document_details(
                project_name=project_name,
                plot_no=plot_no,
                katha_no=katha_no,
                new_passbook_no=new_passbook_no,                  
                document_no=document_no,
                aadhar_no=aadhar_no,
                pass_photo=pass_photo,
                passbook_photo=passbook_photo,
                Note=Note,
            )
            object.save()
            for i in images:
                data = PostImage(post=object, document_photos=i)
                data.save()
            messages.success(request, 'Thank you! Plot Account Was Successfully Created.',
                             extra_tags='alert alert-success')           
        else:
            print(form.errors)
            messages.warning(request, 'Sorry, Something went wrong!', extra_tags='alert alert-warning')                     
            
    
    else:
        form = DocumentImageForm
    return render(request, 'app/documents_register.html', {'form': form})

def load_plot_no(request):
    project_name_id = request.GET.get('projectId')
    plot_nos = New_registration.objects.raw('select * from app_new_registration where app_new_registration.project_name_id = %s', [project_name_id])
    return render(request, 'app/dropdown_list_options.html',  {'plot_nos': plot_nos})