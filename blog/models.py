from django.db import models
#uses files which we need often
from django.utils import timezone

class Post(models.Model):
    #defines the model
    #it's a class
    #with the name 'Post'
    #it's a Django model and should saved in the django db
    #the declaration of variables
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #ForeignKey Link to other models
    title = models.CharField(max_length=200) # CharField Text with limitated characters
    text = models.TextField() # TextField Text with unlimited characters
    created_date = models.DateTimeField(default = timezone.now) #DateTimeField Fild for Time and Date
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self): # new method for publishing
        self.published_date=timezone.now()
        self.save()

    def __str__(self): # return the title
        return self.title



