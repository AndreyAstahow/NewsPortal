from django.core.mail import send_mail, EmailMultiAlternatives
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.loader import render_to_string

from .models import Post

@receiver(post_save, sender=Post)
def news_create(sender, instance, created, **kwargs):
        html_content = render_to_string(
                'html_email/news_created.html',
        )
        msg = EmailMultiAlternatives(
            subject = f'Привет! В твоем любимом разделе новая новость!',
            body = f'',
            from_email='andrey.astahow2016@yandex.ru',
            to = ['astakhoff.andrejj.yandex.ru208@gmail.com']
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()