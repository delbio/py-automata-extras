from automaton.scheduler import IContext


class Context(IContext):
    def __init__(self):
        self.mapping = {}
        self.context = {}
        pass

    def get_action_args(self, state, action_name):

        args = {}

        state_name = state.getName()
        state_handlers = self.mapping.get(state_name, None)
        if state_handlers is None:
            return args

        action_handlers = state_handlers.get(action_name, None)
        if action_handlers is None:
            return args

        mapping = action_handlers.get('args_mapping', None)
        if mapping is None:
            return args

        action_params = mapping.get('args', {})
        param_from_context_mapping = mapping.get('args_from_context', {})
        args = { **args, **action_params }

        for context_prop_name in param_from_context_mapping:
            param_name = param_from_context_mapping.get(context_prop_name, None)
            if param_name is None:
                raise ValueError('No param name founded into mapping for context prop: '+context_prop_name)
            args[param_name] = self.context.get(context_prop_name, None)

        return args

    def update(self, state, action_name, args, result):

        state_name = state.getName()
        state_handlers = self.mapping.get(state_name, None)
        if state_handlers is None:
            return None

        action_handlers = state_handlers.get(action_name, None)
        if action_handlers is None:
            return None

        mapping = action_handlers.get('result_mapping', None)
        if mapping is None:
            return None

        for context_prop_name in mapping:
            result_prop_name = mapping.get(context_prop_name, None)
            if result_prop_name is None:
                self.context[context_prop_name] = result
            else:
                self.context[context_prop_name] = result[result_prop_name]

        pass

