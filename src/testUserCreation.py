import unittest
from unittest.mock import patch
from userCreation import characterCreation, Human, Cyborg

class TestCharacterCreation(unittest.TestCase):
    @patch('builtins.input', side_effect=['human'])
    def test_selectLiveFormHuman(self, mock_input):
        selector = characterCreation()
        character = selector.selectLiveForm()
        self.assertIsInstance(character, Human)

    @patch('builtins.input', side_effect=['cyb',"cyborg"])
    def test_selectLiveFormErrorCyborg(self, mock_input):
        selector = characterCreation()
        character = selector.selectLiveForm()
        self.assertIsInstance(character, Cyborg)
if __name__ == "__main__":
    unittest.main()