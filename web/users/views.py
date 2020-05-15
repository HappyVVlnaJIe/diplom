from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import CustomUserCreationForm,UserEditForm
from .tokens import account_activation_token


@login_required
def root_view(request):
    response = redirect('/settings')
    return response

@login_required
def profile_view(request):
    return render(request, 'profile/profile.html')

@login_required
def business_trip_view(request):
    return render(request, 'profile/business_trip.html')

@login_required
def documents_view(request):
    return render(request, 'profile/documents.html')

@login_required
def settings_view(request):
    return render(request, 'profile/settings.html')

def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Активируйте свой аккаунт на сайте {}'.format(current_site.domain)
            message = render_to_string('registration/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'registration/message.html', {
                'message': 'Пожалуйста, подтвердите свой адрес электронной почты, чтобы закончить регистрацию'})
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'registration/message.html', {
            'message': 'Спасибо за подтверждение адреса электронной почты. Теперь вы можете войти в систему'})
    else:
        return render(request, 'registration/message.html', {'message': 'Ссылка активации не подходит!'})

@login_required
def edit(request):
    if request.method == 'POST':

        user_form = UserEditForm(instance=request.user, data=request.POST)
        user_form.id=request.user.username
        print('user_form.id:')
        print(user_form.id)
        if user_form.is_valid() and user_form.email_is_valid(user_form.id):
            user_form.save()


    else:
        user_form = UserEditForm(instance=request.user)
        user_form.id=request.user.username

    return render(request,
                      'profile/settings.html',
                      {'form': user_form,})