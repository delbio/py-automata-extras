from automaton.placeholder import PlaceHolderAction
import os


class SingleResultAction(PlaceHolderAction):
    def __init__(self, originState, targetState):
        super(PlaceHolderAction, self).__init__(originState, targetState)
        pass

    def execute(self, source_queue_path, dest_queue_path):

        if source_queue_path is None:
            raise ValueError('source_queue_path is None')

        if dest_queue_path is None:
            raise ValueError('dest_queue_path is None')

        return os.path.join(dest_queue_path, 'test')


class DictionaryResultAction(PlaceHolderAction):
    def __init__(self, originState, targetState):
        super(PlaceHolderAction, self).__init__(originState, targetState)
        pass

    def execute(self, source_queue_path, dest_queue_path):

        if source_queue_path is None:
            raise ValueError('source_queue_path is None')

        if dest_queue_path is None:
            raise ValueError('dest_queue_path is None')

        return {
            'source': source_queue_path,
            'dest': dest_queue_path
        }


class ValidateActionResult(PlaceHolderAction):
    def __init__(self, originState, targetState):
        super(PlaceHolderAction, self).__init__(originState, targetState)
        pass

    def execute(self, file_path, dest_queue):
        print('validate_action_result', file_path, dest_queue)
        pass
