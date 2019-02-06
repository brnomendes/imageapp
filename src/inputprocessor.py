
class InputProcessor:

    def __init__(self):
        pass

    def menu(self, filters, image_mode):
        print('This is an Image App\n')

        possibles = [filters[flag] for flag in filters if image_mode in filters[flag].types]

        if not possibles:
            print('Not avaliable filters')
            exit(0)

        choice_index = self._choice_a_filter(possibles)
        filter = possibles[choice_index]

        print(f'\nSelected Filter: {filter.name}\n')

        kwargs = self._get_filter_args(filter)

        return filter, kwargs

    def _choice_a_filter(self, possibles):
        """ Return 'possibles' index for the choice """

        print('Avaliable Filters:')
        for i, filter in enumerate(possibles):
            print(f'{i+1} - {filter.name}')

        option = 0
        while option <= 0 or option > len(possibles):
            try:
                option = int(input('\nType the selected filter number: '))
            except ValueError:
                continue

        return option - 1

    def _get_filter_args(self, filter):
        """ Return dict with args for the filter """

        kwargs = {}
        for arg in filter.args[1:]:
            kwargs[arg] = input(f'Type the {arg.replace("_", " ").title()}: ')
        return kwargs
