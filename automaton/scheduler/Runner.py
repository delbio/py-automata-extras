from automaton.scheduler import IRunner
from automaton.scheduler.execution.Executor import ActionExecutor
from automaton.scheduler.Logger import ConsoleRunnerLogger

class Runner(IRunner):
    def __init__(self):
        pass

    def run(self, automaton, error_handler, next_action_selector, context, interactive):
        result = ConsoleRunnerLogger(
            automaton, error_handler, next_action_selector, context, interactive
        )
        executor = ActionExecutor()
        result.startExecution()
        try:
            while not automaton.isFinished():
                action_name = next_action_selector.nextAction(automaton.getCurrentState(), interactive)
                executor.execute(
                    automaton,
                    action_name,
                    result,
                    error_handler,
                    next_action_selector,
                    context
                )
        finally:
            result.stopExecution()
