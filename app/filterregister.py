import inspect


class Filter:
    """Model of a filter register.

    Args:
        function (:obj:`function`): Function to be registered.
        name (:obj:`str`): Name of the filter that will be displayed in the
            menu.
        types (:obj:`list` of :obj:`str`): Types of image mode that the filter
            supports.
        help (:obj:`str`): Message that will be displayed in the command line
            help.
    """

    def __init__(self, function, name, types, help):
        if function:
            self.function = function
            self.flag = self.function.__name__
            self.args = list(inspect.signature(self.function).parameters.keys())

        self.name = name
        self.types = types
        self.help = help


class FilterRegister:
    """Class that creates a register decorator."""

    def get_register(self):
        """Instance a new decorator to register filters.

        Returns:
            :obj:`function`: Decorator that register filters.
        """
        return self._filter_register()

    def _filter_register(self):
        """This function creates an empty dictionary and a decorator, every
        decorated function will be added to the dictionary.

        Returns:
            :obj:`function`: Decorator that register filters.
        """
        filters = {}

        def _register_decorator(name, types, help=None):
            def _wrapper(function):
                filters[function.__name__] = Filter(function, name, types, help)
                return function

            return _wrapper

        _register_decorator.filters = filters
        return _register_decorator


register = FilterRegister().get_register()
"""An instance of the decorator that will register the filters."""
