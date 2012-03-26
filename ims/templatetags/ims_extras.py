__author__ = 'agbetunsin'

from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.utils import simplejson
from django.utils.safestring import mark_safe
from django import template

register = template.Library()

def jsonify(object):
    """
    Usage:
    {{ some_data|jsonify }}
    """
    if isinstance(object, QuerySet):
        return mark_safe(serialize('json', object))
    return mark_safe(simplejson.dumps(object))

register.filter('jsonify', jsonify)
jsonify.is_safe = True



#@register.tag
def do_datalist(parser, token):
    """
    Renders a collection of options in a datalist tag

    Example::
        {% datalist id collection %}
    """
    bits = list(token.split_contents())
    if len(bits) < 2:
        raise template.TemplateSyntaxError("%r takes at least two arguments" % bits[0])
    val1 = parser.compile_filter(bits[1])
    try:
        val2 = parser.compile_filter(bits[2])
    except IndexError:
        val2 = None
    return DataListNode(val1, val2)
do_datalist= register.tag('datalist', do_datalist)

class DataListNode(template.Node):
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def render(self, context):
        var1 = self.var1.resolve(context, True)

        if self.var2 is None:
            from ims import models
            if   var1 == 'year':
                var2 = [x for x,y in models.YEARS]
            elif var1 == 'status':
                var2 = [x for x,y in models.STATUS]
            elif var1 == 'sector':
                var2 = [x for x,y in models.SECTORS]
            elif var1 == 'industry':
                var2 = models.Industry.objects.all()
            elif var1 == 'duration':
                var2 = (1, 2, 5, 7, 10, 15)
            elif var1 == 'cost':
                var2 = (100000, 1000000, 5000000, 10000000, 50000000, 100000000)
            else:
                var2 = list()
        else:
            var2 = self.var2.resolve(context, True)

        datalist = '<select name="%s"><option>%s %s</option>' % (var1, 'Any', var1)
        for x in var2:
            datalist += '<option value="%s">%s</option>' % (x,x)
        datalist += '</select>'
        return datalist


#@register.tag
def do_operatorlist(parser, token):
    """
    Renders a set equality operators in an options select tag

    Example::
        {% operatorlist id %}
    """
    bits = list(token.split_contents())
    if len(bits) < 1:
        raise template.TemplateSyntaxError("%r takes at least one argument" % bits[0])
    val1 = parser.compile_filter(bits[1])
    return OperatorListNode(val1)
do_operatorlist= register.tag('operatorlist', do_operatorlist)


class OperatorListNode(template.Node):
    def __init__(self, var1):
        self.var1 = var1

    def render(self, context):
        var1 = self.var1.resolve(context, True)
        operatorlist = '<select name="%s">' % var1
        operators = [('==','Equals'),('<','Less than'),('<=','Less than/Equals'),\
            ('>=','Greater than/Equals'),('>','Greater than')]
        for x,y in operators:
            operatorlist += '<option value="%s">%s</option>' % (x,y)
        operatorlist += '</select>'
        return operatorlist