from automaton.scheduler import IExecutor


class ActionExecutor(IExecutor):
    def __init__(self):
        pass

    def execute(self, automaton, action_name, logger, error_handler, next_action_selector, context):
        try:
            state = automaton.getCurrentState()
            args = context.get_action_args(state, action_name)
            logger.doAction(action_name, args)
            result = automaton.doAction(action_name, **args)
            context.update(state, action_name, args, result)
            automaton.move(action_name)
            logger.nextCurrentState(automaton.getCurrentState())
        except Exception as e:
            if error_handler is None:
                raise e
            self.execute(
                automaton,
                error_handler.handleError(automaton.getCurrentState(), action_name, e),
                logger,
                error_handler,
                next_action_selector,
                context
            )
        pass


