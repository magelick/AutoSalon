from django import forms


class ContactForm(forms.Form):
    """
    Форма для контактов с автосалоном на сайте
    """
    # Адрес элетронной почты пользователя
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Адрес электронной почты'})
    )
    # Тема вопроса
    topic_of_the_question = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Тема вопроса'})
    )
    # Вопрос пользователя
    question = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Ваш вопрос'})
    )

