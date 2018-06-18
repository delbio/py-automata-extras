
class SimpleRunner():
    def __init__(self):
        pass

    def run(self, automaton):
        print('Start from:\t', automaton.getCurrentState())
        while not automaton.isFinished():
            nextInputs = automaton.getCurrentState().getNextInputs()
            print("\tNext inputs:\t" + ', '.join(list(nextInputs)))
            actionName = None
            if len(nextInputs) == 1:
                actionName = nextInputs[0]
            else:
                actionName = input('User must select an action: ' + ', '.join(list(nextInputs)) + ' : ')
            automaton.doAction(actionName)
            automaton.move(actionName)
            print('Current State:\t',automaton.getCurrentState())

