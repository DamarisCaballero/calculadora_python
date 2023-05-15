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
