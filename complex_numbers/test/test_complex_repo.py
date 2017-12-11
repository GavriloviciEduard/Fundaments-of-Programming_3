import unittest
from infrastructure.complex_repo import ComplexNumber_Repo
from domain.complex import ComplexNumber


class test_ComplexNumber_Repo(unittest.TestCase):

    
    
    def test_addc(self):
        c=ComplexNumber(2,3)
        repo=ComplexNumber_Repo()
        repo.addc(c)
        self.assertEqual(str(repo),"2+3i\n")
        
    def test_get_all(self):
        c1=ComplexNumber(2,3)
        c2=ComplexNumber(3,4)
        c3=ComplexNumber(5,6)
        
        repo=ComplexNumber_Repo()
        repo.addc(c1)
        repo.addc(c2)
        repo.addc(c3)
        
        l=repo.get_all()
        self.assertEqual(str(l[0]),"2+3i")
        self.assertEqual(str(l[1]),"3+4i")
        self.assertEqual(str(l[2]),"5+6i")
        
        
if __name__=="__main__":
    unittest.main()
        
        
        