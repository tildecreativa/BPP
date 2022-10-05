import unittest
import leccion2_programa_bpp

class PruebasUnitarias(unittest.TestCase):
    def test_resta(self):
        self.assertEqual(leccion2_programa_bpp.resta(5),1)
    def test_suma(self):
        self.assertEqual(leccion2_programa_bpp.suma(5),11)
    def test_menorque100(self):
        self.assertEqual(leccion2_programa_bpp.menorque100(5),True)
    def test_numeroprimo(self):
        self.assertEqual(leccion2_programa_bpp.numeroprimo(5),True)
    def test_parimpar(self):
        self.assertEqual(leccion2_programa_bpp.parimpar(5),'impar')
    

if __name__=='__main__':
    unittest.main()