

class ComplexNumber_Repo():
    
    
    def __init__(self):
        
        """
            input: -.
            output: A repository.
            desc.: Constructor. 
        """
        
        self.__repo=[]
        
    def addc(self,c):
        
        """
            input: A complex number.
            output: A modified repository.
            desc.: A complex number is added in the repository. 
        """
        self.__repo.append(c)
        
    def get_all(self):
        
        """
            input: A repository.
            output: All the values of the repository.
            desc.: The method returns all the values of the repository. 
        """
        
        return self.__repo
    
    def get_all_conjugates(self):
        
        """
            input: A repository.
            output: A modified repository.
            desc.: The method returns all the conjugates of complex numbers. 
        """
        
        l=[]
        for el in self.__repo:
            l.append(el.get_conjugate())
            
        return l
    
    def mult_all_real(self,x):
        
        """
            input: A repository.
            output: A modified repository.
            desc.: The method returns all the values of the repository multiplied by a real number. 
        """
        
        l=[]
        for el in self.__repo:
            l.append(el.mult_by_real(x))
            
        return l
    
    def mult_all_imaginary(self,x):
        
        """
            input: A repository.
            output: A modified repository.
            desc.: The method returns all the values of the repository multiplied by an imaginary number. 
        """
        
        l=[]
        
        for el in self.__repo:
            l.append(el.mult_by_imaginary(x))
            
        return l
    
    def add_all_complex_numbers(self,c):
        
        """
            input: A repository.
            output: A modified repository.
            desc.: The method returns all the values of the repository added with another complex number. 
        """
        
        l=[]
        
        for el in self.__repo:
            l.append(el.add_complx(c))
            
        return l
    
    def multiply_all_complex_numbers(self,c):
        
        """
            input: A repository.
            output: A modified repository.
            desc.: The method returns all the values of the repository multiplied by another complex number. 
        """
        
        l=[]
        
        for el in self.__repo:
            l.append(el.mult_complx(c))
            
        return l
    
    def get_all_complex_numbers_pol_form(self):
        
        """
            input: A repository.
            output: A modified repository.
            desc.: The method returns all the polar forms of the values from the repository. 
        """
        
        l=[]
        
        for el in self.__repo:
            l.append(el.get_polar())
            
        return l
    def get_all_complex_numbers_matrices(self):
        
        """
            input: A repository.
            output: A modified repository.
            desc.: The method returns all the matrices of the values from the repository. 
        """
        
        l=[]
        
        for el in self.__repo:
            l.append(el.matrix_comlx())
            
        return l
    
    def get_all_complex_numbers_powers(self,p):
        
        """
            input: A repository.
            output: A modified repository.
            desc.: The method returns all the values from the repository raised to a power. 
        """
        
        l=[]
        
        for el in self.__repo:
            l.append(el.pow_complx(p))
            
        return l
    
    def get_all_complex_numbers_sqrt(self):
        
        """
            input: A repository.
            output: A modified repository.
            desc.: The method returns all the square roots of the values from the repository. 
        """
        
        l=[]
        
        for el in self.__repo:
            l.append(el.sqrt_complx())
            
        return l
    
    def get_all_complex_numbers_exp(self):
        
        """
            input: A repository.
            output: A modified repository.
            desc.: The method returns all the exponential forms of the values from the repository. 
        """
        
        l=[]
        
        for el in self.__repo:
            l.append(el.exp_complx())
            
        return l    
    
    def __str__(self):
        s=""
        
        for el in self.__repo:
            s+=str(el)+"\n"
            
        return s
    
        
        
         
        