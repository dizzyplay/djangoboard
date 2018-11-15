from django.core.mail import send_mail
from django.template import loader
from background_task import background


@background(schedule=3)
def send_email_check(post_dict):
    mail_list = [post_dict['user_email']]

    html_message = loader.render_to_string(
        'users/check_email_form.html', post_dict
    )
    send_mail(post_dict['username'] + '님 안녕하세요', 'asdf', 'vovoboss@gmail.com',
              mail_list, html_message=html_message)
