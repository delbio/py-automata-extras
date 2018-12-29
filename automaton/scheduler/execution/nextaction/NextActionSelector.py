from automaton.scheduler import INextActionSelector


class NoInteractiveModeNoMappingForMultipleNextInputError(ValueError):
    def __init__(self):
        # Call the base class constructor with the parameters it needs
        super().__init__('Not interactive mode, mutliple action available, no mapping setted')


def select_action_from_list_recursive_interactive(nextInputs):
    actionName = input('User must select an action: ' + ', '.join(list(nextInputs)) + ' : ')
    try:
        i = int(actionName)
        if 0 <= i < len(list(nextInputs)):
            return nextInputs[i]
        else:
            print('\tSelect a number from 0 to ', len(list(nextInputs)) - 1)
            return select_action_from_list_recursive_interactive(nextInputs)
    except ValueError as e:
        pass

    if actionName in nextInputs:
        return actionName

    return select_action_from_list_recursive_interactive(nextInputs)


class NextActionSelector(INextActionSelector):
    def __init__(self):
        self.mapping = {}
        pass

    def nextAction(self, state, interactive):
        nextInputs = state.getNextInputs()
        print("\tNext inputs:\t" + ', '.join(list(nextInputs)))
        if not interactive and len(nextInputs) == 1:
            return nextInputs[0]

        if not interactive:
            print("\tMapping:\t", self.mapping)
            action_name = self.mapping.get(state.getName(), None)
            if action_name is None:
                raise NoInteractiveModeNoMappingForMultipleNextInputError()
            else:
                return action_name

        return select_action_from_list_recursive_interactive(nextInputs)

