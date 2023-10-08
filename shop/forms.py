from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Адрес электронной почты'})
    )
    topic_of_the_question = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Тема вопроса'})
    )
    question = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Ваш вопрос'})
    )

