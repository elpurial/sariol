from django import forms


class Form_contacto(forms.Form):
    nombre = forms.CharField(label="Your name", max_length=500, required=True)    
    asunto = forms.CharField(label="Asunto",widget=forms.Textarea)
    sender = forms.EmailField(label="Your email",required=True)
    cc_myself = forms.BooleanField(required=False)