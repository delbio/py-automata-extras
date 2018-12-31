import unittest
import os

from automaton.scheduler.Runner import Runner
from automaton.scheduler.XmlBuilder import build_from_xml


class TestContextActionArgs(unittest.TestCase):

    def test_run_automata_without_error(self):
        # Arrange
        xml_filename = 'automaton.xml'
        xml_file_dir = os.path.dirname(__file__)
        xml_filepath = os.path.join(xml_file_dir, xml_filename)
        components = build_from_xml(False, xml_filepath)
        runner = Runner()
        # Act
        runner.run(**components)
        # Assert
        # noop


if __name__ == '__main__':
    unittest.main()