from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(UserCreationForm):
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length=50)

    class Meta:
        # model = User
        fields = ['email', 'password']