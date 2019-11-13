from marketing_tool_lead_manager_app.models import Leads
from datetime import date, datetime
import datetime
def Total_Count():
    """
    Gives the Total count of all Leads from Database
    Parameters: None
    Returns : count
    """
    # Get all Leads Count
    count = Leads.objects.all().count()
    return count

def Weekly_Count():
    """
    Gives the Count of all Leads from Database generated within Week
    Parameters: None
    Returns : count
    """
    today = datetime.datetime.now()
    week_start_date = today - datetime.timedelta(days=7)
    count = Leads.objects.filter(SubmittedOnDate__range=[week_start_date, today]).all().count()
    return count

def Montly_Count():
    """
    Gives the Count of all Leads from Database generated within Month
    Parameters: None
    Returns : count
    """
    today = datetime.datetime.now()
    month_start_date = today - datetime.timedelta(days=30)
    count = Leads.objects.filter(SubmittedOnDate__range=[month_start_date, today]).all().count()
    return count

def Total_Count_LeadStatus(lead_status):
    """
    Gives the Count of all Leads from Database based on Lead Status
    Parameters: lead_status ( Contacted, Uncontacted , Converted, Not Interested )
    Returns : count
    """
    count = Leads.objects.filter(Lead_Status=lead_status).all().count()
    return count

def Weekly_Count_LeadStatus(lead_status):
    """
    Gives the Count of all Leads from Database based on Lead Status generated within Week
    Parameters: lead_status ( Contacted, Uncontacted , Converted, Not Interested )
    Returns : count
    """
    today = datetime.datetime.now()
    week_start_date = today - datetime.timedelta(days=7)
    count = Leads.objects.filter(Lead_Status=lead_status).filter(SubmittedOnDate__range=[week_start_date, today]).all().count()
    return count

def Monthly_Count_LeadStatus(lead_status):
    """
    Gives the Count of all Leads from Database based on Lead Status generated within Month
    Parameters: lead_status ( Contacted, Uncontacted , Converted, Not Interested )
    Returns : count
    """
    today = datetime.datetime.now()
    month_start_date = today - datetime.timedelta(days=30)
    count = Leads.objects.filter(Lead_Status=lead_status).filter(SubmittedOnDate__range=[month_start_date, today]).all().count()
    return count

def City_Count(lead_status,city_name):
    """
    Gives the Count of all Leads from Database based on Lead Status and City
    Parameters: lead_status ( Contacted, Uncontacted , Converted, Not Interested ) , city_name ( Mumbai, Kochi, Pune, Banglore, Calcutta, Hyderabad )
    Returns : count
    """
    count = Leads.objects.filter(Lead_Status=lead_status).filter(City = city_name).all().count()
    return count

def Total_City_Count(city_name):
    """
    Gives the Count of all Leads from Database based on City
    Parameters: city_name ( Mumbai, Kochi, Pune, Banglore, Calcutta, Hyderabad )
    Returns : count
    """
    count = Leads.objects.filter(City = city_name).all().count()
    return count


def Total_Routes_Count(a,lead_status):
    """
    Gives the Count of all Leads from Database based on Lead Status and Dynamic Routes Generated
    Parameters: a ( tuple with - LocationFrom, LocationTo, LocationFromOther fields), lead_status ( Contacted, Uncontacted , Converted, Not Interested )
    Returns : count
    """
    count = Leads.objects.filter(Pickup_Location_id = a[0],Drop_Location_id = a[1],Login_Time_id=a[2],Logout_Time_id=a[3],Lead_Status=lead_status).all().count()
    return count