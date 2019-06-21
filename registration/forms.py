from django import forms
from django.core.validators import validate_email
import re
# from .getpost import getid


class RegisterForm(forms.Form):
    RFirstName = forms.CharField(label='RFirstName', max_length=100)
    RLastName = forms.CharField(label='RLastName', max_length=100)
    RID = forms.CharField(label='RID', max_length=9)
    RDateOfBirth = forms.CharField(label='RDateOfBirth', max_length=100)
    email = forms.CharField(label='email', max_length=100)
    RPassword = forms.CharField(label='RPassword', max_length=100)
    diabetes = forms.BooleanField(label='diabetes', initial=False, required=False)

    def check_RID(self):
        if len(self.data['RID']) != 9:
            return False
        else:
            return True

    def check_mail(self):
        # if validate_email(self.data['email']):
        if re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', self.data['email'], re.I):
            return True
        else:
            return False

    def is_valid(self):
        valid = super(RegisterForm,self).is_valid()
        if valid and self.check_RID() and self.check_mail():
            return True
        else:
            return False


class LoginForm(forms.Form):
    RID = forms.CharField(label='ID', max_length=9)
    RPassword = forms.CharField(label='Password', max_length=100)

    def check_RID(self):
        if len(self.data['RID']) != 9:
            return False
        else:
            return True

    def is_valid(self):
        valid = super(LoginForm,self).is_valid()
        if valid and self.check_RID():
            return True
        else:
            return False
    
class SetBloodForm(forms.Form):
    CHOICES = [('f','f')]
    RID = forms.ChoiceField(label='RID',widget=forms.Select, choices=CHOICES)
    RID.widget.attrs.update({'class': 'form-control'})
    Glucose = forms.DecimalField(label='Glucose', max_value=10, min_value=0, decimal_places=2)
    Urea = forms.DecimalField(label='Urea', max_value=10, min_value=0, decimal_places=2)
    Creatinine = forms.DecimalField(label='Creatinine', max_value=10, min_value=0, decimal_places=2)
    eGFR = forms.DecimalField(label='eGFR', max_value=10, min_value=0, decimal_places=2)
    UricAcid = forms.DecimalField(label='UricAcid', max_value=10, min_value=0, decimal_places=2)
    Potassium = forms.DecimalField(label='Potassium', max_value=10, min_value=0, decimal_places=2)
    Sodium = forms.DecimalField(label='Sodium', max_value=10, min_value=0, decimal_places=2)
    Calcium = forms.DecimalField(label='Calcium', max_value=10, min_value=0, decimal_places=2)
    Phosphore = forms.DecimalField(label='Phosphore', max_value=10, min_value=0, decimal_places=2)
    Magnesium = forms.DecimalField(label='Magnesium', max_value=10, min_value=0, decimal_places=2)
    Cholesterol = forms.DecimalField(label='Cholesterol', max_value=10, min_value=0, decimal_places=2)
    Triglycerides = forms.DecimalField(label='Triglycerides', max_value=10, min_value=0, decimal_places=2)
    Protein = forms.DecimalField(label='Protein', max_value=10, min_value=0, decimal_places=2)
    Bilirubin_b = forms.DecimalField(label='Bilirubin_b', max_value=10, min_value=0, decimal_places=2)
    Alkaline_Phosphatase = forms.DecimalField(label='Alkaline_Phosphatase', max_value=10, min_value=0, decimal_places=2)
    ALT = forms.DecimalField(label='ALT', max_value=10, min_value=0, decimal_places=2)

    def check_RID(self):
        if len(self.data['RID']) != 9:
            return False
        else:
            return True
        
    def is_valid(self):
        valid = super(SetBloodForm,self).is_valid()
        if valid and self.check_RID():
            return True
        else:
            return False


