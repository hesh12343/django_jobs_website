from django.db import models

class Job(models.Model):
    class Natures(models.TextChoices):
     FULLTIME='Full time'
     PARTTIME='part time'
     REMOTLY='Remotly'
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=120)
    job_nature = models.CharField(max_length=50, choices=Natures.choices, default=Natures.FULLTIME)
    strat_salary=models.IntegerField()
    end_salary=models.IntegerField()
    description=models.CharField(max_length=300)
    lookingfor=models.CharField(max_length=300)
    requirements=models.CharField(max_length=300)
    jop_feature=models.CharField(max_length=300)
    education=models.CharField(max_length=300)
    def __str__(self):
      return f"job {self.name} with id {self.id}"
 
    
