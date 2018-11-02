from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.


class ProductRequest(models.Model):
    PRODUCT_CATEGORY = (
        ('1', '브랜딩'),
        ('2', '편집디자인'),
        ('3', '웹디자인'),
        ('4', '패키징'),
        ('5', '기타')
    )
    customer_name = models.CharField(max_length=30, verbose_name='고객명')
    customer_phone = models.CharField(max_length=20, verbose_name='연락처')
    customer_email = models.EmailField(verbose_name='이메일')
    project_info = models.TextField(verbose_name='프로젝트 정보')
    request_category = MultiSelectField(min_choices=1, choices=PRODUCT_CATEGORY, blank=None, max_length=9,
                                        verbose_name='요청카테고리')
    customer_request_date = models.CharField(max_length=30, blank=True, verbose_name='시작날짜')
    customer_delivery_date = models.CharField(max_length=300, blank=True, verbose_name='마감날짜')
    customer_price = models.PositiveIntegerField(blank=True, verbose_name='예산', null=True)
    customer_memo = models.TextField(blank=True, verbose_name='메모')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def short_date(self):
        return str(self.created_at)[:19]


