from .models import Leads,Pickup_Location,Drop_Location,Lead_Comment,Login_Time,Logout_Time,CustomUser
from bootstrap_modal_forms.mixins import PopRequestMixin,CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm
from django.contrib.auth.forms import UserCreationForm


class CustomUserForm(PopRequestMixin, CreateUpdateAjaxMixin,
                             UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'role','email', 'password1', 'password2')

class CustomUserUpdateForm(BSModalForm):
    class Meta:
        model = CustomUser
        fields = ['username','email']         

class LeadForm(BSModalForm):

    class Meta:
        model = Leads
        fields = ['Lead_Status','Pickup_Location_id','Drop_Location_id','Login_Time_id','Logout_Time_id','Remark',]

class UpdateLocationFrom(BSModalForm):
    class Meta:
        model = Pickup_Location
        fields = ('Location_Name',)

class UpdateLocationTo(BSModalForm):
    class Meta:
        model = Drop_Location
        fields = ['Drop_Name']

class LeadCommentForm(BSModalForm):
    class Meta:
        model = Lead_Comment
        fields = ['lead_comment_name','lead_comment_remark','lead_comment_product_interested_in','lead_comment_next_followup_date']

class Login_Time_form(BSModalForm):
    class Meta:
        model = Login_Time
        fields = ['Time']

class Logout_Time_form(BSModalForm):
    class Meta:
        model = Logout_Time
        fields = ['Time']

