
import unittest
from domain.complex import ComplexNumber

class test_ComplexNumber(unittest.TestCase):
    
    def test_create(self):
        c=ComplexNumber(12,4)
        
        self.assertEqual(c.get_real(),12)
        self.assertEqual(c.get_imaginary(),4)
        
    def test_seters(self):
        c=ComplexNumber()
        c.set_real(2)
        c.set_imaginary(4)
        
        self.assertEqual(c.get_real(),2)
        self.assertEqual(c.get_imaginary(),4)
        
    def test_get_modulus(self):
        c=ComplexNumber(5,5)
        
        self.assertEqual(c.get_modulus(),7.07)
        
    def test_get_argument(self):
        c=ComplexNumber(3,4)
        self.assertEqual(c.get_argument(),53.13)
        
    def test_get_conjugate(self):
        c=ComplexNumber(3,4)
        a=c.get_conjugate()
        
        self.assertEqual(a.get_real(),3)
        self.assertEqual(a.get_imaginary(),-4)
        
    def test_mult_by_real(self):
        c=ComplexNumber(3,4)
        c=c.mult_by_real(3)
        
        self.assertEqual(c.get_real(),9)
        self.assertEqual(c.get_imaginary(),12)
        
    def test_mult_by_imaginary(self):
        c=ComplexNumber(3,4)
        c=c.mult_by_imaginary(3)
        
        self.assertEqual(c.get_real(),-12)
        self.assertEqual(c.get_imaginary(),9)
        
    def test_add_complx(self):
        c1=ComplexNumber(3,4)
        c2=ComplexNumber(3,-2)
        c=ComplexNumber.add_complx(c1,c2)
        
        self.assertEqual(c.get_real(),6)
        self.assertEqual(c.get_imaginary(),2)
        
    def test_mult_complx(self):
        c1=ComplexNumber(3,4)
        c2=ComplexNumber(3,-2)
        c=ComplexNumber.mult_complx(c1, c2)
        
        self.assertEqual(c.get_real(),17)
        self.assertEqual(c.get_imaginary(),6)
        
        
    def test_get_polar(self):
        c=ComplexNumber(3,4)
        c=c.get_polar()
        
        self.assertEqual(c,"5.0(cos(53.13o)+isin(53.13o))")
        
    def test_matrix_comlx(self):
        c=ComplexNumber(3,4)
        
        r=c.matrix_comlx()
        
        self.assertEqual(str(r),"[[ 3 -4]\n [ 4  3]]")
        
    def test_pow_complx(self):
        c=ComplexNumber(3,4)
        
        c=c.pow_complx(3)
        
        self.assertEqual(c.get_real(),-117)
        self.assertEqual(c.get_imaginary(),44) 
        
        
        
        
        
        

if __name__=='__main__':
    unittest.main()
        
    
        
        
        