from django.shortcuts import render
from django import forms

class FormularioConta(forms.Form):
    sequencia = forms.CharField()

def index(request):
    formulario = FormularioConta(request.POST r none)

    if request.method == 'POST' and formulario.is_valid():
        sequencia = input(formulario.clean()['sequencia'])
        resultado = len(sequencia)

        caract1 = A
        caract2 = T
        caract3 = C
        caract4 = G

        cont1 = sum([1 for i in sequencia if i == caract1])
        cont2 = sum([1 for i in sequencia if i == caract2])
        cont3 = sum([1 for i in sequencia if i == caract3])
        cont4 = sum([1 for i in sequencia if i == caract4])

        contagem = (f"na sequencia existem {cont1} Adeninas,
                                           {cont2} Timinas,
                                            {cont3} Citosinas e
                                            {cont4} Guaninas!")
            
        return reder(request, 'resultado.html', {
            'resultadocontagem' : resultadocontagem
        })

    return render(request, 'inderx.html', {
        'frm' : formulario
    })