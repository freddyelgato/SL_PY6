from fasthtml.common import *

app,rt = fast_app()

@rt('/change')
def get(): return P('Nice to be here!')

@rt('/')
def get(): return Div(
    
    H1('HELLO WORLD'), 
    P('MY NAME IS FREDDY'),
    hx_get="/change")

serve()