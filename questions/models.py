from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
class Subject(models.Model):
    subject_name = models.CharField()
    def __str__(self):
        return self.subject_name
class Mcq(models.Model):
    subject_name = models.ForeignKey('Subject', on_delete=models.CASCADE)
    question = models.TextField()
    content = RichTextField()  # Enables image upload in the editor
    def __str__(self):
        return self.question