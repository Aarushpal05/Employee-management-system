from django.db import models

class Employee(models.Model):

    employee_id = models.CharField(max_length=10, unique=True, editable=False, default='')

    name = models.CharField(max_length=100)

    email = models.EmailField()

    department = models.CharField(max_length=100)

    salary = models.IntegerField()

    def __str__(self):

        return self.name

    def save(self, *args, **kwargs):
        # Generate custom employee ID if it's a new employee
        if not self.employee_id:
            # Get the count of existing employees and add 1
            count = Employee.objects.count() + 1
            self.employee_id = f"EMP{count:03d}"
        
        super().save(*args, **kwargs)


