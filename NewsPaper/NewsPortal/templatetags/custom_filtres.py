from django import template

register = template.Library()

@register.filter()
def censor(value):
    val = value.split()
    text = []
    for i in val:
        if i.istitle():
            text.append(i[0] + '*' * len(i))
        else:
            text.append(i)
    return f'{" ".join(text)}'