from rest_framework import serializers
from marketing_tool_lead_manager_app import models



class LoginTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Login_Time
        fields = ("Time")

class LeadsSerializer(serializers.ModelSerializer):
    Login_Time_id = serializers.SlugRelatedField(
        read_only=True,
        slug_field='Time'
     )
    Pickup_Location_id = serializers.SlugRelatedField(
        read_only=True,
        slug_field='Location_Name'
     )
    Drop_Location_id = serializers.SlugRelatedField(
        read_only=True,
        slug_field='Drop_Name'
     )
    Logout_Time_id = serializers.SlugRelatedField(
        read_only=True,
        slug_field='Time'
     )

    class Meta:
        model = models.Leads
        fields = ['City','Name', 'EmailId','ContactNo', 'CompanyName','Pickup_Location_id','Drop_Location_id','Login_Time_id','Logout_Time_id']

class LeadsCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Leads
        fields = ('Name', 'EmailId','ContactNo', 'CompanyName','Pickup_Location_id','Drop_Location_id','Login_Time_id','Logout_Time_id')

class LeadsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Leads
        fields = ('City','Name', 'EmailId','ContactNo', 'CompanyName','TravalToWork','TravelToWorkOther','MonthlySpend','HearAboutUs','SubmittedOn','Lead_Status')