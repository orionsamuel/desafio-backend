from django.forms import ModelForm
from app.models import Alunos

# Creat the form class.
class AlunosForm(ModelForm):
    class Meta:
        model = Alunos
        fields = ['pasta', 'ano', 'nome', 'filiacao']