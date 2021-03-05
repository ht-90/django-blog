from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.conf import settings

# import modules for sign up email confirmation
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


# get_user_model is required rather than importing User directly from models
User = get_user_model()

subject = "Membership Sign Up Confirmation"
message_template = """
Thank you for joining the membership!
Please click the link below to complete member registration process!

"""

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    # called when user submit a creation form
    def save(self, commit=True):
        # initialize a user object but not save to db yet
        user = super().save(commit=False)
        # explicitly save email as it is not saved by default
        user.email = self.cleaned_data["email"]
        
        # Prevent log in until email confirmation is completed
        user.is_active = False

        if commit:
            user.save()
            activate_url = get_activate_url(user)
            message = message_template + activate_url
            user.email_user(subject, message)
        
        return user
    
def get_activate_url(user):
    # Encode user name and generate user token
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    return settings.FRONTEND_URL + "/activate/{}/{}/".format(uid, token)

def activate_user(uidb64, token):
    # Continue if user is found in database
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except Exception:
        return False
    # Activate user if token matches
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return True
    
    return False
