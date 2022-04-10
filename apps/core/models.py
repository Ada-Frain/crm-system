from asyncio.base_futures import _FINISHED
from django.db import models
from django.shortcuts import reverse

class Project(models.Model):
    FINISHED = 'Закончен'
    INWORK = 'В работе'
    STATUS_CHOICES = ((FINISHED, "Закончен"),
    (INWORK, "В работе"))

    name = models.CharField(max_length=200, db_index=True, verbose_name='Название проекта')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    contract_number = models.IntegerField(db_index=True, unique=True, verbose_name='Номер контракта')
    brand = models.CharField(max_length=200, db_index=True, verbose_name='Бренд')
    contractor = models.CharField(max_length=200, db_index=True, verbose_name='Подрядчик')
    contractor_contract = models.IntegerField(db_index=True, unique=True, verbose_name='Номер договора с подрядчиком')
    advance_payment1 = models.CharField(max_length=200, verbose_name='Аванс')
    advance_payment2 = models.CharField(max_length=200, verbose_name='Аванс')
    advance_payment3 = models.CharField(max_length=200, verbose_name='Аванс')
    final_sum = models.CharField(max_length=200, verbose_name='Итоговая сумма')
    cs_upd = models.CharField(max_length=200, verbose_name='КС/УПД')
    adress = models.CharField(max_length=200, verbose_name='Адрес')
    contacts = models.CharField(max_length=200, verbose_name='Контакты')
    engineer = models.CharField(max_length=200, verbose_name='Инженер')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=INWORK, verbose_name='Статус')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:project_detail', kwargs={"slug" : self.slug})