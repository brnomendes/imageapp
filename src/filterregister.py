import inspect


class FilterRegister:

    def get_register(self):
        return self._filter_register()

    def _filter_register(self):
        filters = {}

        def _register_decorator(name, types, help=None):
            """ Verifcations """
            def _wrapper(function):

                filters[function.__name__] = {}
                filters[function.__name__]['function'] = function
                filters[function.__name__]['args'] = list(inspect.signature(function).parameters.keys())
                filters[function.__name__]['name'] = name
                filters[function.__name__]['types'] = types
                filters[function.__name__]['help'] = help

                return function
            return _wrapper

        _register_decorator.filters = filters
        return _register_decorator


register = FilterRegister().get_register()