class SetUrineForm(forms.Form):
    CHOICES = [('f','f')]
    RID = forms.ChoiceField(label='RID',widget=forms.Select, choices=CHOICES)
    RID.widget.attrs.update({'class': 'form-control'})
    # RID = forms.CharField(label='RID', max_length=9)
    PH = forms.DecimalField(label='PH', max_value=10, min_value=0, decimal_places=2)
    Nitrit = forms.DecimalField(label='Nitrit', max_value=10, min_value=0, decimal_places=2)
    Ketone = forms.DecimalField(label='Ketone', max_value=10, min_value=0, decimal_places=2)
    Urobilinogen = forms.DecimalField(label='Urobilinogen', max_value=10, min_value=0, decimal_places=2)
    Bilirubin = forms.DecimalField(label='Bilirubin', max_value=10, min_value=0, decimal_places=2)
    Leucocytes = forms.DecimalField(label='Leucocytes', max_value=10, min_value=0, decimal_places=2)
    Erythrocytes = forms.DecimalField(label='Erythrocytes', max_value=10, min_value=0, decimal_places=2)
    Albumin = forms.DecimalField(label='Albumin', max_value=10, min_value=0, decimal_places=2)

    def check_RID(self):
        if len(self.data['RID']) != 9:
            return False
        else:
            return True
        
    def is_valid(self):
        valid = super(SetUrineForm,self).is_valid()
        if valid and self.check_RID():
            return True
        else:
            return False

class SetDiabeteForm(forms.Form):
    CHOICES = [('f','f')]
    RID = forms.ChoiceField(label='RID',widget=forms.Select, choices=CHOICES)
    RID.widget.attrs.update({'class': 'form-control'})
    Glucose = forms.DecimalField(label='Glucose', max_value=10, min_value=0, decimal_places=2)
    Albumin = forms.DecimalField(label='Albumin', max_value=10, min_value=0, decimal_places=2)
    FGP = forms.DecimalField(label='FGP', max_value=10, min_value=0, decimal_places=2)
    RPG = forms.DecimalField(label='RPG', max_value=10, min_value=0, decimal_places=2)
    CGTT = forms.DecimalField(label='CGTT', max_value=10, min_value=0, decimal_places=2)
    CapillaryGlucose = forms.DecimalField(label='CapillaryGlucose', max_value=10, min_value=0, decimal_places=2)
    HBA1C = forms.DecimalField(label='HBA1C', max_value=10, min_value=0, decimal_places=2)
    Urea = forms.DecimalField(label='Urea', max_value=10, min_value=0, decimal_places=2)
    Creatinine = forms.DecimalField(label='Creatinine', max_value=10, min_value=0, decimal_places=2)
    eGFR = forms.DecimalField(label='eGFR', max_value=10, min_value=0, decimal_places=2)
    UricAcid = forms.DecimalField(label='UricAcid', max_value=10, min_value=0, decimal_places=2)
    Potassium = forms.DecimalField(label='Potassium', max_value=10, min_value=0, decimal_places=2)
    Sodium = forms.DecimalField(label='Sodium', max_value=10, min_value=0, decimal_places=2)
    Calcium = forms.DecimalField(label='Calcium', max_value=10, min_value=0, decimal_places=2)
    Phosphore = forms.DecimalField(label='Phosphore', max_value=10, min_value=0, decimal_places=2)
    Magnesium = forms.DecimalField(label='Magnesium', max_value=10, min_value=0, decimal_places=2)
    Cholesterol = forms.DecimalField(label='Cholesterol', max_value=10, min_value=0, decimal_places=2)
    Triglycerides = forms.DecimalField(label='Triglycerides', max_value=10, min_value=0, decimal_places=2)
    Protein = forms.DecimalField(label='Protein', max_value=10, min_value=0, decimal_places=2)
    Bilirubin_b = forms.DecimalField(label='Bilirubin_b', max_value=10, min_value=0, decimal_places=2)
    Alkaline_Phosphatase = forms.DecimalField(label='Alkaline_Phosphatase', max_value=10, min_value=0, decimal_places=2)
    ALT = forms.DecimalField(label='ALT', max_value=10, min_value=0, decimal_places=2)


    def check_RID(self):
        if len(self.data['RID']) != 9:
            return False
        else:
            return True
        
    def is_valid(self):
        valid = super(SetDiabeteForm,self).is_valid()
        if valid and self.check_RID():
            return True
        else:
            return False
