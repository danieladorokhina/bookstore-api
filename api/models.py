from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.title
    
