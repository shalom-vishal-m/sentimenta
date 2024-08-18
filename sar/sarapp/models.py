from django.db import models
class TextEntry(models.Model):
  text=models.TextField()
  sentiment_score=models.FloatField(null=True,blank=True)
  
  def __str__(self):
    return self.text[:50]