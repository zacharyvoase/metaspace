"""
Create Python modules using class syntax.

Example:

    # in mymodule.py:
    class submodule(Namespace):
        abc = 123

    # somewhere else:
    >>> from mymodule.submodule import abc
    >>> abc
    123
"""

import sys
import types


class NamespaceMeta(type):
    def __new__(mcls, name, bases, attrs):
        if attrs.get('__metaclass__') is NamespaceMeta:
            return type.__new__(mcls, name, bases, attrs)
        module = types.ModuleType(name)
        if attrs['__module__'] == '__main__':
            attrs.pop('__module__')
            module.__dict__.update(attrs)
            sys.modules[name] = module
        else:
            module.__dict__.update(attrs)
            sys.modules[attrs['__module__'] + '.' + name] = module
        return module


class Namespace(object):

    __metaclass__ = NamespaceMeta
