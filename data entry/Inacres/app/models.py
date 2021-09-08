from django.core import validators
from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator


# Create your models here.
class New_project(models.Model):
    project_name = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
        return self.project_name

class New_registration(models.Model):
    STATE = (
        ('AP', 'ANDHRA PRADESH'),
        ('TS', 'TELANGANA')    
    )
   
    project_name = models.ForeignKey(New_project, on_delete=models.CASCADE)
    plot_no = models.CharField(max_length=20, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    mail_id = models.EmailField(max_length=100, blank=False, null=False)
    mobile_no  = models.CharField(max_length=15, blank=False, null=False, unique=True)
    survey_no = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=150, blank=False, null=False)
    mandal = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, blank=False, null=False)
    district = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=50, choices=STATE)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return self.plot_no



class Document_details(models.Model):
    project_name = models.ForeignKey(New_project, on_delete=models.CASCADE)
    plot_no = models.ForeignKey(New_registration, on_delete=models.CASCADE, related_name='plot_nos')
    katha_no = models.CharField(max_length=50, blank=False, null=False, unique=True, help_text='Enter Katha Number..')
    new_passbook_no = models.CharField(max_length=50, blank=False, null=False, unique=True, help_text='Enter passbook Number..')
    document_no = models.CharField(max_length=100, blank=False, null=False, unique=True, help_text='Enter Extent document number..')
    aadhar_no = models.BigIntegerField( unique=True, help_text='Enter Aadhar Number..')
    pass_photo = models.ImageField(upload_to='app/',null=False, blank=False, editable=True,  help_text='Upload Passport size Image..')
    passbook_photo = models.ImageField(upload_to='app/',null=False, blank=False, editable=True,  help_text='Upload passbook Image..')
    Note = models.TextField(help_text='please enter note..')

    def __str__(self):
        return self.project_name.project_name

class PostImage(models.Model):
    post = models.ForeignKey(Document_details, default=None, on_delete=models.CASCADE)
    document_photos = models.FileField(upload_to = 'app/')
 
    def __str__(self):
        return str(self.post.plot_no)
