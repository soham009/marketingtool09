from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from marketing_tool_lead_manager_app.models import Leads, CustomUser, Drop_Location, Pickup_Location,Login_Time,Logout_Time, Company_Leads

# Register your models here.

class LeadsAdmin(ImportExportModelAdmin):
    search_fields = ["Name","CompanyName"]
    list_filter = ["Lead_Status", "CompanyName"]
    list_display = [
        "pk",
        "SubmittedOnDate",
        "City",
        "Name",
        "Gender",
        "EmailId",
        "ContactNo",
        "CompanyName",
        "Pickup_Location_id",
        "Drop_Location_id",
        "Login_Time_id",
        "Logout_Time_id",
        "Lead_Status",
        "Remark",
    ]
    list_editable = ["Lead_Status","Remark"]

class Drop_LocationAdmin(ImportExportModelAdmin):
    search_fields = ["pk","Drop_Location_id"]
    list_display = [
        "pk",
        "Drop_Name",
    ]
    list_editable = ["Drop_Name"]

class Pickup_LocationAdmin(ImportExportModelAdmin):
    search_fields = ["pk","Pickup_Location_id"]
    list_display = [
        "pk",
        "Location_Name",
    ]
    list_editable = ["Location_Name"]

class Login_TimeAdmin(ImportExportModelAdmin):
    search_fields = ["pk","Login_Time_id"]
    list_display = [
        "pk",
        "Time",
    ]
    list_editable = ["Time"]

class Logout_TimeAdmin(ImportExportModelAdmin):
    search_fields = ["pk","Logout_Time_id"]
    list_display = [
        "pk",
        "Time",
    ]
    list_editable = ["Time"]

class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ["pk","name"]
    list_display = [
        "pk",
        "role",
        "name",
    ]
    list_editable = ["role","name"]


admin.site.register(Leads,LeadsAdmin)
admin.site.register(Drop_Location,Drop_LocationAdmin)
admin.site.register(Pickup_Location,Pickup_LocationAdmin)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Login_Time,Login_TimeAdmin)
admin.site.register(Logout_Time,Logout_TimeAdmin)
admin.site.register(Company_Leads)

admin.site.site_header = "Marketing Tool"
admin.site.site_title = "Marketing Tool"
admin.site.index_title = "Welcome to Marketing Tool"

