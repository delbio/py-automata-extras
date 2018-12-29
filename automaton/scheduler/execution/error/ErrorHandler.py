from automaton.scheduler import IExecutionErrorHandler


class ActionExecutionErrorHandler(IExecutionErrorHandler):
    def __init__(self):
        self.mapping = {}
        pass

    def getErrorName(self, error):
        return error.__class__.__name__

    def handleError(self, state, actionName, error):
        state_name = state.getName()
        state_handlers = self.mapping.get(state_name, None)
        if state_handlers is None:
            raise error

        error_name = self.getErrorName(error)
        next_action = state_handlers.get(error_name, None)
        if next_action is None:
            raise error

        return next_action

