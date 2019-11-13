#--- Marketing Tool - Imported Packages List ----
#<------Django Internal Packages-----
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.forms import CheckboxSelectMultiple, CheckboxInput, DateInput
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password


#</------Django Internal Packages-----

#<------ External Installed Packages -----
import datetime
from rest_framework import generics
from funky_sheets.formsets import HotView
from marketing_tool_lead_manager_app.serializers import LeadsSerializer, LeadsCitySerializer, LeadsDetailsSerializer
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from django.http import JsonResponse

#</------ External Installed Packages -----


#------ Marketing Tool Internal Project Packages -----
from marketing_tool_lead_manager_app.models import Leads, CustomUser, Pickup_Location, Drop_Location, Login_Time, Logout_Time,Company_Leads,Lead_Comment
from marketing_tool_lead_manager_app.forms import LeadForm,UpdateLocationFrom,LeadCommentForm,Login_Time_form,UpdateLocationTo,Logout_Time_form,CustomUserForm,CustomUserUpdateForm
from marketing_tool_lead_manager_app import count_functions
from marketing_tool_lead_manager_app import dictionaries
#</------ Marketing Tool Internal Project Packages -----

#<------------Page Rendering Views------------------>




def Signup(request):
    """Registers a user"""
    if request.method == "POST":
        username =  request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return render(request, 'marketing_tool_lead_manager_app/Signup.html',{'error_message':'Passwords do not match!'})
        if CustomUser.objects.filter(username = username).exists():
            return render(request, 'marketing_tool_lead_manager_app/Signup.html',{'error_message':'Username already exists!'})
        else:
            # Role 2 is for admin, 1 is for super admin.
            user = CustomUser.objects.create(username=username, password= make_password(password), user_role=2)
            login(request, user)
            return render(request, 'marketing_tool_lead_manager_app/lead_zing_grid_list.html') 
    else:
        return render(request, 'generamarketing_tool_lead_manager_appteletter/Signup.html')        

#Home Page View
def survey_form(request):
    """Homepage of Marketing Tool
    Parameters: HttpRequest object
    Returns : Nothing"""
    leads = Leads.objects.all()
    pickup_locations = Pickup_Location.objects.all()
    Drop_Locations = Drop_Location.objects.all()
    login_time_list = Login_Time.objects.all()
    logout_time_list = Logout_Time.objects.all()
    page_active = 1
    data = { 'leads': leads,
            'pickup_locations' :pickup_locations,
            'Drop_Locations' : Drop_Locations,
            'page_active': page_active,
            'login_time_list' :login_time_list,
            'logout_time_list' : logout_time_list}
    return render(request,'marketing_tool_lead_manager_app/survey_form.html',data)

#Survey_Form_Submit
def home_form_submit(request):
    if request.method == "POST":
        City = request.POST['City']
        Full_Name = request.POST['Name']
        Gender = request.POST['Gender']
        Email_Id = request.POST['user_Email_Id']
        Contact_No = request.POST['user_Contact_No']
        Company_Name = request.POST['user_Company_Name']
        TravalToWork = request.POST['TravalToWork']
        MonthlySpend = request.POST['MonthlySpend']
        HearAboutUs = request.POST['HearAboutUs']
        LoginTime = request.POST['LoginTime']
        LogoutTime = request.POST['LogoutTime']
        Remark = request.POST['Remark']
        Pickup_Location_id = Pickup_Location.objects.get(pk=request.POST['LocationFrom'])
        Drop_Location_id = Drop_Location.objects.get(pk=request.POST['LocationTo'])
        Login_Time_id = Login_Time.objects.get(pk=request.POST['LoginTime'])
        Logout_Time_id = Logout_Time.objects.get(pk=request.POST['LogoutTime'])
        leads = Leads.objects.create( City='Mumbai',Name = Full_Name,Gender=Gender, EmailId = Email_Id, ContactNo = Contact_No, CompanyName = Company_Name, Pickup_Location_id = Pickup_Location_id, Drop_Location_id = Drop_Location_id, Login_Time_id = Login_Time_id, Logout_Time_id = Logout_Time_id, TravalToWork = TravalToWork, MonthlySpend = MonthlySpend, Remark = Remark,HearAboutUs=HearAboutUs)
    return HttpResponseRedirect(reverse('marketing_tool_lead_manager_app:home'))

