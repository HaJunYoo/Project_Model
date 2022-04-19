from django import forms
from usermgmt.models import Member

# this is the option to show the form
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member # use Member model data base
        fields = '__all__' # use all attributes
        #field = ['salutation', 'first_name', 'last_name', 'email']
