from django import forms

class PlayerNames:
    pitcher = forms.CharField(max_length=20, label='Enter the first and last name of a pitcher')
    hitter = forms.CharField(max_length=20, label='Enter the first and last name of a hitter')