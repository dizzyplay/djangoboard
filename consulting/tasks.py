from django.core.mail import send_mail
from django.template import loader
from background_task import background


@background(schedule=3)
def send_product_request_mail(post_dict, send_author=False):
    mail_list = ['dizzyplay@naver.com', 'studiofroots@gmail.com']
    if send_author:
        mail_list.append(post_dict['customer_email'])

    html_message = loader.render_to_string(
        'consulting/email_html.html', post_dict
    )
    send_mail(post_dict['customer_name'] + '님 안녕하세요', 'asdf', 'vovoboss@gmail.com',
              mail_list, html_message=html_message)

