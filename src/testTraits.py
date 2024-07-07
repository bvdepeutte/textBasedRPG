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
            "easyLearner",
            "healing",
            "mecanic",
            "iem",
            "asocial",
            "gluttony",
            "frugal",
            "poorVision",
            "dumb",
            "greed",
            "rebel"
        ]
        self.assertEqual(sorted(traits.getAvailableTraits()),
                         sorted(expectedList),
                         "getAvailableTraits doesn't the expected values")
    
    def test_traitSelection(self):
        traits = Traits()
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
        traits.traitSelection("fire")
        self.assertEqual(traits.getAvailableTraits().sort(),
                         expectedList.sort(),
                         "traitSelection doesn't set the expected values")        

    def test_getEnabledTrait(self):
        traits = Traits()
        expectedList = [
            "poorVision",
            "asocial",
            "easyLearner",
            "fire"
        ]
        traits.traitSelection("poorVision")
        traits.traitSelection("asocial")
        traits.traitSelection("easyLearner")
        traits.traitSelection("fire")
        self.assertEqual(sorted(traits.getEnabledTraits()),
                         sorted(expectedList),
                         "traitSelection doesn't set the expected values")  

    def testGetAvailablePoints(self):
        traits = Traits()
        traits.traitSelection("asocial")
        traits.traitSelection("easyLearner")
        traits.traitSelection("fire")        
        points = traits.getAvailablePoints()
        self.assertNotEqual(points,0)
        self.assertNotEqual(traits.getEnabledTraits(),[])
if __name__ == "__main__":
    unittest.main()