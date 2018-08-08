
def select_action_from_list(nextInputs,interactive):
    if not interactive and len(nextInputs) == 1:
        return nextInputs[0]

    actionName = input('User must select an action: ' + ', '.join(list(nextInputs)) + ' : ')
    try:
        i = int(actionName)
        if 0 <= i < len(list(nextInputs)):
            return nextInputs[i]
        else:
            print('\tSelect a number from 0 to ', len(list(nextInputs)) -1)
            return select_action_from_list(nextInputs,interactive)
    except ValueError as e:
        pass

    if actionName in nextInputs:
        return actionName

    return select_action_from_list(nextInputs,interactive)


class SimpleRunner():
    def __init__(self):
        pass

    def run(self, automaton, interactive):
        print('Start from:\t', automaton.getCurrentState())
        while not automaton.isFinished():
            nextInputs = automaton.getCurrentState().getNextInputs()
            print("\tNext inputs:\t" + ', '.join(list(nextInputs)))
            actionName = select_action_from_list(nextInputs,interactive)
            automaton.doAction(actionName)
            automaton.move(actionName)
            print('Current State:\t',automaton.getCurrentState())

