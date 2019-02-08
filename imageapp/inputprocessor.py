
class InputProcessor:
    """Allows the user to select a filter for the input image.

    This module is responsible for displaying the filters available to the
    user, then the user chooses the filter and sets the arguments.
    """

    def menu(self, filters, image_mode):
        """Displays a menu of options with the filters available for the
        image mode type.

        From the image mode, a menu is displayed for the user with the
        compatible filters to choose one. After choosing the filter, the
        required arguments are requested, then the chosen filter with the
        arguments is returned.

        Args:
            filters: (:obj:`dict` of :obj:`str:`
                :py:mod:`imageapp.filterregister.Filter`) -- List of registered
                filters.
            image_mode (:obj:`str`): Image mode type.

        Returns:
            (:obj:`function`, :obj:`dict` of :obj:`str:`:obj:`str`): Function
            of the chosen filter and a dictionary with the arguments provided
            by the user.

        """
        print('This is an Image App\n')

        possibles = [filters[flag] for flag in filters
                     if image_mode in filters[flag].types]

        if not possibles:
            print('Not avaliable filters')
            exit(0)

        filter = self._choice_a_filter(possibles)

        print(f'\nSelected Filter: {filter.name}\n')

        kwargs = self._get_filter_args(filter)

        return filter, kwargs

    def _choice_a_filter(self, possibles):
        """Allows the user to choose a filter compatible with the input image.

        Displays to the user a menu with the compatible filters, then waits
        for the user's choice, and then returns the chosen filter.

        Args:
            possibles: (:obj:`dict` of :obj:`str:`
                :py:mod:`imageapp.filterregister.Filter`) -- List of compatible
                filters.

        Returns:
            (:py:mod:`imageapp.filterregister.Filter`): Filter chosen by the
            user.
        """
        print('Avaliable Filters:')
        for i, filter in enumerate(possibles):
            print(f'{i+1} - {filter.name}')

        option = 0
        while option <= 0 or option > len(possibles):
            try:
                option = int(input('\nType the selected filter number: '))
            except ValueError:
                continue

        return possibles[option - 1]

    def _get_filter_args(self, filter):
        """Requires the arguments needed to apply the filter.

        For each argument required for the chosen filter, ask the user for
        the value.

        Args:
            filter (:py:mod:`imageapp.filterregister.Filter`): Filter chosen,
                in which you will be asked the necessary arguments.

        Returns:
            (:obj:`dict` of :obj:`str:`:obj:`str`): Dictionary of user
            arguments for the chosen filter.
        """
        kwargs = {}
        for arg in filter.args[1:]:
            kwargs[arg] = input(f'Type the {arg.replace("_", " ").title()}: ')
        return kwargs
