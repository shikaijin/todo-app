from django import forms



# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()


class ForgetPwdForm(forms.Form):
    """Forget the password and try to find it"""
    email = forms.EmailField(label=u'User email', 
        widget=forms.EmailInput(attrs={'class':'form-control', 'id':'email','placeholder':u'Enter user email'}))
    pwd_1 = forms.CharField(label=u'Newpassword', max_length=36,
        widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'pwd_1','placeholder':u'Endter 6-36 length password'}))
    pwd_2 = forms.CharField(label=u'Enter angin', max_length=36,
        widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'pwd_2','placeholder':u'Enter new password again'}))
    check_code = forms.CharField(label=u'Verification Code', 
        widget=forms.TextInput(attrs={'class':'form-control', 'id':'check_code','placeholder':u'Enter Verification Code'}))