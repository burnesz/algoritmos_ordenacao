from django import forms

tipo_choice = (
    ("","Escolha uma das opções"),
    (0, "Valores aleatórios"),
    (1, "Valores quase ordenados"),
    (2, "Valores Ordenados Descrescentemente")
    )

algoritmo_choice = (
    ("","Escolha uma das opções"),
    (0, "Quick Sort"),
    (1, "Heap Sort"),
    (2, "Merge")
    )


class FormArray (forms.Form):
    tipo = forms.ChoiceField(choices=tipo_choice)
    tamanho = forms.IntegerField()
    algoritmo = forms.ChoiceField(choices=algoritmo_choice)