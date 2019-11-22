from django import forms
from Users.models import User, Ministry


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user_type', 'username',)

        labels = {
            'user_type': 'نوع المستخدم',
            'username': 'اسم المستخدم',
        }

        widgets = {
            'user_type': forms.Select(
                attrs={'name': 'username', 'type': 'text', 'class': 'form-control'}),
            'username': forms.TextInput(
                attrs={'name': 'username', 'type': 'text', 'class': 'form-control', 'placeholder': 'اسم المستخدم'
                    , 'onkeypress': "return (event.charCode >= 65 && event.charCode <= 90) || (event.charCode >= 97 "
                                    "&& event.charCode <= 122) || (event.charCode >= 46 && event.charCode <= 57) "
                    , 'onkeyup': "this.value = this.value.toLowerCase()"}),
        }

        help_texts = {
            'username': 'أحرف , أرقام , و . /',
        }


class MinistryCreateForm(forms.ModelForm):
    class Meta:
        model = Ministry
        fields = ('ministry_name',)
        labels = {
            'ministry_name': 'اسم الوزاره'
        }
        widgets = {
            'ministry_name': forms.TextInput(attrs={'class':'form-control'})
        }