from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    city = models.CharField(max_length=200)
    address = models.TextField(max_length=300)

    def to_json(self):
        return{
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=200)
    salary = models.FloatField()
    comp_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    def to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'salary': self.salary
        }