from email.policy import default
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username', 'password1', 'password2'
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = "form-control form-control-lg"
        # self.fields['username'].widget.attrs['id'] = "form3Example3cg"
        self.fields['password1'].widget.attrs['class'] = "form-control form-control-lg"
        self.fields['password2'].widget.attrs['class'] = "form-control form-control-lg"
        # self.fields['email'].widget.attrs['class'] = "form-control form-control-lg"


# class SignUpForm(forms.Form):
#     username = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput())

#     # class Meta:
#     #     model = User
#     #     fields = (
#     #         'username', 'password1', 'password2', 'email'
#     #     )

#     def __init__(self, *args, **kwargs):
#         super(SignUpForm, self).__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs['class'] = "form-control form-control-lg"
#         # self.fields['username'].widget.attrs['id'] = "form3Example3cg"
#         self.fields['password'].widget.attrs['class'] = "form-control form-control-lg"
#         # self.fields['password2'].widget.attrs['class'] = "form-control form-control-lg"
#         self.fields['email'].widget.attrs['class'] = "form-control form-control-lg"

gen_choice = (
    ('Not Mentioned', 'Not Mentioned'),
    ('Male', 'Male'),
    ('Female', 'Female')
)


class EditProfileForm(forms.ModelForm):
    gender = forms.TypedChoiceField(choices=gen_choice, widget=forms.Select(
        attrs={'class': 'form-control form-control-lg', 'aria-label': "Default"}
    ))

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email',
                  'gender', 'mobile', 'address', 'pro_pic']

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = "form-control form-control-lg"
        self.fields['last_name'].widget.attrs['class'] = "form-control form-control-lg"
        self.fields['email'].widget.attrs['class'] = "form-control form-control-lg"
        self.fields['mobile'].widget.attrs['class'] = "form-control form-control-lg"
        self.fields['address'].widget.attrs['class'] = "form-control form-control-lg"
        self.fields['pro_pic'].widget.attrs.update(
            {'class': "form-control form-control-lg", 'type': 'file'}
        )
