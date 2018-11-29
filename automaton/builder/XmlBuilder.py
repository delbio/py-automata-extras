from automaton.builder.common import getClassFromElement, getclass, setPropertyOnObject


# Manage State Type actions

def setBegin(a, s, t):
    a.setBegin(s)

def addEnd(a, s, t):
    a.addEnd(s)

def nop(a, s, t):
    pass

def unknownStateType(a, s, t):
    raise ValueError("state type unknown: " + t )

class AutomatonXmlBuilder():
    def __init__(self):
        pass

    def newObjectFromXmlElement(self, element):
        automaton = getClassFromElement(element)()
        setPropertyOnObject('Property', element, automaton)

        switcher = {
            'BEGIN': setBegin,
            'END': addEnd,
            '-': nop,
        }

        stateNodes = element.findall('States/State');
        for stateElement in stateNodes:
            state = getClassFromElement(stateElement)()
            setPropertyOnObject('Property', stateElement, state)
            automaton.addState(state)
            stateType = stateElement.attrib['type']
            switcher.get(stateType, unknownStateType )(automaton, state, stateType)

        actionNodes = element.findall('Actions/Action')
        for actionElement in actionNodes:
            sourceState = automaton.getState(actionElement.attrib['source'])
            targetState = automaton.getState(actionElement.attrib['target'])

            action = getClassFromElement(actionElement)(sourceState, targetState)
            setPropertyOnObject('Property', actionElement, action)
            sourceState.addAction(action)


        automaton.setCurrentState(automaton.getBegin())
        automaton.checkIntegrity()
        return automaton
