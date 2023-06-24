from django.contrib.auth.forms import UserCreationForm
from service.models import Cook


class CookForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience"
        )

    def __init__(self, *args, **kwargs) -> None:
        super(CookForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs[
            'placeholder'] = 'Enter your username'
        self.fields['password1'].widget.attrs[
            'placeholder'] = 'Enter your password'
        self.fields['password2'].widget.attrs[
            'placeholder'] = 'Confirm your password'
        self.fields['first_name'].widget.attrs[
            'placeholder'] = 'Enter your first name'
        self.fields['last_name'].widget.attrs[
            'placeholder'] = 'Enter your last name'
        self.fields['years_of_experience'].widget.attrs[
            'placeholder'] = 'Enter your years of experience'
