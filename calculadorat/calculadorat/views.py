from django.shortcuts import render

def calculadora(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operacion = request.POST['operacion']
        
        if operacion == 'sumar':
            resultado = num1 + num2
            return render(request, 'calc.html', {'resultado': resultado})
        elif operacion == 'restar':
            resultado = num1 - num2
            return render(request, 'calc.html', {'resultado': resultado})
        elif operacion == 'multiplicar':
            resultado = num1 * num2
            return render(request, 'calc.html', {'resultado': resultado})
        elif operacion == 'dividir':
            if num2 != 0:
                resultado = num1 / num2
                return render(request, 'calc.html', {'resultado': resultado})
            else:
                error_msg = "Error: No se puede dividir entre cero."
                return render(request, 'calc.html', {'error_msg': error_msg})

    return render(request, 'calc.html')

#....................................#

def lista_usuarios(request):
    usuarios = [
    {'nombre': 'Carlos Eduardo Mata', 'edad': 33},
    {'nombre': 'Sofía Ama Paz', 'edad': 27},
    {'nombre': 'Alejandro Jose de Pez', 'edad': 19},
    {'nombre': 'María Fernanda López', 'edad': 29},
    {'nombre': 'Juan Carlos Ramírez', 'edad': 23},
    {'nombre': 'Ana Sofía Rodríguez', 'edad': 32},
    {'nombre': 'Pedro Alejandro Gómez', 'edad': 21},
    {'nombre': 'Amelia Gabriela Pérez', 'edad': 27},
    {'nombre': 'Andres Miguel Sánchez', 'edad': 25},
    {'nombre': 'Carolina Elizabeth Torres', 'edad': 30},
    {'nombre': 'Ricardo Antonio Mendoza', 'edad': 28},
    {'nombre': 'Isabel Cristina Morales', 'edad': 29},
    {'nombre': 'Alejandra Cristina Morales', 'edad': 39},
]
    for usuario in usuarios:
        if usuario['nombre'].startswith('A'):
            usuario['negrita'] = True
        else:
            usuario['negrita'] = False
    return render(request, 'lista-usuarios.html', {'usuarios': usuarios})
