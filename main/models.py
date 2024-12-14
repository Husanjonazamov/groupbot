from django.db import models




class User(models.Model):
    user_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=150)
    
    
    def __str__(self):
        return self.first_name
    
    
class Notice(models.Model):
    descriptions = models.TextField()
    interval = models.PositiveIntegerField(help_text="Interval in seconds")  
    
    def __str__(self):
        return self.descriptions[:50]  


class Elonlarim(models.Model):
    description = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.description[:50]  

    
    