from django import template

register = template.Library()


@register.filter(name="desconto_10")
def desconto_10(valor):
    return valor * 0.9


@register.filter(name="remover")
def remover(texto, sai):
    return texto.replace(sai, "")


@register.filter(name="pertence_ao")
def pertence_ao(usuario, grupo):
    g = usuario.groups.filter(name=grupo)
    if(g.exists()):
        return True
    return False


@register.simple_tag(name="substituir")
def substituir(texto, sai, entra, sai2="", entra2=""):
    return texto.replace(sai, entra).replace(sai2, entra2)
