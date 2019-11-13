#--- Marketing Tool - Imported Packages List ----

#------Django Internal Packages-----
from django.urls import include, path,re_path
from django.contrib.auth import views as auth_views
#<------Django Internal Packages-----

#------ Marketing Tool Importing Project Files -----
#Marketing Tool - Our Application Views
from marketing_tool_lead_manager_app import views

#</--- Marketing Tool Importing Project Files ----

app_name = 'marketing_tool_lead_manager_app'




#--- Marketing Tool Data Management URL List ----
urlpatterns = [

# ------ Marketing Tool Index Form URLs -----

#Marketing Tool - Index Form
path("", views.survey_form, name="home"),

path('sentry-debug/', views.survey_form),
#Marketing Tool - Survey  Form
#path("survey_form", views.survey_form, name="survey_form"),

#Marketing Tool - Survey Form Submit
path("home_form_submit", views.home_form_submit, name="home_form_submit"),

#path("home_form_submit", views.home_form_submit, name="home_form_submit"),

#</------ Marketing Tool Index Form URLs -----

#------ Marketing Tool All Leads Urls -----

#Marketing Tool - Summary Page URL
#path("summary", views.summary, name="summary"),

#Marketing Tool - All Leads URL
path("leads", views.lead_zing_grid_list, name="lead_zing_grid_list"),

#</------ Marketing Tool All Leads Urls -----


#------ Marketing Tool Leads by City Urls -----

#Marketing Tool - Leads by City URL
path("leads/mumbai", views.lead_zing_grid_list_mumbai, name="lead_zing_grid_list_mumbai"),

#</------ Marketing Tool All Leads Urls -----

#<------ Marketing Tool All Routes Urls -----

#Marketing Tool - All Routes List
path("routes", views.all_routes, name="routes"),

#Marketing Tool - All Routes Details
path("routes/details", views.routes_details, name="routes_details"),

#Marketing Tool - Leads Details based on Location From, Location To, Login Time and Logout Time (Zinggrid Table)
path('leads/details/<int:location_from>/<int:location_to>/<int:login_time>/<int:logout_time>/',views.leads_locationfrom_locationto_logintime_logouttime,name='leads_locationfrom_locationto_logintime_logouttime'),

#Marketing Tool - Leads Details based on Location From, Location To, Login Time and Logout Time (Data Table)
path('leads/detail/<int:location_from>/<int:location_to>/<int:login_time>/<int:logout_time>/',views.leads_locationfrom_locationto_logintime_logouttime_dt,name='leads_locationfrom_locationto_logintime_logouttime_dt'),



#</------ Marketing Tool All Routes Urls -----

#<------ Marketing Tool City Routes Urls -----

#Marketing Tool - Mumbai Routes List
path("routes/city", views.leads_routes, name="leads_routes"),

#Marketing Tool - Mumbai Routes Details
path("routes/city/details", views.city_routes_details, name="city_routes_details"),


#</------ Marketing Tool City Routes Urls -----

#<------ Marketing Tool Location From Urls -----
#Marketing Tool - Location From
path("location_from", views.location_from, name="location_from"),

#</------ Marketing Tool Location From Urls -----

#<------ Marketing Tool Location To Urls -----
#Marketing Tool - Location To
path("location_to", views.location_to, name="location_to"),

#<------ Marketing Tool Location To Urls -----

#<------ Marketing Tool Login Time Urls -----
#Marketing Tool - Login Time
path("login_time", views.login_time, name="login_time"),

#</------ Marketing Tool Login Time Urls -----

#<------ Marketing Tool Logout Time Urls -----

#Marketing Tool - Logout Time
path("logout_time", views.logout_time, name="logout_time"),

#</------ Marketing Tool Logout Time Urls -----


#<------ Marketing Tool Portal Users Urls -----

#Marketing Tool - User List
path("users", views.users, name="users"),

#</------ Marketing Tool Portal Users Urls -----


#<------ Marketing Tool User Authentication Urls -----

#Marketing Tool - Sign In
path("Login", views.Login, name="Login"),


 #Marketing Tool - Sign Up
path("register", views.register, name="register"),

#Marketing Tool - Sign Up
path('sign_out/', views.user_sign_out, name = 'sign_out'),

#Marketing Tool - Forget Password
#path("forgetpassword" , views.forgetpassword, name="forgetpassword"),

#</------ Marketing Tool User Authentication Urls -----


#<------ Marketing Tool BS Modal Urls -----

#Marketing Tool - read url
path('read/<int:pk>', views.LeadReadView.as_view(), name='read_lead'),

#Marketing Tool - update url
path('update/<int:pk>', views.LeadUpdateView.as_view(), name='update_lead'),

#Marketing Tool - delete url
path('delete/<int:pk>', views.LeadDeleteView.as_view(), name='delete_lead'),

#Marketing Tool - location update
path('update/location/<int:pk>', views.LocationUpdateView.as_view(), name='update_location'),


#</------ Marketing Tool BS Modal Urls -----


#<------ Marketing Tool Rest API Urls -----

path('leads_api/', views.Leads_API.as_view(), name='leads_api2_list'),

path('leads_mumbai_api/', views.Leads_Mumbai_API.as_view(), name='Leads_Mumbai_API'),

path('routes/list', views.routes_list, name='routes_list'),

#</------ Marketing Tool Experiment URLS-----

path('routes/experiment', views.all_routes_experiment, name='all_routes_experiment'),

#</------ Marketing Tool :ead_status_details_url-----

#path('leads_status_details/<int:pk>', views.leads_status_details.as_view(), name='leads_status_details'),


#<------ Marketing Tool Zing Grid Test -----
#path('lead_zing_grid_list',views.lead_zing_grid_list,name='lead_zing_grid_list'),

#path('lead_zing_grid_list_mumbai',views.lead_zing_grid_list_mumbai,name='lead_zing_grid_list_mumbai'),

#path('routes_zing_grid_list',views.routes_zing_grid_list,name='routes_zing_grid_list'),	

#path('leads_api/details/<int:location_from>/<int:location_to>/<int:login_time>/<int:logout_time>/', views.leads_api_Details.as_view()),



#<------ Marketing Tool B2B Company Leads Urls -----

#Marketing Tool - Company Leads base 
path("company_lead_base", views.company_lead_base, name="company_lead_form"),


#Marketing Tool - Company Leads Form 
path("company/form", views.company_lead_form, name="company_lead_form"),

#Marketing Tool - Company Leads Data
path("company/leads", views.company_lead_data, name="company_lead_data"),

#Marketing Tool - Company Leads Report 
path("company/reports", views.company_lead_report, name="company_lead_report"),

#Marketing Tool - Company Leads Report 
path("company_lead_form_submit", views.company_lead_form_submit, name="company_lead_form_submit"),
#</------ Marketing Tool B2B Company Leads Urls -----

path("view_leads/<int:pk>", views.view_leads, name="view_leads"),

path("add_new_lead_status/<int:pk>",views.add_new_lead_status, name='add_new_lead_status'),

path('updatelead/<int:pk>',views.updatelead.as_view(),name='updatelead'),

path('deletelead/<int:pk>',views.deletelead.as_view(),name='deletelead'),

path('update_login_time/<int:pk>', views.update_login_time.as_view(), name='update_login_time'),

path('update_logout_time/<int:pk>', views.update_logout_time.as_view(), name='update_logout_time'),

path('update_login_time/<int:pk>', views.update_login_time.as_view(), name='update_login_time'),

path('delete_login_time/<int:pk>', views.delete_login_time.as_view(), name='delete_login_time'),

path('delete_logout_time/<int:pk>', views.delete_logout_time.as_view(), name='delete_logout_time'),

path('delete_pickup/<int:pk>', views.delete_pickup.as_view(), name='delete_pickup'),

path('delete_drop/<int:pk>', views.delete_drop.as_view(), name='delete_drop'),

path('Add_pickup/', views.Add_pickup.as_view(), name='Add_pickup'),

path('Add_drop/', views.Add_drop.as_view(), name='Add_drop'),

path('Add_login/', views.Add_login.as_view(), name='Add_login'),

path('Add_logout/', views.Add_logout.as_view(), name='Add_logout'),

path('Add_new_user/', views.Add_new_user.as_view(), name='Add_new_user'),

path('update_user/<int:pk>', views.update_user.as_view(), name='update_user'),

path('delete_user/<int:pk>', views.delete_user.as_view(), name='delete_user'),












]