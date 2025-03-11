from django import template
import re

register = template.Library()


@register.filter
def add_img_class(value):
    # Agrega la clase img-fluid a todas las imágenes dentro de figure
    value = re.sub(r'(<figure class="image">.*?<img [^>]*?)>', r'\1 class="img-fluid">', value, flags=re.DOTALL)
    return value
