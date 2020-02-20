from .models import Revenue
from .models import Projectform
from django import forms
from django.utils.dateparse import parse_date
from datetime import datetime

class ProjectForm(forms.ModelForm):

    class Meta:
        model= Projectform
        fields=('project_name','user_name','phone_number','project_details','hour_rate')

class Postform(forms.ModelForm):
    class Meta:
        model = Revenue
        fields = ('project_name','start_time','end_time')
        
    def save(self, commit=True):
        instance = super(Postform, self).save(commit=False)
        end_time=self.cleaned_data['end_time']
        start_time=self.cleaned_data['start_time']
    
        time=datetime.strptime(end_time, '%Y/%m/%d %H:%M')
        end_time=time.hour
        end_date=time.day
        
        time=datetime.strptime(start_time, '%Y/%m/%d %H:%M')
        start_time=time.hour
        start_date=time.day
       

        date_diff=(end_date-start_date)*24
        spent_time=(end_time-start_time)+date_diff
    
        project_id=self.cleaned_data['project_name']
        print(project_id)
        ans=project_id.project_name
        print(ans)

        instance.spent_time=spent_time
        
        if commit:
            instance.save()
        return instance