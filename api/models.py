from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255, help_text='Name of the project.')

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name


class BoardColumn(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='board_column')
    name = models.CharField(max_length=255, help_text="Name of the board's column.")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '%s - %s' % (self.project.name, self.name)


class Task(models.Model):
    board_column = models.ForeignKey(BoardColumn, on_delete=models.CASCADE, related_name='task')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, help_text='Name of the task.')
    description = models.TextField(help_text='Task description.', null=True, blank=True)
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return '%s - %s - %s' % (self.project.name, self.board_column.name, self.name)


class TaskFile(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.FileField(help_text='Task attachment.', null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        if task_file:
            return '%s - %s' % (self.task.name, self.task_file)
        else:
            return '%s - %s' % (self.task.name, 'No attachment')