from allauth.account.forms import SignupForm
from django.core.mail import mail_admins


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)

        mail_admins(
            subject='New user!',
            message=f'User {user.username} have registered on the website.'
        )

        return user