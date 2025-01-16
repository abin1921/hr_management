from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser






# Create your models here.
class Department(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.TextField() 
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
    status = models.IntegerField() 

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    usertype=models.CharField(null=True, blank=True,max_length=100)
    code = models.CharField(max_length=100,blank=True) 
    firstname = models.TextField(null= True)
    lastname = models.TextField(null= True) 
    gender = models.IntegerField(blank=True,null= True) 
    dob = models.DateField(blank=True,null= True) 
    contact = models.IntegerField(null= True) 
    address = models.TextField(null= True) 
    email = models.TextField(null= True)
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE,null= True)
    date_hired = models.DateField(null= True) 
    salary = models.FloatField(default=0) 
    status = models.IntegerField(null= True) 

    def __str__(self):
        return self.firstname + ' ' +self.lastname + ' '

    

class DepartmentHead(models.Model):
    code = models.CharField(max_length=100,blank=True) 
    firstname = models.TextField()
    lastname = models.TextField() 
    gender = models.IntegerField(blank=True,null= True) 
    dob = models.DateField(blank=True,null= True) 
    contact = models.IntegerField() 
    address = models.TextField() 
    email = models.TextField() 
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
    date_hired = models.DateField() 
    salary = models.FloatField(default=0) 
    status = models.IntegerField() 

    def __str__(self):
        return self.firstname + ' ' +self.lastname + ' '


class LeaveType(models.Model):
    leavetype = models.TextField()
    def __str__(self):
        return self.leavetype

class EmployeeLeave(models.Model):
    emp_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    leavetype_id = models.ForeignKey(LeaveType, on_delete=models.CASCADE) 
    from_date = models.DateField() 
    to_date = models.DateField() 
    days_no = models.IntegerField() 
    reason = models.TextField()
    status = models.IntegerField(null=True) 

    
    def __str__(self):
        return self.emp_id

class AdminLeave(models.Model):
    adm_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    leavetype_id = models.ForeignKey(LeaveType, on_delete=models.CASCADE) 
    from_date = models.DateField() 
    to_date = models.DateField() 
    days_no = models.IntegerField() 
    reason = models.TextField()
    status = models.IntegerField(null=True) 
    def __str__(self):
        return self.adm_id

class Clients(models.Model):
    code = models.CharField(max_length=100,blank=True) 
    fullname = models.TextField()
    company_name = models.TextField()
    projects_no = models.IntegerField() 
    email = models.TextField() 
    status = models.IntegerField() 
    def __str__(self):
        return self.fullname

class ClientCompany(models.Model):
    company_name = models.TextField()
    owner = models.TextField() 
    email = models.EmailField() 
    address = models.TextField() 
    projects_no = models.IntegerField() 
    status = models.IntegerField() 
    def __str__(self):
        return self.company_name

class Projects(models.Model):
    title = models.TextField()
    company_id = models.ForeignKey(ClientCompany, on_delete=models.CASCADE) 
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
    emp_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    from_date = models.DateField() 
    to_date = models.DateField() 
    project_description = models.TextField()
    status = models.IntegerField() 
    def __str__(self):
        return self.title

class TrainingType(models.Model):
    trainer = models.TextField()
    course = models.TextField()
    cost = models.FloatField(default=0) 
    def __str__(self):
        return self.course

class Training(models.Model):
    training_id = models.ForeignKey(TrainingType, on_delete=models.CASCADE) 
    from_date = models.DateField() 
    to_date = models.DateField() 
    batch_time=models.TimeField(default=timezone.now)
    status = models.IntegerField() 
    def __str__(self):
        return self.training_id


class Notififaction(models.Model):
    title = models.TextField()
    message = models.TextField()
    def __str__(self):
        return self.message

class EmpNotififaction(models.Model):
    title = models.TextField()
    message = models.TextField()
    def __str__(self):
        return self.message
    
class HrNotififaction(models.Model):
    title = models.TextField()
    message = models.TextField()
    def __str__(self):
        return self.message
    













    













