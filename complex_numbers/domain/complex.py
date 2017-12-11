from builtins import str
import numpy
import math



class ComplexNumber(object):
   
   
    def __init__(self,r=1,i=1):
        
        """
            input: Two integers 'r' and 'i'.
            output: A complex number(r,i).
            desc.: Constructor. 
        """
         
        self.__real=r
        self.__imaginary=i
    
    def get_real(self):
        
        """
            input: A complex number.
            output: The real part of the complex number.
            desc.: Getter. 
        """
        return self.__real
    
    def get_imaginary(self):
        
        """
            input: A complex number.
            output: The imaginary part of the complex number.
            desc.: Getter. 
        """
        return self.__imaginary
    
    def set_real(self,r):
        
        """
            input: A complex number and an integer 'r'.
            output: The complex number with the real part changed.
            desc.: Setter. 
        """
        
        self.__real=r
        
    def set_imaginary(self,i):
        
        """
            input: A complex number and an integer 'i'.
            output: The complex number with the imaginary part changed.
            desc.: Setter. 
        """
        self.__imaginary=i
        
    def get_modulus(self):
        
        """
            input: A complex number.
            output: The modulus of a complex number.
            desc.: Getter. 
        """
        return round(math.sqrt( (self.__imaginary**2) + (self.__real**2) ),2)
        
    def get_argument(self):
        
        """
            input: A complex number.
            output: The argument of a complex number.
            desc.: Getter. 
        """
        return round(math.degrees(math.atan(self.__imaginary/self.__real)),2)
    
    def get_polar(self):
        
        """
            input: A complex number.
            output: The polar form of a complex number.
            desc.: Getter. 
        """
        
        a=self.get_argument()
        b=self.get_modulus()
        
        return str(b)+"(cos(" +str(a)+"o)"+"+isin("+str(a)+"o))"
    
    def get_conjugate(self):
        
        """
            input: A complex number.
            output: The conjugate of a complex number.
            desc.: Getter. 
        """
        
        c=ComplexNumber(self.__real,-(self.__imaginary))
        return c
    
    def mult_by_real(self,x):
        
        """
            input: A complex number and an integer 'x'.
            output: A complex number multiplied by an integer 'x'.
            desc.: The method returns a new complex number obtained by the multiplication of the current complex number with an integer 'x'. 
        """
        
        c=ComplexNumber(self.__real*x,self.__imaginary*x)
        return c
        
    def mult_by_imaginary(self,x):
        
        """
            input: A complex number and an integer 'x'.
            output: A complex number multiplied by an imaginary number 'x'.
            desc.: The method returns a new complex number obtained by the multiplication of the current complex number with an imaginary number 'x'. 
        """
            
        c=ComplexNumber(-(self.__imaginary)*x,self.__real*x)
        return c
        
    def add_complx(self,other):
        
        """
            input: Two complex numbers.
            output: A complex number obtained by adding two complex numbers.
            desc.: The method returns a new complex number obtained by the additon of two complex numbers. 
        """
        c=ComplexNumber(self.__real+other.__real,self.__imaginary+other.__imaginary)
        return c
        
    def mult_complx(self,other):
        
        """
            input: Two complex numbers.
            output: A complex number obtained by multiplying two complex numbers.
            desc.: The method returns a new complex number obtained by the multiplication of two complex numbers. 
        """
        c=ComplexNumber( ( (self.__real*other.__real)-(self.__imaginary*other.__imaginary) ), ( (self.__real*other.__imaginary) +(other.__real*self.__imaginary) ))
        return c
    
    def matrix_comlx(self):
        
        """
            input: A complex number.
            output: An array representing the matrix form of a complex number.
            desc.: The method returns an array represnting the matrix form of a complex number. 
        """
        return numpy.array( [self.__real,-(self.__imaginary),self.__imaginary,self.__real] ).reshape((2,2))
    
    def pow_complx(self,n):
        
        """
            input: A complex number anf an integer 'n'.
            output: An cew complex number(self**n).
            desc.: The method returns a new complex number obtained by the powers of a complex number. 
        """
        
        c1=ComplexNumber(self.__real,self.__imaginary)
        c2=ComplexNumber(self.__real,self.__imaginary)
        
        while n-1:
            c1=c1.mult_complx(c2)
            n-=1
            
        return c1
        
    
    def sqrt_complx(self):
        
        """
            input: A complex number.
            output: The square root of a complex number.
            desc.: The method returns the square root of a complex number. 
        """
        
        a=self.get_argument()
        b=self.get_modulus()
        
        return str(round(math.sqrt(b),2))+"(cos(" +str(round(a/2,2))+"o)"+"+isin("+str(round(a/2,2))+"o))"
    
    def exp_complx(self):
        
        """
            input: A complex number.
            output: The exponential form of a complex number.
            desc.: The method returns the exponential form of a complex number. 
        """
        
        a = round(math.exp(self.__real)*math.cos(self.__imaginary),2)
        b = round(math.exp(self.__real)*math.sin(self.__imaginary),2)
        
    
        return str(a)  + str(b) + "i"
        
        
        
    
    def __str__(self):
        
        if(self.__real == 0):
            if(self.__imaginary < 0):
                s = ' - ' + str(-(self.__imaginary)) + 'i'
            else:
                s = str(self.__imaginary) + 'i'
        else:
            if(self.__imaginary > 0):
                s = str(self.__real) + ' + ' + str(self.__imaginary) + 'i'
            else:
                s = str(self.__real) + ' - ' + str(-(self.__imaginary)) + 'i'
        return s
                
        
        
    
            
        