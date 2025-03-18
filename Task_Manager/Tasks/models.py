from django.db import models
from django.utils.timezone import now

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    status = models.CharField(max_length=50, default='Upcoming')

    def save(self, *args, **kwargs):
        print(f"Saving task: {self.title}")  
        if self.due_date < now().date():
            self.status = 'Overdue'
        elif self.due_date == now().date():
            self.status = 'Due Today'
        else:
            self.status = 'Upcoming'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title