from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, send_mail
from django.template import loader
from .forms import ProductRequestForm


def main_view(request):
    return render(request, './consulting/project_requirements_form.html')


def test_view(request):
    if request.method == 'POST':
        form = ProductRequestForm(request.POST)
        if form.is_valid():
            post = form.save()
            html_message = loader.render_to_string(
                'consulting/email_html.html',
                {
                    'user_name':post.customer_name,
                    'subject': post.project_info,
                    'phone': post.customer_phone,
                    'request_category': post.get_request_category_display,
                    'email':post.customer_email,
                    'price':post.customer_price,
                    'request_date': post.customer_request_date,
                    'delivery_date': post.customer_delivery_date,
                    'memo': post.customer_memo
                }
            )
            content = "\n".join([post.customer_name, post.customer_phone, post.project_info])
            # email = EmailMessage(post.customer_name+'님의 요청입니다', str(content) , to=['dizzyplay@naver.com'])
            send_mail(post.customer_name+'님 안녕하세요','asdf','vovoboss@gmail.com',['dizzyplay@naver.com','studiofroots@gmail.com'],html_message=html_message)
            print(post)
            # email.send()
            return redirect('consulting:test_view')
    else:
        form = ProductRequestForm()
    return render(request, './consulting/test.html',{
        'form': form
    })


