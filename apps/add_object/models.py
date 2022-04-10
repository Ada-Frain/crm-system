from django.db import models
from apps.core.models import Project


class Project1(models.Model):
    FINISHED = 'Закончен'
    INWORK = 'В работе'
    STATUS_CHOICES = ((FINISHED, "Закончен"),
    (INWORK, "В работе"))

    name = models.CharField(max_length=200, db_index=True, verbose_name=u'Название проекта')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    contract_number = models.IntegerField(db_index=True, unique=True, verbose_name=u'Номер контракта')
    brand = models.CharField(max_length=200, db_index=True, verbose_name=u'Бренд')
    contractor = models.CharField(max_length=200, db_index=True, verbose_name=u'Подрядчик')
    contractor_contract = models.IntegerField(db_index=True, unique=True, verbose_name=u'Номер договора с подрядчиком')
    advance_payment1 = models.CharField(max_length=200, verbose_name=u'Аванс')
    advance_payment2 = models.CharField(max_length=200, verbose_name=u'Аванс')
    advance_payment3 = models.CharField(max_length=200, verbose_name=u'Аванс')
    final_sum = models.CharField(max_length=200, verbose_name=u'Итоговая сумма')
    cs_upd = models.CharField(max_length=200, verbose_name=u'КС/УПД')
    adress = models.CharField(max_length=200, verbose_name=u'Адрес')
    contacts = models.CharField(max_length=200, verbose_name=u'Контакты')
    engineer = models.CharField(max_length=200, verbose_name=u'Инженер')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=INWORK, verbose_name=u'Статус')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return self.name