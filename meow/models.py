from django.db import models

class Message(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.author + " says " + self.content
    

