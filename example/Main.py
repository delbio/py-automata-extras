import argparse

from defusedxml.ElementTree import parse

from automaton.scheduler.execution.error.ErrorHandlerXmlBuilder import ErrorHandlerXmlBuilder
from automaton.scheduler.execution.nextaction.NextActionSelectorXmlBuilder import NextActionSelectorXmlBuilder
from automaton.scheduler.context.XmlContextBuilder import XmlContextBuilder
from automaton.scheduler.Runner import Runner
from automaton.builder.common import allow_local_module_if_requested
from automaton.builder.XmlBuilder import AutomatonXmlBuilder

def build_from_xml(filepath):
    root = parse(filepath).getroot()
    allow_local_module_if_requested(filepath, root)
    builder = AutomatonXmlBuilder()
    automaton = builder.newObjectFromXmlElement(root)
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
    }


def getArgs():
    parser = argparse.ArgumentParser(description='CLI Automaton Runner')
    parser.add_argument('config', help='config file path')
    parser.add_argument('-i', dest='interactive',
                        action='store_const', const=True, default=False,
                        help='run automaton into interactive mode'
                        )
    return parser.parse_args()


if __name__ == "__main__":
    args = getArgs()
    components = build_from_xml(args.config)
    components['interactive'] = args.interactive
    runner = Runner()
    runner.run(**components)
