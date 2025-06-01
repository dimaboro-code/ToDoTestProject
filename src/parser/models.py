from django.db import models


class TechParkCompany(models.Model):
    certificate_number = models.CharField("№ СВИД.", max_length=50)
    issue_date = models.CharField("Дата выдачи", max_length=50)
    valid_until = models.CharField("Срок действия", max_length=50)
    bin = models.CharField("БИН", max_length=20)
    status = models.CharField("Статус", max_length=50)
    name = models.CharField("Наименование компании", max_length=255)

    def __str__(self):
        return f"{self.name} ({self.certificate_number})"
