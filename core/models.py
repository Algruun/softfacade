from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __unicode__(self):
        return '%s' % self.name


class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(to=Author, related_name='book_author')
    page_count = models.PositiveIntegerField()

    class Meta:
        unique_together = ('title', 'author')

    def __unicode__(self):
        return '%s - %s' % (self.author, self.title)
