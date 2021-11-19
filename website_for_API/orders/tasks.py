from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    print("Фссузе!")
    order = Order.objects.get(id=order_id)
    subject = f'Заказ номер. {order_id}'
    message = 'Дорогой. {},\n\nYou have successfully placed an order.\
                Your order id is {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject,
                          message,
                          'dostavimvdom2@gmail.com',
                          [order.email])
    return mail_sent
