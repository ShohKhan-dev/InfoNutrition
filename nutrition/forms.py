
from django import forms
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Div
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions



class SignUpForm(UserCreationForm):
    username = forms.CharField(min_length=3, label=_('Username'), validators=[validate_slug], max_length=30, error_messages={'invalid': _('Enter a valid username consisting of letters, numbers, underscores or hyphens')})
    first_name = forms.CharField(min_length=3, max_length=30, label=_('First name'))

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        helper = self.helper = FormHelper()

        layout = helper.layout = Layout()
        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs.update({'placeholder': _(field.label)})
            if field_name == 'password1':
                self.fields[field_name].help_text = '<small>' + str(_("Your password must contain at least 8 characters.")) + '</small>'
            else:
                self.fields[field_name].help_text = None
        helper.form_show_labels = False
        # for fieldname in ['username', 'password1', 'password2']:

    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        email = cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email', _("Email already exists"))
            # raise forms.ValidationError(_("Email already exists"), code='invalid')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')