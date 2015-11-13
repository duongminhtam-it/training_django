from django import forms


class BookForm(forms.Form):
    name = forms.CharField()
    title = forms.CharField()
    content = forms.CharField()

    def dosomething(self):
        pass
