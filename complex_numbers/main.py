from ui.console import ComplexNumber_UI
from application.complex_controller import ComplexNumber_Controller
from infrastructure.complex_repo import ComplexNumber_Repo

r=ComplexNumber_Repo()
c=ComplexNumber_Controller(r)
ui=ComplexNumber_UI(c)

ui.start()