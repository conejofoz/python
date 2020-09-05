from django.db import models

# Create your models here.
class Livro(models.Model):
    autor = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    numeroPaginas = models.IntegerField()
    titulo = models.CharField(max_length=50)
    anoPublicacao = models.IntegerField()
    emailEditora = models.EmailField()

def __str__(self):
    return self.titulo