#from infrastructure.complex_repo import ComplexNumber_Repo
from domain.complex import ComplexNumber

class ComplexNumber_Controller():
    
    def __init__(self,repo):
        
        """
            input: A repository.
            output: A controller.
            desc.: Constructor. 
        """
        
        self.__repo=repo
        
    
    def add_cnr(self,r,i):
        
        """
            input: Two integers 'r' and 'i'.
            output: A modified controller.
            desc.: The controller adds a complex number in the repository. 
        """
        c=ComplexNumber(r,i)
        self.__repo.addc(c)
        
    def add_obj_cnr(self,c):
        
        """
            input: A complex numbber(object).
            output: A modified controller.
            desc.: The controller adds a complex number(object) in the repository. 
        """
        
        self.__repo.addc(c)
        
    def get_all_cnr(self):
        
        """
            input: A controller.
            output: A repository.
            desc.: The controller returns all the values of the repository. 
        """
        
        return self.__repo.get_all()
    
    def get_all_conj(self):
        
        """
            input: A controller.
            output: A repository.
            desc.: The controller returns all the conjugates from the repository. 
        """
        
        return self.__repo.get_all_conjugates()
    
    def mult_r(self,x):
        
        """
            input: A controller.
            output: A repository.
            desc.: The controller returns all the values multiplied by a real number from the repository. 
        """
        
        return  self.__repo.mult_all_real(x)
    
    def mult_i(self,x):
        
        """
            input: A controller.
            output: A repository.
            desc.: The controller returns all the values multiplied by an imaginary number from the repository. 
        """
        
        return self.__repo.mult_all_imaginary(x)
    
    def add_all_cnr(self,a,b):
        
        """
            input: A controller.
            output: A repository.
            desc.: The controller returns all the values added with another complex number from the repository. 
        """
        
        c=ComplexNumber(a,b)
        
        return self.__repo.add_all_complex_numbers(c)
    
    def mult_all_cnr(self,a,b):
        
        """
            input: A controller.
            output: A repository.
            desc.: The controller returns all the values multiplied with another complex number from the repository. 
        """
        
        c=ComplexNumber(a,b)
        
        return self.__repo.multiply_all_complex_numbers(c)
    
    def get_all_cnr_pf(self):
        
        """
            input: A controller.
            output: A repository.
            desc.: The controller returns all the polar forms from the repository. 
        """
        
        return self.__repo.get_all_complex_numbers_pol_form()
    
    def get_all_cnr_mx(self):
        
        """
            input: A controller.
            output: A repository.
            desc.: The controller returns all the matrices from the repository. 
        """
        return self.__repo.get_all_complex_numbers_matrices()
    
    def get_all_cnr_pow(self,p):
        
        """
            input: A controller.
            output: A repository.
            desc.: The controller returns all the values raised to a power from the repository. 
        """
        
        return self.__repo.get_all_complex_numbers_powers(p)
    
    def get_all_cnr_sqrt(self):
        
        """
            input: A controller.
            output: A repository.
            desc.: The controller returns all the square roots from the repository. 
        """
        
        return self.__repo.get_all_complex_numbers_sqrt()
    
    def get_all_exp(self):
        
        """
            input: A controller.
            output: A repository.
            desc.: The controller returns all the exponential forms from the repository. 
        """
        
        return self.__repo.get_all_complex_numbers_exp()
        
    
    def __str__(self):
        
        s=""
        
        for el in self.__repo:
            s+=str(el)+"\n"
    
        