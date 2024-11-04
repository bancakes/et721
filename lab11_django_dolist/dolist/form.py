from django import forms

class TodoListForm(forms.form):
    text = forms.Charfield(max_length=45, widget = forms.TextInput(attrs={'class':'todo_text'}))