#Marketing Tool - Summary View
@login_required(login_url = '/Login')
def summary(request):
    """Summary Page of webapp
    Parameters: HttpRequest object
    Returns : Nothing"""
    all_lead_objects_count = Leads.objects.all().count()
    lead_uncontacted_objects_count = Leads.objects.all().filter(Lead_Status='Uncontacted').count()
    lead_interested_objects_count = Leads.objects.all().filter(Lead_Status='Interested').count()
    lead_converted_objects_count = Leads.objects.all().filter(Lead_Status='Converted').count()
    lead_undecided_objects_count = Leads.objects.all().filter(Lead_Status='Undecided').count()
    all_custom_user_object = CustomUser.objects.all()
    data ={'lead_count':all_lead_objects_count, 'uncontacted_count':lead_uncontacted_objects_count, 'interested_count':lead_interested_objects_count,'converted_count':lead_converted_objects_count, 'undecided_count':lead_undecided_objects_count,'users':all_custom_user_object}
    return render(request,'marketing_tool_lead_manager_app/summary.html',data)


#Marketing Tool - All Leads View
@login_required(login_url = '/Login')
def lead_zing_grid_list(request):
    leads = Leads.objects.all()
    pickup_locations = Pickup_Location.objects.all()
    Drop_Locations = Drop_Location.objects.all()
    login_time_list = Login_Time.objects.all()
    logout_time_list = Logout_Time.objects.all()
    page_active = 1
    data = { 'leads': leads,
            'pickup_locations' :pickup_locations,
            'Drop_Locations' : Drop_Locations,
            'page_active': page_active,
            'login_time_list' :login_time_list,
            'logout_time_list' : logout_time_list}
    return render(request,'marketing_tool_lead_manager_app/lead_zing_grid_list.html',data)

#Marketing Tool - Mumbai Leads View
@login_required(login_url = '/Login')
def lead_zing_grid_list_mumbai(request):
    return render(request,'marketing_tool_lead_manager_app/lead_zing_grid_list_mumbai.html')


