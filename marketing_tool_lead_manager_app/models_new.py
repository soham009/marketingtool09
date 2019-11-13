#<---------Django Imported Libraries--------->
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils import timezone
#</---------Django Imported Libraries--------->

# Create your models here.

#user Model
class CustomUser(AbstractUser):
    '''Overrides the custom django user model'''
    # Datafields
    NORMAL_USER = 1
    RESTAURANT_1_ADMIN = 2
    SUPER_ADMIN = 13
    ROLE_CHOICES = (
      (NORMAL_USER,'normal_user'),
      (RESTAURANT_1_ADMIN,'admin'),
      (SUPER_ADMIN,'super_admin'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=NORMAL_USER)
    name = models.CharField(max_length=264, blank='True')
    password_change_request = models.BooleanField(default=False)

#Pickup location Model
class Pickup_Location(models.Model):
    Location_Name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.Location_Name)

#Drop location Model
class Drop_Location(models.Model):
    Drop_Name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.Drop_Name)

#Login Time Model
class Login_Time(models.Model):
    Time = models.CharField(max_length=200)

    def __str__(self):
        return str(self.Time)

#Logout Time Model
class Logout_Time(models.Model):
    Time = models.CharField(max_length=200)

    def __str__(self):
        return str(self.Time)

#Leads Model
class Leads(models.Model):
    LEAD_STATUS = (('Interested','Interested'),
                   ('Undecided','Undecided'),
                   ('Uncontacted','Uncontacted'),
                   ('Converted','Converted'))
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    City = models.CharField(max_length=264,blank=True)
    Name = models.CharField(max_length=264)
    Gender	=	models.CharField(max_length=264,blank=True)
    EmailId	=	models.CharField(max_length=264,blank=True)
    ContactNo	=	models.CharField(max_length=264,blank=True)
    CompanyName	=	models.CharField(max_length=264,blank=True)
    TravalToWork	=	models.CharField(max_length=264,blank=True)
    TravelToWorkOther	= models.CharField(max_length=264,blank=True)
    MonthlySpend	=	models.CharField(max_length=264,blank=True)
    HearAboutUs	=	models.CharField(max_length=264,blank=True)
    SubmittedOn	=	models.CharField(max_length=264,blank=True)
    Lead_Status = models.CharField(choices=LEAD_STATUS,max_length=264,default="Uncontacted")
    Remark = models.TextField(blank=True)
    LocationFromOther = models.CharField(max_length=264,blank=True)
    SubmittedOnDate	=	models.DateTimeField(default=timezone.now)
    is_valid = models.BooleanField(default=False)
    Pickup_Location_id = models.ForeignKey(Pickup_Location, on_delete = models.CASCADE)
    Drop_Location_id = models.ForeignKey(Drop_Location,  on_delete = models.CASCADE)
    Login_Time_id = models.ForeignKey(Login_Time, on_delete = models.CASCADE)
    Logout_Time_id = models.ForeignKey(Logout_Time,  on_delete = models.CASCADE)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = "Leads Collected"
        verbose_name = "Lead"

class Lead_Comment(models.Model):
    status_type_choices=(('Interested','Interested'),
                        ('Undecided','Undecided'),
                        ('Uncontacted','Uncontacted'),
                        ('Converted','Converted'))
    product_interested_in_type_choice=(('Nodal Service','Nodal Service'),
                                      ('Hub Cab','Hub Cab'),
                                      ('Others','Others'))
    lead_comment_id=models.ForeignKey(Leads, on_delete = models.CASCADE)
    lead_comment_updated_by =models.ForeignKey(Leads,on_delete= models.CASCADE)
    lead_comment_name=models.CharField(choices=status_type_choices,max_length=264)
    lead_comment_create_date= models.DateTimeField(default=timezone.now)
    lead_comment_remark=models.TextField(max_length=264,blank=True)
    lead_comment_product_interested_in = models.CharField(choices=product_interested_in_type_choice,max_length=264,default='Not Selected')
    lead_comment_next_followup_date=models.DateField(max_length=264)
    lead_comment_updated = models.DateTimeField(auto_now=True)
    lead_comment_Created_at = models.DateTimeField(auto_now_add=True)
    lead_comment_Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name_plural = "Leads Comment"
        verbose_name = "Lead Comment"

class Company_Leads(models.Model):
   company_leads_added_by = models.ForeignKey(CustomUser,on_delete= models.CASCADE)
   company_leads_pickup_location_id = models.ForeignKey(Pickup_Location, on_delete = models.CASCADE)
   company_leads_created_at = models.DateTimeField(auto_now_add=True)
   company_leads_corporate_hub =models.CharField(choices=status_type_choices,max_length=264)
   company_leads_company_name = models.CharField(choices=status_type_choices,max_length=264)
   company_leads_login_time =models.ForeignKey(Login_Time,on_delete= models.CASCADE)
   company_leads_logout_time=models.ForeignKey(Logout_Time,on_delete= models.CASCADE)
   company_leads_employee_strength= models.CharField(choices=status_type_choices,max_length=264)
   company_leads_contact_person=models.CharField(choices=status_type_choices,max_length=264)
   company_leads_contact_mobile=models.CharField(choices=status_type_choices,max_length=264)
   company_leads_contact_email= models.CharField(choices=status_type_choices,max_length=264)
   
   def __str__(self):
       return self.pk


class Company_Leads_Comment(models.Model):
   status_type_choices=(('Interested','Interested'),
                            ('Undecided','Undecided'),
                            ('Uncontacted','Uncontacted'),
                            ('Converted','Converted'))
   product_interested_in_type_choice=(('Nodel Service','Nodel Service'),
                                      ('Hub Cab','Hub Cab'),
                                      ('Others','Others'))
   company_lead_comment_id=models.ForeignKey(Company_Leads, on_delete = models.CASCADE)
   company_lead_comment_updated_by =models.ForeignKey(Company_Leads,on_delete= models.CASCADE)
   company_lead_comment_name=models.CharField(choices=status_type_choices,max_length=264)
   company_lead_comment_create_date= models.DateTimeField(default=timezone.now)
   company_lead_comment_remark=models.TextField(max_length=264,blank=True)
   
   def __str__(self):
       return self.pk     