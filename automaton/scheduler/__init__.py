import abc
import inspect


class IRunner(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self, automaton, error_handler, next_action_selector, context, interactive):
        raise NotImplementedError('users must define ' + inspect.stack()[0][3] + ' to use this base class')


class IRunnerLogger(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def startExecution(self):
        raise NotImplementedError('users must define ' + inspect.stack()[0][3] + ' to use this base class')

    @abc.abstractmethod
    def nextCurrentState(self, state):
        raise NotImplementedError('users must define ' + inspect.stack()[0][3] + ' to use this base class')

    @abc.abstractmethod
    def doAction(self, action_name, args):
        raise NotImplementedError('users must define ' + inspect.stack()[0][3] + ' to use this base class')

    @abc.abstractmethod
    def stopExecution(self):
        raise NotImplementedError('users must define ' + inspect.stack()[0][3] + ' to use this base class')


class IExecutor(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self, automaton, action_name, logger, error_handler, next_action_selector, context):
        raise NotImplementedError('users must define ' + inspect.stack()[0][3] + ' to use this base class')


class INextActionSelector(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def nextAction(self, state, interactive):
        raise NotImplementedError('users must define ' + inspect.stack()[0][3] + ' to use this base class')


class IExecutionErrorHandler(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getErrorName(self, error):
        raise NotImplementedError('users must define ' + inspect.stack()[0][3] + ' to use this base class')

    @abc.abstractmethod
    def handleError(self, state, actionName, error):
        raise NotImplementedError('users must define ' + inspect.stack()[0][3] + ' to use this base class')


class IContext(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_action_args(self, state, action_name):
        raise NotImplementedError('users must define ' + inspect.stack()[0][3] + ' to use this base class')

    @abc.abstractmethod
    def update(self, state, action_name, args, result):
        raise NotImplementedError('users must define ' + inspect.stack()[0][3] + ' to use this base class')