#All Routes View
@login_required(login_url = '/Login')
def all_routes(request):
    """All Routes Page of webapp
    Parameters: HttpRequest object
    Returns : Nothing"""
    #Pickup Location Object Calling
    pickup_location_objects = Pickup_Location.objects.all()
    #Drop Location Object Calling
    drop_location_objects = Drop_Location.objects.all()
    #Login Time  Object Calling
    login_time_objects = Login_Time.objects.all()
    #Logout Time  Object Calling
    logout_time_objects = Logout_Time.objects.all()
    #Creating a object called as
    x = list(set(list(Leads.objects.all().values_list('Pickup_Location_id', 'Drop_Location_id','Login_Time_id','Logout_Time_id'))))
    lead_Status_list = ["Uncontacted","Undecided","Converted","Interested"]
    routes = [ count_functions.Total_Routes_Count(a,lead_status) for a in x for lead_status in lead_Status_list ]
    final = [routes[i * 4:(i + 1) * 4] for i in range((len(routes) + 4 - 1) // 4 )]
    routes_dict = dict(zip(x, final))
    #Pickup Location Dictionary Formation
    Pickup_Location_dict = {}
    for pickup in pickup_location_objects:
        Pickup_Location_dict[pickup.pk]=pickup.Location_Name
    #Drop Location Dictionary Formation
    drop_Location_dict = {}
    for drop in drop_location_objects:
        drop_Location_dict[drop.pk]=drop.Drop_Name
    #Login Time Dictionary Formation
    login_time_dict = {}
    for login in login_time_objects:
        login_time_dict[login.pk]=login.Time
    #Logout Time Dictionary Formation
    logout_time_dict = {}
    for logout in logout_time_objects:
        logout_time_dict[logout.pk]=logout.Time
    return render(request,'marketing_tool_lead_manager_app/all_routes.html', { 'routes_dict': routes_dict,'Pickup_Location_dict':Pickup_Location_dict,'drop_Location_dict':drop_Location_dict,'login_time_dict':login_time_dict,'logout_time_dict':logout_time_dict })

#All Routes Detail View
@login_required(login_url = '/Login')
def routes_details(request):
    """All Routes By City Details Page of webapp
    Parameters: HttpRequest object
    Returns : Nothing"""
    return render(request,'marketing_tool_lead_manager_app/all_routes_details.html')


#Marketing Tool - Leads Details based on Location From, Location To, Login Time and Logout Time (Zinggrid)
@login_required(login_url = '/Login')
def leads_locationfrom_locationto_logintime_logouttime(request,location_from,location_to,login_time,logout_time):
    #Pickup Location Object Calling
    pickup_location_objects = Pickup_Location.objects.get(pk=location_from)
    #Drop Location Object Calling
    drop_location_objects = Drop_Location.objects.get(pk=location_to)
    #Login Time  Object Calling
    login_time_objects = Login_Time.objects.get(pk=login_time)
    #Logout Time  Object Calling
    logout_time_objects = Logout_Time.objects.get(pk=logout_time)
    leads = Leads.objects.filter(Pickup_Location_id=pickup_location_objects,Drop_Location_id=drop_location_objects,Login_Time_id=login_time_objects,Logout_Time_id=logout_time_objects).all()
    data = {'leads':leads,'location_from':location_from,'location_to':location_to,'login_time':login_time,'logout_time':logout_time}
    return render(request,'marketing_tool_lead_manager_app/routes_list_zinggrid.html',data)

#Marketing Tool - Leads Details based on Location From, Location To, Login Time and Logout Time (Data  Table)
@login_required(login_url = '/Login')
def leads_locationfrom_locationto_logintime_logouttime_dt(request,location_from,location_to,login_time,logout_time):
    leads_list = Leads.objects.all()
    pickup_location_objects = Pickup_Location.objects.get(pk=location_from)
    drop_location_objects = Drop_Location.objects.get(pk=location_to)
    login_time_objects = Login_Time.objects.get(pk=login_time)
    logout_time_objects = Logout_Time.objects.get(pk=logout_time)

    leads = Leads.objects.filter(Pickup_Location_id=pickup_location_objects,Drop_Location_id=drop_location_objects,Login_Time_id=login_time_objects,Logout_Time_id=logout_time_objects).all()
    
    data = {'leads':leads,'location_from':location_from,'location_to':location_to,'login_time':login_time,'logout_time':logout_time}
    
    return render(request,'marketing_tool_lead_manager_app/routes_list_details.html',data)



#Mumbai Leads Routes View
@login_required(login_url = '/Login')
def leads_routes(request):
    """All Mumbai Routes Page of webapp
    Parameters: HttpRequest object
    Returns : Nothing"""
    #Pickup Location Object Calling
    pickup_location_objects = Pickup_Location.objects.all()
    #Drop Location Object Calling
    drop_location_objects = Drop_Location.objects.all()
    #Login Time  Object Calling
    login_time_objects = Login_Time.objects.all()
    #Logout Time  Object Calling
    logout_time_objects = Logout_Time.objects.all()
    y = list(set(list(Leads.objects.all().filter(City='Mumbai').values_list('Pickup_Location_id', 'Drop_Location_id','Login_Time_id','Logout_Time_id'))))
    lead_Status_list = ["Uncontacted","Undecided","Converted","Interested"]
    routes = [ count_functions.Total_Routes_Count(a,lead_status) for a in y for lead_status in lead_Status_list ]
    final = [routes[i * 4:(i + 1) * 4] for i in range((len(routes) + 4 - 1) // 4 )]
    routes_dict = dict(zip(y, final))
    #Pickup Location Dictionary Formation
    Pickup_Location_dict = {}
    for pickup in pickup_location_objects:
        Pickup_Location_dict[pickup.pk]=pickup.Location_Name
    #Drop Location Dictionary Formation
    drop_Location_dict = {}
    for drop in drop_location_objects:
        drop_Location_dict[drop.pk]=drop.Drop_Name
    #Login Time Dictionary Formation
    login_time_dict = {}
    for login in login_time_objects:
        login_time_dict[login.pk]=login.Time
    #Logout Time Dictionary Formation
    logout_time_dict = {}
    for logout in logout_time_objects:
        logout_time_dict[logout.pk]=logout.Time
    return render(request,'marketing_tool_lead_manager_app/mumbai_routes.html', { 'routes_dict': routes_dict,'Pickup_Location_dict':Pickup_Location_dict,'drop_Location_dict':drop_Location_dict,'login_time_dict':login_time_dict,'logout_time_dict':logout_time_dict })


#Mumbai Routes Detail View
@login_required(login_url = '/Login')
def city_routes_details(request):
    """All Mumbai Routes Details Page of webapp
    Parameters: HttpRequest object
    Returns : Nothing"""
    return render(request,'marketing_tool_lead_manager_app/mumbai_routes_details.html')


#Location From View
@login_required(login_url = '/Login')
def location_from(request):
    """All location From Page of webapp
    Parameters: HttpRequest object
    Returns : Nothing"""
    location_from_objects = Pickup_Location.objects.all()
    data = {'location_from':location_from_objects}
    return render(request,'marketing_tool_lead_manager_app/location_from.html',data)

#Location To View
@login_required(login_url = '/Login')
def location_to(request):
    """All location To Page of webapp
    Parameters: HttpRequest object
    Returns : Nothing"""
    location_to_objects = Drop_Location.objects.all()
    data = {'location_to':location_to_objects}
    return render(request,'marketing_tool_lead_manager_app/location_to.html',data)


#Login Time View
@login_required(login_url = '/Login')
def login_time(request):
    """All login Time Page of webapp
    Parameters: HttpRequest object
    Returns : Nothing"""
    login_time_objects = Login_Time.objects.all()
    data = {'login_time':login_time_objects}
    return render(request,'marketing_tool_lead_manager_app/login_time.html',data)

#Logout Time View
@login_required(login_url = '/Login')
def logout_time(request):
    """All logout Time Page of webapp
    Parameters: HttpRequest object
    Returns : Nothing"""
    logout_time =Logout_Time.objects.all()
    data = {'logout_time':logout_time}
    return render(request,'marketing_tool_lead_manager_app/logout_time.html',data)

#Portal Users View
@login_required(login_url = '/Login')
def users(request):
    """All Portal Users Page of webapp
    Parameters: HttpRequest object
    Returns : Nothing"""
    all_custom_user_object = CustomUser.objects.all()
    data = {'users':all_custom_user_object}
    return render(request,'marketing_tool_lead_manager_app/portal_user.html',data)
#</------------Page Rendering Views------------------>

#<-------Authentications Views ---------------------->
def Login(request):
    """Logs in a user if the credentials are valid and the user is active, 
    else redirects to the same page and displays an error message."""
    if request.method == "POST":
        username =  request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request,'marketing_tool_lead_manager_app/lead_zing_grid_list.html')
        else:
            return render(request, 'marketing_tool_lead_manager_app/login.html',{'error_message': 'Username or Password Incorrect!'})

    else:
        return render(request, 'marketing_tool_lead_manager_app/login.html')


#User Sign up
def register(request):
    """Registers a user"""
    if request.method == "POST":
        username =  request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return render(request, 'marketing_tool_lead_manager_app/Signup.html',{'error_message':'Passwords do not match!'})
        if CustomUser.objects.filter(username = username).exists():
            return render(request, 'marketing_tool_lead_manager_app/Signup.html',{'error_message':'Username already exists!'})
        else:
            # Role 2 is for admin, 1 is for super admin.
            user = CustomUser.objects.create(username=username, password= make_password(password), user_role=2)
            login(request, user)
            return render(request, 'marketing_tool_lead_manager_app/lead_zing_grid_list.html') 
    else:
        return render(request, 'marketing_tool_lead_manager_app/Signup.html')  

#User Sign Out
def user_sign_out(request):
    return render(request, 'marketing_tool_lead_manager_app/Login.html')
#</-------Authentications Views ---------------------->

#<------------BS Modal Views ------------------------->
#Read Lead view
@method_decorator(login_required, name='dispatch')
class LeadReadView(BSModalReadView):
    model = Leads
    template_name = 'marketing_tool_lead_manager_app/read_Lead.html'

#Update lead view
@method_decorator(login_required, name='dispatch')
class LeadUpdateView(BSModalUpdateView):
    model = Leads
    template_name = 'marketing_tool_lead_manager_app/update_Lead.html'
    form_class = LeadForm
    success_message = 'Success: Lead was updated.'
    success_url = reverse_lazy('leads')

@method_decorator(login_required, name='dispatch')
class LeadUpdateView(BSModalUpdateView):
    model = Leads
    template_name = 'marketing_tool_lead_manager_app/update_Lead.html'
    form_class = LeadForm
    success_message = 'Success: Lead was updated.'
    success_url = reverse_lazy('leads')    

#Delete Lead view
@method_decorator(login_required, name='dispatch')
class LeadDeleteView(BSModalDeleteView):
    model = Leads
    template_name = 'marketing_tool_lead_manager_app/delete_Lead.html'
    success_message = 'Success: Lead was deleted.'
    success_url = reverse_lazy('leads')


@method_decorator(login_required, name='dispatch')
class LocationUpdateView(BSModalUpdateView):
    model = Pickup_Location
    template_name = 'marketing_tool_lead_manager_app/update_location.html'
    form_class = UpdateLocationFrom
    success_message = 'Success: Location was updated.'
    success_url = reverse_lazy('marketing_tool_lead_manager_app:location_from')

@method_decorator(login_required, name='dispatch')
class LocationDropUpdateView(BSModalUpdateView):
    model = Drop_Location
    template_name = 'marketing_tool_lead_manager_app/update_location.html'
    form_class = UpdateLocationTo
    success_message = 'Success: Location was updated.'
    success_url = reverse_lazy('marketing_tool_lead_manager_app:location_to')    

@method_decorator(login_required, name='dispatch')
class update_login_time(BSModalUpdateView):
    model = Login_Time
    template_name = 'marketing_tool_lead_manager_app/Update_Login_Time.html'
    form_class = Login_Time_form
    success_message = 'Success: Login time was updated.'
    success_url = reverse_lazy('marketing_tool_lead_manager_app:login_time')     

@method_decorator(login_required, name='dispatch')
class update_logout_time(BSModalUpdateView):
    model = Logout_Time
    template_name = 'marketing_tool_lead_manager_app/Update_Logout_Time.html'
    form_class = Logout_Time_form
    success_message = 'Success: Logout time was updated.'
    success_url = reverse_lazy('marketing_tool_lead_manager_app:logout_time')

@method_decorator(login_required, name='dispatch')    
class delete_login_time(BSModalDeleteView):
    model = Login_Time
    template_name = 'marketing_tool_lead_manager_app/delete.html'
    success_message = 'Success: Location was Deleted.'
    success_url = reverse_lazy('marketing_tool_lead_manager_app:login_time')

@method_decorator(login_required, name='dispatch')
class delete_logout_time(BSModalDeleteView):
    model = Logout_Time
    template_name = 'marketing_tool_lead_manager_app/delete.html'
    success_message = 'Success: Location was Deleted.'
    success_url = reverse_lazy('marketing_tool_lead_manager_app:logout_time') 

@method_decorator(login_required, name='dispatch')
class delete_pickup(BSModalDeleteView):
    model = Pickup_Location
    template_name = 'marketing_tool_lead_manager_app/delete.html'
    success_message = 'Success: Location was Deleted.'
    success_url = reverse_lazy('marketing_tool_lead_manager_app:location_from')

@method_decorator(login_required, name='dispatch')
class delete_drop(BSModalDeleteView):
    model = Drop_Location
    template_name = 'marketing_tool_lead_manager_app/delete.html'
    success_message = 'Success: Location was Deleted.'
    success_url = reverse_lazy('marketing_tool_lead_manager_app:location_to')  

@method_decorator(login_required, name='dispatch')
class Add_pickup(BSModalCreateView):
    model = Pickup_Location
    template_name = 'marketing_tool_lead_manager_app/createlocation.html'
    form_class = UpdateLocationFrom
    success_message = 'Success: Organization was added.'
    success_url = reverse_lazy('marketing_tool_lead_manager_app:location_from')

@method_decorator(login_required, name='dispatch')
class Add_drop(BSModalCreateView):
    model = Drop_Location
    template_name = 'marketing_tool_lead_manager_app/createlocation.html'
    form_class = UpdateLocationTo
    success_message = 'Success: Organization was added.'
    success_url = reverse_lazy('marketing_tool_lead_manager_app:location_to')

@method_decorator(login_required, name='dispatch')
class Add_login(BSModalCreateView):
    model = Login_Time
    template_name = 'marketing_tool_lead_manager_app/addlogintime.html'
    form_class = Login_Time_form
    success_message = 'Success: Organization was added.'
    success_url = reverse_lazy('marketing_tool_lead_manager_app:login_time')

@method_decorator(login_required, name='dispatch')
class Add_logout(BSModalCreateView):
    model = Logout_Time
    template_name = 'marketing_tool_lead_manager_app/addlogouttime.html'
    form_class = Logout_Time_form
    success_message = 'Success: Organization was added.'
    success_url = reverse_lazy('marketing_tool_lead_manager_app:logout_time')  

@method_decorator(login_required, name='dispatch')
class Add_new_user(BSModalCreateView):
    template_name = 'marketing_tool_lead_manager_app/adduser.html'
    form_class = CustomUserForm
    success_message = 'Success: New Team Member was added.'
    success_url = reverse_lazy('marketing_tool_lead_manager_app:users')

@method_decorator(login_required, name='dispatch')
class update_user(BSModalUpdateView):
    model = CustomUser
    template_name = 'marketing_tool_lead_manager_app/updateuser.html'
    form_class = CustomUserUpdateForm
    success_message = 'Success: Logout time was updated.'
    success_url = reverse_lazy('marketing_tool_lead_manager_app:users')

@method_decorator(login_required, name='dispatch')
class delete_user(BSModalDeleteView):
    model = CustomUser
    template_name = 'marketing_tool_lead_manager_app/delete.html'
    success_message = 'Success: Lead was deleted.'
    success_url = reverse_lazy('marketing_tool_lead_manager_app:users')    


#</-----------BS Modal Views ------------------------>

#Update lead view
class Leads_API(generics.ListAPIView):
    '''ListView for the api endpoint /api/restaurant/'''
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer

#Update lead view
class Leads_Mumbai_API(generics.ListAPIView):
    '''ListView for the api endpoint /api/restaurant/'''
    queryset = Leads.objects.filter(City='Mumbai').all()
    serializer_class = LeadsSerializer

class leads_api_Details(generics.ListAPIView):
    serializer_class = LeadsDetailsSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        location_from = self.kwargs['location_from']
        location_to = self.kwargs['location_to']
        login_time = self.kwargs['login_time']
        logout_time = self.kwargs['logout_time']
        pickup_location_objects = Pickup_Location.objects.get(pk=location_from)
        #Drop Location Object Calling
        drop_location_objects = Drop_Location.objects.get(pk=location_to)
        #Login Time  Object Calling
        login_time_objects = Login_Time.objects.get(pk=login_time)
        #Logout Time  Object Calling
        logout_time_objects = Logout_Time.objects.get(pk=logout_time)
        return Leads.objects.filter(Pickup_Location_id=pickup_location_objects,Drop_Location_id=drop_location_objects,Login_Time_id=login_time_objects,Logout_Time_id=logout_time_objects).all()


def routes_list(request):
    MAX_OBJECTS = 20
    leads_all = Leads.objects.all()
    data = list(leads_all.values("Pickup_Location_id", "Drop_Location_id", "Login_Time_id","Logout_Time_id"))
    return JsonResponse(data)


#<------------ Experiment View ------------------------->

#All Routes View
def all_routes_experiment(request):
    """All Routes Page of webapp
    Parameters: HttpRequest object
    Returns : Nothing"""
    #Pickup Location Object Calling
    routes_dict_list=[]
    leads=Leads.objects.all()
    for lead in leads:
         routes_dict_list.append({'location_from':lead.Pickup_Location_id.Location_Name,'location_to':lead.Drop_Location_id.Drop_Name,'login_time':lead.Login_Time_id.Time,'logout_time':lead.Logout_Time_id.Time})
    data = { 'routes_dict_list':str(routes_dict_list).replace("/'","") }
    return render(request,'marketing_tool_lead_manager_app/routes_experiment.html',data)

#</------------ Experiment View ------------------------->


#<------------- Company Lead B2B View-------------------->

#Base page view
@login_required(login_url = '/Login')
def company_lead_base(request):
    return render(request, 'marketing_tool_lead_manager_app/base_b2b.html')

@login_required(login_url = '/Login')
def company_lead_form(request):
    username=request.user.username
    #user_pk=request.user.pk
    pickup_locations = Pickup_Location.objects.all()
    login_time_list = Login_Time.objects.all()
    logout_time_list = Logout_Time.objects.all()
    data = {'username' :username,'pickup_locations' :pickup_locations,'login_time_list' :login_time_list,'logout_time_list' : logout_time_list}
    return render(request, 'marketing_tool_lead_manager_app/company_lead_form.html',data)

@login_required(login_url = '/Login')
def company_lead_report(request):
    return render(request, 'marketing_tool_lead_manager_app/company_lead_report.html')

@login_required(login_url = '/Login')
def company_lead_data(request):
    company_leads_all_objects = Company_Leads.objects.all()
    data = {
        'leads':company_leads_all_objects,
    }
    return render(request, 'marketing_tool_lead_manager_app/company_lead_list.html',data)

@login_required(login_url = '/Login')
def company_lead_form_submit(request):
    if request.method == 'POST':
        #company_leads_added_by=request.POST['company_leads_added_by']
        company_leads_pickup_location_id=request.POST['company_leads_pickup_location_id']
        company_leads_corporate_hub=request.POST['company_leads_corporate_hub']
        company_leads_company_name=request.POST['company_leads_company_name']
        company_leads_login_time=request.POST['company_leads_login_time']
        company_leads_logout_time=request.POST['company_leads_logout_time']
        company_leads_employee_strength=request.POST['company_leads_employee_strength']
        company_leads_contact_person=request.POST['company_leads_contact_person']
        company_leads_designation=request.POST['company_leads_designation']
        company_leads_contact_mobile=request.POST['company_leads_contact_mobile']
        company_leads_contact_email=request.POST['company_leads_contact_email']
        Company_Leads.objects.create(company_leads_added_by = CustomUser.objects.get(pk=1),
                                    company_leads_pickup_location_id = Pickup_Location.objects.get(pk=int(company_leads_pickup_location_id)),
                                    company_leads_corporate_hub = company_leads_corporate_hub,
                                    company_leads_company_name = company_leads_company_name,
                                    company_leads_login_time = Login_Time.objects.get(pk=int(company_leads_login_time)),
                                    company_leads_logout_time = Logout_Time.objects.get(pk=int(company_leads_logout_time)),
                                    company_leads_employee_strength = company_leads_employee_strength,
                                    company_leads_contact_person = company_leads_contact_person,
                                    company_leads_designation = company_leads_designation,
                                    company_leads_contact_mobile = company_leads_contact_mobile,
                                    company_leads_contact_email = company_leads_contact_email)
    return render(request, 'marketing_tool_lead_manager_app/company_lead_form.html')

#</------------- Company Lead B2B View-------------------->






# class UpdateLeadTestView(CreateLeadTestView):
#   template_name = 'marketing_tool_lead_manager_app/update.html'
#   # Define 'update' action
#   action = 'update'
#   # Define 'update' button
#   button_text = 'Update'

''' def lead_zing_grid_list(request):
    return render(request,'marketing_tool_lead_manager_app/lead_zing_grid_list.html')


def routes_zing_grid_list(request):
    return render(request,'marketing_tool_lead_manager_app/routes_list_zinggrid.html')

 '''





#<------ Marketing Tool Trash Views -----

#Leads By City view
''' def leads_city(request):
    """All Leads By City (Mumbai) Page of webapp
    Parameters: HttpRequest object
    Returns : Nothing"""
    mumbai_leads_object = Leads.objects.all().filter(City='Mumbai')
    data ={'leads' : mumbai_leads_object}
    return render(request,'marketing_tool_lead_manager_app/mumbai_leads.html',data)
 '''

''' class CreateLeadTestView(HotView):
    # Define model to be used by the view
    model = Leads
    # Define template
    template_name = 'marketing_tool_lead_manager_app/create.html'
    # Define custom characters/strings for checked/unchecked checkboxes
    checkbox_checked = 'yes' # default: true
    checkbox_unchecked = 'no' # default: false
    # Define prefix for the formset which is constructed from Handsontable spreadsheet on submission
    prefix = 'table'
    # Define success URL
    success_url = reverse_lazy('update')
    # Define fields to be included as columns into the Handsontable spreadsheet
    fields = (
        'id',
        'City',
        'Name',
        'Gender',
        'EmailId',
        'ContactNo',
        'CompanyName',
        'Lead_Status',
    )
    # Define extra formset factory kwargs
    factory_kwargs = {
        'widgets': {
            'LocationFromOther': DateInput(attrs={'type': 'date'}),
            'Lead_Status': CheckboxSelectMultiple(),
            'is_valid': CheckboxInput(),
        }
    }
    # Define Handsontable settings as defined in Handsontable docs
    hot_settings = {
        'contextMenu': 'true',
        'autoWrapRow': 'true',
        'rowHeaders': 'true',
        'contextMenu': 'true',
        'search': 'true',
        # When value is dictionary don't wrap it in quotes
        'headerTooltips': {
            'rows': 'false',
            'columns': 'true'
        },
        # When value is list don't wrap it in quotes
        'dropdownMenu': [
            'remove_col',
            '---------',
            'make_read_only',
            '---------',
            'alignment'
        ]
    }
 '''


 #</------ Marketing Tool Trash Views -----

# def leads_status_details(request,pk):
    
#     return render(request,'loans_3m_crm_system_app/lead_detail_viewexperiment.html',data)
@login_required(login_url = '/Login')
def view_leads(request,pk):
    leads_list = Leads.objects.all()
    role =request.user.role
    leads = Leads.objects.get(pk=pk)
    leadstatus = Lead_Comment.objects.filter(lead_comment_id=leads).all()
    data = { 'leads' : leads,'leadstatus' : leadstatus}
    return render(request,'marketing_tool_lead_manager_app/view_leads.html',data)

@login_required(login_url = '/Login')
def add_new_lead_status(request,pk):
    # team_member_id=request.user.team_member_id
    if request.method == 'POST':
        lead_comment_id=request.POST['lead_comment_id']
        lead_comment_updated_by=request.POST['lead_comment_updated_by']
        lead_comment_name=request.POST['lead_comment_name']
        lead_comment_create_date=request.POST['lead_comment_create_date']
        lead_comment_remark=request.POST['lead_comment_remark']
        lead_comment_product_interested_in=request.POST['lead_comment_product_interested_in']
        lead_comment_next_followup_date=request.POST['lead_comment_next_followup_date']
        lead_object = Leads.objects.get(pk=lead_comment_id)
        CustomUser_object=CustomUser.objects.get(pk=lead_comment_updated_by)
        # leads=Leads.objects.all().filter(pk=lead_comment_id)
        Lead_Comment.objects.create(lead_comment_id = lead_object,
                                   lead_comment_updated_by = CustomUser_object,
                                   lead_comment_name = lead_comment_name,
                                   lead_comment_create_date=lead_comment_create_date,
                                   lead_comment_remark=lead_comment_remark,
                                   lead_comment_product_interested_in=lead_comment_product_interested_in,
                                   lead_comment_next_followup_date=lead_comment_next_followup_date)
                                #    lead_comment_Created_at=lead_comment_Created_at,
                                #    lead_comment_Updated_at=lead_comment_Updated_at)
    return HttpResponseRedirect(reverse('marketing_tool_lead_manager_app:view_leads',kwargs={'pk':pk}))

@method_decorator(login_required, name='dispatch')
class updatelead(BSModalUpdateView):
    model = Lead_Comment
    template_name = 'marketing_tool_lead_manager_app/updatelead.html'
    form_class = LeadCommentForm
    success_message = 'Success: Entry was updated.'
    def get_success_url(self,**kwargs):
        lead_comment_object = Lead_Comment.objects.get(pk=self.kwargs['pk'])
        lead_comment_id = int(str(lead_comment_object.lead_comment_id))
        return reverse_lazy('marketing_tool_lead_manager_app:view_leads', kwargs={'pk': lead_comment_id })

@method_decorator(login_required, name='dispatch')
class deletelead(BSModalDeleteView):
    model = Lead_Comment
    template_name = 'marketing_tool_lead_manager_app/deletelead.html'
    form_class = LeadCommentForm
    success_message = 'Success: Entry was updated.'
    def get_success_url(self,**kwargs):
        lead_comment_object = Lead_Comment.objects.get(pk=self.kwargs['pk'])
        lead_comment_id = int(str(lead_comment_object.lead_comment_id))
        return reverse_lazy('marketing_tool_lead_manager_app:view_leads', kwargs={'pk': lead_comment_id })