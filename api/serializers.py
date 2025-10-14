from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), write_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'author', 'author_name']


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['id', 'name', 'biography', 'books']

    def get_books(self, obj):
        books = Book.objects.filter(author=obj)
        if not books:
            return ""
        return ", ".join([f"{book.title} — {book.price} uah" for book in books])