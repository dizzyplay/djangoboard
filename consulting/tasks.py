from django.core.mail import send_mail
from django.template import loader
from background_task import background


@background(schedule=3)
def send_product_request_mail(post_dict):
    html_message = loader.render_to_string(
        'consulting/email_html.html', post_dict
    )
    # content = "\n".join([post.customer_name, post.customer_phone, post.project_info])
    send_mail(post_dict['customer_name'] + '님 안녕하세요', 'asdf', 'vovoboss@gmail.com',
              ['dizzyplay@naver.com', 'studiofroots@gmail.com'], html_message=html_message)

    # {
    #     'user_name': post.customer_name,
    #     'subject': post.project_info,
    #     'phone': post.customer_phone,
    #     'request_category': post.get_request_category_display,
    #     'email': post.customer_email,
    #     'price': post.customer_price,
    #     'request_date': post.customer_request_date,
    #     'delivery_date': post.customer_delivery_date,
    #     'memo': post.customer_memo
    # }
