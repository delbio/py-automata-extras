from automaton.core.Action import Action


class PlaceHolderAction(Action):
    def __init__(self, originState, targetState=None):
        self.actionName = None
        super(PlaceHolderAction, self).__init__(originState, targetState)
        pass

    def getName(self):
        return self.actionName

    def execute(self, *arg):
        print(self.getName())
        pass

from automaton.core.State import State

class PlaceHolderState(State):
    def __init__(self):
        self.stateName = None
        super(PlaceHolderState, self).__init__()
        pass

    def getName(self):
        return self.stateName


