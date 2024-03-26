from django.db import models

class Project(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="The name of the Project.")
    description = models.CharField(  # Fix typo: Charield to CharField
        max_length=350,
        help_text="The Project's description.")

    def __str__(self):
        return self.name

class Task(models.Model):
    """A projected task."""
    name = models.CharField(
        max_length=50,
        help_text="The name of the Task.")
    description = models.CharField(  # Fix typo: Charield to CharField
        max_length=350,
        help_text="The Task's description.")
    due_date = models.DateField(
        verbose_name="Date the task was projected.")  # Fix typo: "project." to "projected."
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE)
    def __str__(self):
        return self.name
