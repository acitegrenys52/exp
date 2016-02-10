import inspect
import re


def s(string):
    ns = inspect.stack()[1][0].f_locals
    my_dict = {}
    for k, v in ns.iteritems():
        if not k.startswith('__'):
            my_dict[k] = v
    result = re.finditer('\{(.+?)\}', string)

    for q in result:
        found = q.groups()[0]
        value = my_dict.get(found)
        if value:
            string = re.sub('\{' + found + '\}', str(value), string)
    return string
