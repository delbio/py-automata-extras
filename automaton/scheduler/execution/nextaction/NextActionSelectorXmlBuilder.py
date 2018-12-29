from automaton.scheduler.execution.nextaction.NextActionSelector import NextActionSelector
from automaton.builder.common import getClassFromElement, getclass, setPropertyOnObject


# Per le esecuzioni non interattive
# se e' presente piu' di una azione in uscita
# in un mapping deve essere definita la azione da usare

class NextActionSelectorXmlBuilder():
    def __init__(self):
        pass

    def newObjectFromXmlElement(self, element):
        root_node = element.find('ActionSelector')
        # handler = getClassFromElement(element)()
        handler = NextActionSelector()
        if root_node is None:
            return handler

        setPropertyOnObject('Property', root_node, handler)

        state_nodes = root_node.findall('States/State')
        for stateElement in state_nodes:
            state_name = stateElement.attrib['name']
            action_name = stateElement.text
            handler.mapping[state_name] = action_name

        return handler
