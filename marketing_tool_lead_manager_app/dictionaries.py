#------ Marketing Tool Internal Project Packages -----
from marketing_tool_lead_manager_app.models import Leads, CustomUser, Pickup_Location, Drop_Location, Login_Time, Logout_Time
from marketing_tool_lead_manager_app.forms import LeadForm,UpdateLocationFrom
from marketing_tool_lead_manager_app import count_functions
#</------ Marketing Tool Internal Project Packages -----

from marketing_tool_lead_manager_app import count_functions
from marketing_tool_lead_manager_app.models import Leads


def Total_Routes_Count(a,lead_status):
    """
    Gives the Count of all Leads from Database based on Lead Status and Dynamic Routes Generated
    Parameters: a ( tuple with - LocationFrom, LocationTo, LocationFromOther fields), lead_status ( Contacted, Uncontacted , Converted, Not Interested )
    Returns : count
    """
    count = Leads.objects.filter(Pickup_Location_id = a[0],Drop_Location_id = a[1],Login_Time_id=a[2],Logout_Time_id=a[3],Lead_Status=lead_status).all().count()
    return count


leads = Leads.objects.all()
x = list(set(list(Leads.objects.values_list('Pickup_Location_id', 'Drop_Location_id','Login_Time_id','Logout_Time_id'))))
lead_Status_list = ["Uncontacted","Undecided","Converted","Interested"]
total = [ count_functions.Total_Count_LeadStatus(x) for x in lead_Status_list ]
week = [ count_functions.Weekly_Count_LeadStatus(x) for x in lead_Status_list ]
month = [ count_functions.Monthly_Count_LeadStatus(x) for x in lead_Status_list ]
mumbai = [ count_functions.City_Count(x,"Mumbai") for x in lead_Status_list ]
kochi = [ count_functions.City_Count(x,"Kochi") for x in lead_Status_list ]
pune = [ count_functions.City_Count(x,"Pune") for x in lead_Status_list ]
banglore = [ count_functions.City_Count(x,"Banglore") for x in lead_Status_list ]
hyderabad = [ count_functions.City_Count(x,"Hyderabad") for x in lead_Status_list ]
calcutta = [ count_functions.City_Count(x,"Calcutta") for x in lead_Status_list ]
mumbai_dict = dict(zip(lead_Status_list, mumbai))
kochi_dict = dict(zip(lead_Status_list, kochi))
pune_dict = dict(zip(lead_Status_list, pune))
banglore_dict = dict(zip(lead_Status_list, banglore))
calcutta_dict = dict(zip(lead_Status_list, calcutta))
hyderabad_dict = dict(zip(lead_Status_list, hyderabad))
total_dict = dict(zip(lead_Status_list, total))
week_dict = dict(zip(lead_Status_list, week))
month_dict = dict(zip(lead_Status_list, month))
total_city_collect = { 'mumbai_all' : count_functions.Total_City_Count('Mumbai'), 'kochi_all' : count_functions.Total_City_Count('Kochi'), 'pune_all' : count_functions.Total_City_Count('Pune'), 'hyderabad_all' : count_functions.Total_City_Count('Hyderabad'), 'banglore_all' : count_functions.Total_City_Count('Banglore'), 'calcutta_all' : count_functions.Total_City_Count('Calcutta')}
total_collect = { 'all': count_functions.Total_Count(), 'week': count_functions.Weekly_Count(), 'month': count_functions.Montly_Count(),}
routes = [ count_functions.Total_Routes_Count(a,lead_status) for a in x for lead_status in lead_Status_list ]
final = [routes[i * 4:(i + 1) * 4] for i in range((len(routes) + 4 - 1) // 4 )]
routes_dict = dict(zip(x,final))




#<------ Marketing Tool Trash Variables -----
#routes = [ count_functions.Total_Routes_Count(a,lead_status) for a in x for lead_status in lead_Status_list ]
#final = [routes[i * 4:(i + 1) * 4] for i in range((len(routes) + 4 - 1) // 4 )]

#</------ Marketing Tool Trash Variables -----