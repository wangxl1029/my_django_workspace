import datetime
from django import template

register = template.Library()


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.inclusion_tag("img_uploader/includes/tag_line.html")
def show_tag_line(image):
    return {'img': image}
