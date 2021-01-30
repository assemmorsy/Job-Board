from django.db import models

JOBTYPE = [( "FT", "full time") , ("PT" , "part time")]
# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name



class Job(models.Model):
    title = models.CharField( max_length=50)
    job_type =models.CharField(max_length=2 , choices=JOBTYPE)
    description = models.TextField()
    published_at=models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(  default=1)
    salary = models.IntegerField(default= 0)
    experiance = models.IntegerField(default= 1)
    
    category = models.ForeignKey(category, default= 1,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    