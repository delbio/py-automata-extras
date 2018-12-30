from automaton.scheduler.execution.error.ErrorHandler import ActionExecutionErrorHandler
from automaton.builder.xml import getClassFromElement, getclass, setPropertyOnObject

class ErrorHandlerXmlBuilder():
    def __init__(self):
        pass

    def newObjectFromXmlElement(self, element):
        root_node = element.find('Error')
        # handler = getClassFromElement(element)()
        handler = ActionExecutionErrorHandler()
        if root_node is None:
            return handler

        setPropertyOnObject('Property', root_node, handler)

        state_nodes = root_node.findall('States/State')
        for stateElement in state_nodes:
            state_name = stateElement.attrib['name']
            handler.mapping[state_name] = {}

            errorHandlerOnStateNodes = stateElement.findall('Handler')
            for mapElement in errorHandlerOnStateNodes:
                error_class = mapElement.attrib['error']
                action_name = mapElement.attrib['action']
                handler.mapping[state_name][error_class] = action_name

        return handler
