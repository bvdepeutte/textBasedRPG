import unittest
from unittest.mock import patch
import io
import sys
from userCreation import characterCreation, Human, Cyborg


class TestCharacterCreation(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['human'])
    def test_selectLiveFormHuman(self, mock_input, mock_stdout):
        selector = characterCreation()
        character = selector.selectLiveForm()
        self.assertIsInstance(character, Human)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['cyb',"cyborg"])
    def test_selectLiveFormErrorCyborg(self, mock_input, mock_stdout):
        selector = characterCreation()
        character = selector.selectLiveForm()
        self.assertIsInstance(character, Cyborg)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['cyb',"cyborg","trader"])
    def test_selectClass(self, mock_input, mock_stdout):
        selector = characterCreation()
        selector.selectLiveForm()
        selector.selectClass()
        isTrader = selector.classSelection.lower()
        testList = ["greed","iem","energy"]
        traits = selector.character.traits.getEnabledTraits()
        self.assertEqual(isTrader, "trader")
        self.assertListEqual(sorted(testList),sorted(traits))

if __name__ == "__main__":
    unittest.main()