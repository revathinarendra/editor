from django.contrib import admin
from .models import Mcq, Subject
from ckeditor_uploader.widgets import CKEditorUploadingWidget  # Correct import
from django import forms

# Create a custom form with the CKEditor widget
class McqsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())  # Use CKEditor for rich text field

    class Meta:
        model = Mcq
        fields = '__all__'

# Register the model with the custom form
class McqsAdmin(admin.ModelAdmin):
    form = McqsAdminForm

admin.site.register(Mcq, McqsAdmin)
admin.site.register(Subject)