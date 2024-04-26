from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category','name', 'description', 'price', 'image',]
        widgets = {
			'category': forms.Select(attrs={
				'class': INPUT_CLASSES
			}),
            'name': forms.TextInput(attrs={
                'placeholder':'Name of the item...',  
                'class':INPUT_CLASSES
            }),  
            'description': forms.Textarea(attrs={
            	'rows':'5',  
            	'cols':'10', 
            	'placeholder':'Description of the item...',   
            	'class': INPUT_CLASSES
            }),
            'price': forms.NumberInput(attrs={
            	'type':'number', 
            	'min':'1', 
            	'step':'any', 
            	'placeholder':'Price...',    
            	'class':INPUT_CLASSES
            }),
            'image':forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
		} 
