# Ex02 Django ORM Web Application
## Date: 28.10.2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

![alt text](<Screenshot (7).png>)



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import loan,loanAdmin
admin.site.register(loan,loanAdmin)

models.py

from django.db import models
from django.contrib import admin
class loan(models.Model):
	Name=models.CharField(max_length=20)
	Accno=models.IntegerField(primary_key="Accno")
	DOB=models.DateField()
	Photo=models.ImageField()
	Mobileno=models.IntegerField()
	Aadharno=models.IntegerField()
class loanAdmin(admin.ModelAdmin):
	list_display=('Name','Accno','DOB','Photo','Mobileno','Aadharno')

```

## OUTPUT
![alt text](<Screenshot (6).png>)





## RESULT
Thus the program for creating a database using ORM hass been executed successfully
