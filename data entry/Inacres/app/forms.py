from django import forms
from django.forms import fields
from .models import New_registration, New_project, Document_details

class NewRegistrationForm(forms.ModelForm):

    class Meta:
       model = New_registration
       fields = ('project_name', 'plot_no', 'first_name', 'last_name', 'mail_id', 'mobile_no', 'survey_no', 'land_extent', 'address', 'city', 'district', 'state',  'pincode')

class NewProjectForm(forms.ModelForm):

    class Meta:
       model = New_project
       fields = '__all__'

class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document_details
        fields = ['project_name', 'plot_no', 'katha_no', 'new_passbook_no', 'aadhar_no', 'document_no', 'pass_photo', 'passbook_photo', 'Note']

class DocumentImageForm(DocumentForm):
    document_photos = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(DocumentForm.Meta):
        fields = (DocumentForm.Meta.fields + ['document_photos',])

    



