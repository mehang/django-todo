
from django.db import models
import datetime

PRIORITY_CHOICES = ( 
    (1, 'Low'), 
    (2, 'Normal'), 
    (3, 'High'), 
    (4, 'Urgent')
)

class List(models.Model):
    title = models.CharField(max_length = 250, unique = True)
    description = models.TextField() 
    createddate = models.DateTimeField(default=datetime.datetime.now) 
    completiondate = models.DateTimeField(default=(datetime.datetime.now()+datetime.timedelta(days=1)))
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2) 
    completed = models.BooleanField(default=False) 


    def __str__(self):
        return self.title
    
    class Meta: 
        ordering = ['completiondate','-priority','title'] 

    class Admin:
        pass



