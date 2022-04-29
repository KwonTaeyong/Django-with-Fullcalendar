from django import template

register = template.Library()


#
# @register.filter
# def datefomat(ori_date):
#
#
#
#     fi_date = ''
#
#
#     return fi_date


@register.filter
def sub(value, arg):
    return value - arg


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

