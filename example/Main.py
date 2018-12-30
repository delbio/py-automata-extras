import argparse

from automaton.scheduler.Runner import Runner
from automaton.scheduler.XmlBuilder import build_from_xml


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
    components = build_from_xml(args.interactive, args.config)
    runner = Runner()
    runner.run(**components)
