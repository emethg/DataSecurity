from django import forms


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

    def is_valid(self):
        valid = super(RegisterForm,self).is_valid()
        if valid and self.check_RID():
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
    RID = forms.CharField(label='RID', max_length=100)
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
    RID = forms.CharField(label='RID', max_length=100)
    PH = forms.CharField(label='PH', max_length=100)
    Nitrit = forms.CharField(label='Nitrit', max_length=100)
    Ketone = forms.CharField(label='Ketone', max_length=100)
    Urobilinogen = forms.CharField(label='Urobilinogen', max_length=100)
    Bilirubin = forms.CharField(label='Bilirubin', max_length=100)
    Leucocytes = forms.CharField(label='Leucocytes', max_length=100)
    Erythrocytes = forms.CharField(label='Erythrocytes', max_length=100)
    Albumin = forms.CharField(label='Albumin', max_length=100)

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
    RID = forms.CharField(label='RID', max_length=100)
    Glucose = forms.CharField(label='Glucose', max_length=100)
    Albumin = forms.CharField(label='Albumin', max_length=100)
    FGP = forms.CharField(label='FGP', max_length=100)
    RPG = forms.CharField(label='RPG', max_length=100)
    CGTT = forms.CharField(label='CGTT', max_length=100)
    CapillaryGlucose = forms.CharField(label='CapillaryGlucose', max_length=100)
    HBA1C = forms.CharField(label='HBA1C', max_length=100)

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
