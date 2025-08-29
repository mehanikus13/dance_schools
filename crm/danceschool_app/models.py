from django.db import models

class Parent(models.Model):
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    phone_number = models.CharField("Номер телефона", max_length=20, blank=True)
    email = models.EmailField("Email", blank=True)
    telegram = models.CharField("Telegram", max_length=100, blank=True)
    viber = models.CharField("Viber", max_length=100, blank=True)
    whatsapp = models.CharField("WhatsApp", max_length=100, blank=True)
    city = models.CharField("Город", max_length=100, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Родитель"
        verbose_name_plural = "Родители"

class Student(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая заявка'),
        ('call', 'Созвон'),
        ('thinking', 'Думает'),
        ('trial', 'Записан на пробное'),
        ('callback', 'Перезвонить'),
        ('active', 'Активен'),
        ('vacation', 'В отпуске'),
        ('archive', 'Архив'),
    ]

    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    date_of_birth = models.DateField("Дата рождения", null=True, blank=True)
    city = models.CharField("Город", max_length=100, blank=True)
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Родитель")
    phone_number = models.CharField("Номер телефона", max_length=20, blank=True)
    email = models.EmailField("Email", blank=True)
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"


class Branch(models.Model):
    name = models.CharField("Название филиала", max_length=200)
    address = models.CharField("Адрес", max_length=300)
    phone_number = models.CharField("Контактный телефон", max_length=20, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"


class Hall(models.Model):
    name = models.CharField("Название зала", max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name="Филиал")

    def __str__(self):
        return f"{self.name} ({self.branch.name})"

    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Залы"
