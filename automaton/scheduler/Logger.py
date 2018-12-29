from automaton.scheduler import IRunnerLogger


class ConsoleRunnerLogger(IRunnerLogger):
    def __init__(self, automaton, error_handler, next_action_selector, context, interactive):
        self.automaton = automaton
        self.interactive = interactive
        self.context = context
        pass

    def startExecution(self):
        print('Start from:\t', self.automaton.getCurrentState())
        pass

    def nextCurrentState(self, state):
        print('Current State:\t', state)
        pass

    def doAction(self, action_name, args):
        print('Exec Action: ', action_name, ' with args: ', args)
        pass

    def stopExecution(self):
        print('Stopped into:\t', self.automaton.getCurrentState())
        pass


