import unittest
from traits import Traits

class TestTraits(unittest.TestCase):
    def test_getAvailableTraits(self):
        traits = Traits()
        expectedList = [
            "poison",
            "fire",
            "acid",
            "psycho",
            "social",
            "adaptative",
            "energy",
            "easylearner",
            "healing",
            "mecanic",
            "iem",
            "asocial",
            "gluttony",
            "frugal",
            "poorVision",
            "dumb"
        ]
        self.assertEqual(traits.getAvailableTraits(),
                         expectedList,
                         "getAvailableTraits doesn't the expected values")
    
    def test_traitSelection(self):
        traits = Traits()
        wholeList = [
            "poison",
            "fire",
            "acid",
            "psycho",
            "social",
            "adaptative",
            "energy",
            "easylearner",
            "healing",
            "mecanic",
            "iem",
            "asocial",
            "gluttony",
            "frugal",
            "poorVision",
            "dumb"
        ]
        expectedList = [
            "poison",
            "acid",
            "psycho",
            "adaptative",
            "energy",
            "healing",
            "mecanic",
            "iem",
            "gluttony",
            "frugal",
            "dumb"
        ]
        traits.traitSelection("poorVision")
        traits.traitSelection("asocial")
        traits.traitSelection("easylearner")
        traits.traitSelection("social")
        traits.traitSelection("fire")
        self.assertEqual(traits.getAvailableTraits(),
                         expectedList,
                         "traitSelection doesn't set the expected values")        


if __name__ == "__main__":
    unittest.main()