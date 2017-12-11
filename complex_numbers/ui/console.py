
#from application.complex_controller import ComplexNumber_Controller
#from infrastructure.complex_repo import ComplexNumber_Repo
import os
#from domain.complex import ComplexNumber


class ComplexNumber_UI():
    
    
    def __init__(self, cntr):
        self.__controller=cntr   
    
    @staticmethod
    def read_number():
        
        while True:
            try:
                n=0
                while not n:
                    n=int(input())
                    if not n:
                        print("n!=0")
                break
            except:
                print("Wrong Value!Try again!")
                
        return n
    @staticmethod
    def read_r_i():
        
        print("Enter a real value:")
        a=ComplexNumber_UI.read_number()
        
        print("Enter an imaginary value:")
        b=ComplexNumber_UI.read_number()
        
        return a,b
        
    @staticmethod   
    def menu():
        os.system("cls")
        
        print("1.Determine the cartesian form (real part and imaginary part) of a complex number.")
        print("2.Determine the complex conjugate of a complex number.")
        print("3.Multiply a complex number by a real number.")
        print("4.Multiply a complex number by an imaginary number.")
        print("5.Add two complex numbers.")
        print("6.Multiply two complex numbers.")
        print("7.Determine the polar form (modulus and argument) of a complex number")
        print("8.Determine the matrix represantaion of a complex number.")
        print("9.Powers of a complex number.")
        print("10.Square root of a complex number.")
        print("11.Exponential form of a complex number.")
        print("12.Add a complex number in the repository.")
        print("13.Print the list of complex numbers.")
        print("0.Exit")
        
    
    @staticmethod
    def parse(line):
        
        
        
        try:
            it=0
            a,b='',''
    
            if line[it]=='-':
                a+='-'
                it+=1
                
            while it<len(line) and not(line[it].isdigit()):
                it+=1
                
            while line[it]!='-' and line[it]!='+':
                a+=line[it]
                it+=1

            while it<len(line) and not(line[it].isdigit()):
                it+=1
            
            while it<len(line) and line[it].isdigit():
                b+=line[it]
                it+=1

            return int(a),int(b)
        
        except:
            input("The input data is not in the right form!")
        
    
    def read_from_file(self):
        
        try:
            file=open("input_data","r")
            for lines in file:
                s=lines
                a,b=ComplexNumber_UI.parse(s)
                self.__controller.add_cnr(a,b)
                
        except:
            input("Something is wrong with the file 'input_data' !")    
    def app_keyboard(self):
        
        
        
        print("Enter the number of complex numbers you want to be read:")
        n=ComplexNumber_UI.read_number()
        
        while n:
            
            a,b=ComplexNumber_UI.read_r_i()
            
            self.__controller.add_cnr(a,b)
            
            n-=1    
        
        
        while True:
            
            ComplexNumber_UI.menu()
            print("-------------------------KEYBOARD-------------------------")
            
            opt=input("Select an option:")
            
            if opt=="0":
                break
            
            elif opt=="1":
                a,b=ComplexNumber_UI.read_r_i()
                self.__controller.add_cnr(a,b)
                
                repo=self.__controller.get_all_cnr()
                
                for el in repo:
                    print(str(el))
                input("Press any key...")
                
                
            elif opt=="2":
                a,b=ComplexNumber_UI.read_r_i()
                self.__controller.add_cnr(a,b)
                
                repo=self.__controller.get_all_conj()
                
                for el in repo:
                    print(str(el))
                input("Press any key...")
                
            elif opt=='3':
                a,b=ComplexNumber_UI.read_r_i()
                self.__controller.add_cnr(a,b)
                
               
                print("Enter a number:")
                x=ComplexNumber_UI.read_number()
                repo=self.__controller.mult_r(x)
                
                for el in repo:
                    print(str(el))
                input("Press any key...")
                
                
            elif opt=='4':
                a,b=ComplexNumber_UI.read_r_i()
                self.__controller.add_cnr(a,b)
                
                
                print("Enter a number:")
                x=ComplexNumber_UI.read_number()
                repo=self.__controller.mult_i(x)
                
                for el in repo:
                    print(str(el))
                input("Press any key...")
                
            elif opt=='5':
                a,b=ComplexNumber_UI.read_r_i()

                
                repo=self.__controller.add_all_cnr(a,b)
                
                for el in repo:
                    print(str(el))
                    
                self.__controller.add_cnr(a,b)
                input("Press any key...")
                
            elif opt=='6':
                a,b=ComplexNumber_UI.read_r_i()
                
                repo=self.__controller.mult_all_cnr(a,b)
                
                for el in repo:
                    print(str(el))
                    
                self.__controller.add_cnr(a,b)
                input("Press any key...")
        
            elif opt=='7':
                a,b=ComplexNumber_UI.read_r_i()
                self.__controller.add_cnr(a,b)
                
                repo=self.__controller.get_all_cnr_pf()
                
                for el in repo:
                    print(str(el))
                input("Press any key...")
            
                    
            elif opt=='8':
                a,b=ComplexNumber_UI.read_r_i()
                self.__controller.add_cnr(a,b)
                repo=self.__controller.get_all_cnr_mx()
                
                for el in repo:
                    print(str(el),'\n')
                input("Press any key...")
                    
            elif opt=='9':
                a,b=ComplexNumber_UI.read_r_i()
                self.__controller.add_cnr(a,b)
                print("Enter a power:")
                p=ComplexNumber_UI.read_number()
                
                repo=self.__controller.get_all_cnr_pow(p)
                
                for el in repo:
                    print(str(el))
                    
                input("Press any key...")
                
            elif opt=='10':
                a,b=ComplexNumber_UI.read_r_i()
                self.__controller.add_cnr(a,b)
                
                repo=self.__controller.get_all_cnr_sqrt()
                
                for el in repo:
                    print(str(el))
                    
                input("Press any key...")
                
                
            elif opt=='11':
                a,b=ComplexNumber_UI.read_r_i()
                self.__controller.add_cnr(a,b)
                
                repo=self.__controller.get_all_exp()
                
                for el in repo:
                    print(str(el))
                    
                input("Press any key...")
                
            elif opt=='12':
                a,b==ComplexNumber_UI.read_r_i()
                self.__controller.add_cnr(a,b)
                
                
            elif opt=='13':
                repo=self.__controller.get_all_cnr()
                
                for el in repo:
                    print(str(el))
                    
                input("Press any key...")
                
                
            else:
                input("The option doesn't exist! Try again! Press any key...")
                
    def app_file(self):
        
        
        
        self.read_from_file()
        
        try:
            file=open("output_data","w")
        except:
            input("Something is wrong with the file 'output_data'! ")     
        
        
        while True:
           
            ComplexNumber_UI.menu()
            print("-------------------------FILE-------------------------")
            
            opt=input("Select an option:")
            
            if opt=="0":
                break
            
            elif opt=="1":
                repo=self.__controller.get_all_cnr()
                
                file.write("The cartesian form is=>")
                for el in repo:
                    file.write(str(el))
                    file.write(" ** ")
                    
                file.write('\n\n')
                input("Press any key...")
                
                
            elif opt=="2":
                repo=self.__controller.get_all_conj()
                
                file.write("The conjugate is=>")
                for el in repo:
                    file.write(str(el))
                    file.write(" ** ")
                    
                file.write('\n\n')
                input("Press any key...")
                
            elif opt=='3':
        
                print("Enter a number:")
                x=ComplexNumber_UI.read_number()
                repo=self.__controller.mult_r(x)
                
                file.write("The complex number multiplied by "+str(x)+"is=>")
                for el in repo:
                    file.write(str(el))
                    file.write(" ** ")
                    
                file.write('\n\n')
                input("Press any key...")
                
                
            elif opt=='4':                
                
                print("Enter a number:")
                x=ComplexNumber_UI.read_number()
                repo=self.__controller.mult_i(x)
                
                file.write("The complex number multiplied by "+str(x)+"i"+" is=>")
                for el in repo:
                    file.write(str(el))
                    file.write(" ** ")
                    
                file.write('\n\n')
                input("Press any key...")
                
            elif opt=='5':
                a,b=ComplexNumber_UI.read_r_i()

                
                repo=self.__controller.add_all_cnr(a,b)
                
                file.write("The result of two complex numbers added is=>")
                for el in repo:
                    file.write(str(el))
                    file.write(" ** ")
                    
                file.write('\n\n')
                    
                self.__controller.add_cnr(a,b)
                input("Press any key...")
                
            elif opt=='6':
                a,b=ComplexNumber_UI.read_r_i()
                
                repo=self.__controller.mult_all_cnr(a,b)
                
                file.write("The result of two complex numbers multiplied is=>")
                for el in repo:
                    file.write(str(el))
                    file.write(" ** ")
                file.write('\n\n')
                    
                self.__controller.add_cnr(a,b)
                input("Press any key...")
        
            elif opt=='7':
                
                repo=self.__controller.get_all_cnr_pf()
                
                
                file.write("The polar form is=>")
                for el in repo:
                    file.write(str(el))
                    file.write(" ** ")
                file.write('\n\n')
                input("Press any key...")
            
                    
            elif opt=='8':
                
                repo=self.__controller.get_all_cnr_mx()
                
                
                file.write("The matrix is=>")
                for el in repo:
                    file.write('\n')
                    file.write(str(el))
                    file.write('\n')
                    file.write(" ** ")
                file.write('\n\n')
                input("Press any key...")
                    
            elif opt=='9':
                
                print("Enter a power:")
                p=ComplexNumber_UI.read_number()
                
                repo=self.__controller.get_all_cnr_pow(p)
                
                file.write("The complex number raised to a power "+str(p)+" is=>")
                for el in repo:
                    file.write(str(el))
                    file.write(" ** ")
                file.write('\n\n')    
                input("Press any key...")
                
            elif opt=='10':
                
                
                repo=self.__controller.get_all_cnr_sqrt()
                
                
                file.write("The square root of a complex number is=>")
                for el in repo:
                    file.write(str(el))
                    file.write(" ** ")
                file.write('\n\n')    
                input("Press any key...")
                
                
            elif opt=='11':
                
                repo=self.__controller.get_all_exp()
                
                file.write("The exponential form is=>")
                for el in repo:
                    file.write(str(el))
                    file.write(" ** ")
                file.write('\n\n')    
                input("Press any key...")
                
            elif opt=='12':
                a,b==ComplexNumber_UI.read_r_i()
                self.__controller.add_cnr(a,b)
                
                
            elif opt=='13':
                repo=self.__controller.get_all_cnr()
                
                for el in repo:
                    print(str(el))
                    
                input("Press any key...")
                
                
            else:
                input("The option doesn't exist! Try again! Press any key...")
                
    def start(self):
        
        choice=0
        
        while True and (choice!=1 or choice!=2) :
            
            try:
                choice=input("Press \n1 if you want to give input from the keyboard \n or \n2 if you want to use the data from a file\n")
                break
            except:
                input("Something went wrong! Try again!")
                
        
        if choice=='1':
            self.app_keyboard()
            
        else:
            self.app_file()
            
        
                
                
                
            
        
        
        
            