from django import template
from django.contrib import auth

register = template.Library()
from products.models import Basket, Products
import datetime
from dateutil.relativedelta import relativedelta


@register.filter
def addedToBasket_check(user, product):
    basket = None
    try:
        basket = Basket.objects.get(auth_user=user, product=product)
    except:
        pass

    if (basket):
        return True
    else:
        return False


def addS(count):
    if abs(count) > 1:
        return 's'
    else :
        return ' '

@register.filter
def is_past_due(fdate):
    current_date = datetime.datetime.now().date()
    due_date = fdate - current_date
    due_days = due_date.days
    print due_date, due_days

    if due_days == 0:
        return 'Today'
    elif due_days == 1:
        return 'Tomorrow'
    elif due_days > 0:
        now = datetime.datetime.now()
        due = datetime.timedelta(due_days)
        ans = now - due
        print relativedelta(now, ans)
        delta = relativedelta(now, ans)

        years = delta.years;
        months = delta.months;
        weeks = delta.days / 7;
        days = delta.days % 7
        days_due = ''

        if years > 0:
            days_due += str(years) + ' - Year' + addS(years) + ', '
        if months > 0:
            days_due += str(months) + ' - Month' + addS(months) + ', '
        if weeks > 0:
            days_due += str(weeks) + ' - Week' + addS(weeks) + ', '
        if days > 0:
            days_due += str(days) + ' - Day' + addS(days) + ' '
        return days_due + 'left'
    elif due_days < 0:

        now = datetime.datetime.now()
        due = datetime.timedelta(abs(due_days))
        ans = now - due
        print relativedelta(now, ans)
        delta = relativedelta(now, ans)

        years = delta.years;
        months = delta.months;
        weeks = delta.days / 7;
        days = delta.days % 7
        days_due = ''

        if years > 0:
            days_due += str(years) + ' - Year' + addS(years) + ', '
        if months > 0:
            days_due += str(months) + ' - Month' + addS(months) + ', '
        if weeks > 0:
            days_due += str(weeks) + ' - Week' + addS(weeks) + ', '
        if days > 0:
            days_due += str(days) + ' - Day' + addS(days) + ' '
        return days_due + 'ago'
    else:
        return 'No days left'
