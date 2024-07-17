#
#
import inspect

from pages.technical_evaluation_tab import Edit_TE


def get_methods(cls):
    methods = []
    for name, obj in inspect.getmembers(cls):
        if inspect.isfunction(obj) or inspect.ismethod(obj):
            methods.append(str(cls.__name__.lower()) + '_steps' + '.' + name + '(browser)')

    methods_str = "\n".join(methods)
    return methods_str

print(get_methods(Edit_TE))