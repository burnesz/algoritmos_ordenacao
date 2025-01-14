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
    tipo = forms.TypedChoiceField(
        choices=tipo_choice,
        coerce=int,
        widget=forms.Select(attrs={"class": "form-select"})
        )
    tamanho = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    algoritmo = forms.TypedChoiceField(
        choices=algoritmo_choice,
        coerce=int,
        widget=forms.Select(attrs={"class": "form-select"})
        )