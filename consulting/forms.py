from django import forms
from .models import ProductRequest


class ProductRequestForm(forms.ModelForm):
    request_category = forms.MultipleChoiceField(choices = ProductRequest.PRODUCT_CATEGORY)

    class Meta:
        model = ProductRequest
        fields = [
            'customer_name',
            'customer_phone',
            'customer_email',
            'project_info',
            'request_category',
            'customer_request_date',
            'customer_delivery_date',
            'customer_price',
            'customer_memo',
        ]

        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': '성함'
            }),
            'customer_phone': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'ex)000-0000-0000'
            }),
            'customer_email': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'ex)example@example.com'
            }),
            'project_info': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': '9'
            }),
            'customer_request_date': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'customer_delivery_date': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
            }),
            'customer_price': forms.NumberInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder' : 'ex)숫자만 입력해주세요 (만원단위)',
            }),
            'customer_memo': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': '5'
            }),
        }
