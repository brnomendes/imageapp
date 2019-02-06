import inspect


class Filter:

    def __init__(self, flag, function, args, name, types, help):
        self.flag = flag
        self.function = function
        self.args = args
        self.name = name
        self.types = types
        self.help = help


class FilterRegister:

    def get_register(self):
        return self._filter_register()

    def _filter_register(self):
        filters = {}

        def _register_decorator(name, types, help=None):
            """ Verifcations """
            def _wrapper(function):

                filters[function.__name__] = Filter(function.__name__, function, list(inspect.signature(function).parameters.keys()), name, types, help)

                return function
            return _wrapper

        _register_decorator.filters = filters
        return _register_decorator


register = FilterRegister().get_register()
