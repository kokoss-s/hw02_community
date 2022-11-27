# Импортируем CreateView, чтобы создать ему наследника
from django.views.generic import CreateView

# Функция reverse_lazy позволяет получить URL по параметрам функции path()
# Берём, тоже пригодится
from django.urls import reverse_lazy

# Импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm


class SignUp(CreateView):
    # Из какого класса взять форму
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('posts:index')
    # Имя шаблона, куда будет передана переменная form с объектом
    # HTML-формы. Всё это чем-то похоже на вызов функции render() во
    # view-функции.
    template_name = 'users/signup.html'
