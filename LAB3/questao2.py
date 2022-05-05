def wrap_function(func):

    def wrapper(*args, **kwargs):

        print('Para o aluno:')
        func(*args, **kwargs)
        
    return wrapper
    
@wrap_function
def media_aluno(a, b, c, d, dados):

    for key in dados:

        print(key, ':', dados[key])
    
    media = (a + b + c + d) / 4

    print('A media e:', media)

d = {'nome' : 'Gilberto', 'sobrenome': 'Ferreira', 'Materia' : 'Matematica' , 'Bimestre' : '1'}
print(wrap_function(media_aluno(7, 4, 8, 3, d)))