from django.forms.widgets import Media
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include



app_name = 'app'

urlpatterns = [
    #path('tinymce/', include('tinymce.urls')),
    path('', views.index, name='index'),
    #path('login/', views.login_request, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sites/', views.site_names, name='sites'),
    path('registration/', views.new_registration, name='registration'),
    path('newproject/', views.new_project, name='newproject'),
    path('user_details/vikarabad/', views.user_details_vikarabad, name='userdetailsvikarabad'),
    path('user_details/aleru/', views.user_details_aleru, name='userdetailsaleru'),
    path('user_details/shadnagar/', views.user_details_shadnagar, name='userdetailsshadnagar'),
    path('user_details/bhuthpur/', views.user_details_bhuthpur, name='userdetailsbhuthpur'),
    path('user_details/maddur/', views.user_details_maddur, name='userdetailsmaddur'),
    path('details/<int:pk>', views.plot_details, name='details'),
    path('documentregister/', views.document_register, name='documentregister'),
    #path('edit/<int:pk>', views.documentsUpdateView, name='update'),
    path('ajax/load-plot_nos/', views.load_plot_no, name='ajax_load_plot_no'), 
    path('search/', views.user_details, name='search'),
    path('plots_available/',views.plots_available, name='plotsavailable'),
    path(r'^{}(?P<path>.*)$'.format(settings.MEDIA_URL[1:]), views.protected_serve, {'file_root': settings.MEDIA_ROOT}),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
