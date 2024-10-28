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


