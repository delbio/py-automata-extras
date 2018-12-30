from defusedxml.ElementTree import parse

from automaton.builder.xml import allow_local_module_if_requested
from automaton.scheduler.execution.error.XmlBuilder import ErrorHandlerXmlBuilder
from automaton.scheduler.execution.nextaction.XmlBuilder import NextActionSelectorXmlBuilder
from automaton.scheduler.context.XmlBuilder import XmlContextBuilder
from automaton.builder.XmlBuilder import AutomatonXmlBuilder


def build_from_xml(interactive, filepath):
    root = parse(filepath).getroot()
    allow_local_module_if_requested(filepath, root)
    builder = AutomatonXmlBuilder()
    automaton = builder.newObjectFromXmlElement(root)
    automaton.setCurrentState(automaton.getBegin())
    error_handler_builder = ErrorHandlerXmlBuilder()
    error_handler = error_handler_builder.newObjectFromXmlElement(root)
    next_action_selector_builder = NextActionSelectorXmlBuilder()
    next_action_selector = next_action_selector_builder.newObjectFromXmlElement(root)
    context_builder = XmlContextBuilder()
    context = context_builder.newObjectFromXmlElement(root)
    return {
        'automaton': automaton,
        'error_handler': error_handler,
        'next_action_selector': next_action_selector,
        'context': context,
        'interactive': interactive
    }