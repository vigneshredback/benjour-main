from django.db import models

# Create your models here.

# class Journal(models.Model):
#     title = models.CharField(max_length=100)
#     stylesheet_file = models.FileField(upload_to='uploads/stylesheet', blank=False, null=False)
#     journal_template_file = models.FileField(upload_to='uploads/template', blank=False, null=False)
#     author = models.CharField(max_length=100,null=True,blank=True)
#     author = models.CharField(max_length=100,null=True,blank=True)
#     published_date = models.DateField(null=True,blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title


# # class Issue(models.Model):
# #     title = models.CharField(max_length=100)
# #     journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
# #     created_at = models.DateTimeField(auto_now_add=True)
# #     updated_at = models.DateTimeField(auto_now=True)

# #     def __str__(self):
# #         return self.title

# class Paper(models.Model):
#     journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     content = models.TextField(null=True,blank=True)
#     pdf_file = models.FileField(upload_to='uploads/paper')
#     word_file = models.FileField(upload_to='uploads/template', blank=False, null=False)
#     published_date = models.DateField(null=True,blank=True)
#     author = models.CharField(max_length=100,null=True,blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
        # return self.title

class JournalName(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100,null=True,blank=True)
    published_date = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stylesheet_word_file = models.FileField(upload_to='uploads/journal', blank=False, null=False)
    stylesheet_pdf_file = models.FileField(upload_to='uploads/journal', blank=False, null=False)
    journal_template_word_file = models.FileField(upload_to='uploads/journal', blank=False, null=False)
    journal_template_pdf_file = models.FileField(upload_to='uploads/journal', blank=False, null=False)
    def __str__(self):
        return self.title
        

class Volume(models.Model):
    title = models.CharField(max_length=100)
    volume_number = models.IntegerField(unique=True)
    journal_name = models.ForeignKey(JournalName, on_delete=models.CASCADE)
    published_date = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Issue(models.Model):
    title = models.CharField(max_length=100)
    issue_number = models.IntegerField(unique=True)
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE)
    published_date = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Paper(models.Model):
    journal_issue_number = models.ForeignKey(Issue, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True,blank=True)
    keywords = models.TextField(null=True,blank=True)
    pdf_file = models.FileField(upload_to='uploads/paper')
    word_file = models.FileField(upload_to='uploads/paper', blank=False, null=False)
    published_date = models.DateField(null=True,blank=True)
    author = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
