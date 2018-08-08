import sys
import argparse
from pprint import pprint

from defusedxml.ElementTree import parse

from automaton.builder.XmlBuilder import XmlBuilder
from automaton.runner.Runner import SimpleRunner

sys.path.append('./actions')


def build_from_xml(filepath):
    builder = XmlBuilder()
    root = parse(filepath).getroot()
    automaton = builder.newObjectFromXmlElement(root)
    print('Loaded Automaton: \n', automaton.__str__())
    return automaton

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
    pprint(vars(args))
    automaton =  build_from_xml(args.config)
    runner = SimpleRunner()
    runner.run(automaton, args.interactive)
