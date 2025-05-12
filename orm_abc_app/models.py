# import datetime
from django.db import models

c_choices = (
    (5, "пять"),
    (13, "тринадцать"),
    (15, "пятнадцать"),
    (100, "сто"),
)


class AbcModel(models.Model):
    task = models.CharField(
        verbose_name="Формулировка  задачи",
        default="Является ли ли С гипотенузой катетов A и B ?",
        max_length=255,
    )
    a = models.IntegerField(
        verbose_name="Значение А",
        default=3,
    )
    b = models.IntegerField(
        verbose_name="Значение B", default=4, help_text="Подсказка для значения B"
    )
    c = models.IntegerField(
        verbose_name="Значение С",
        choices=c_choices,
        default=5,
    )
    result = models.CharField(
        verbose_name="Результат",
        default="Результат не определен",
        max_length=255,
    )
    current_date = models.DateTimeField(
        verbose_name="Дата изменения(save)", auto_now=True
    )

    def __str__(self):
        # return self.task
        # return '%s %s' % (self.task, self.current_date)
        return f"self.id:{self.id}; self.task:{self.task}"

    class Meta:
        verbose_name = "A_B_C_Таблица"
        verbose_name_plural = "A_B_C_Таблицы"
        ordering = ("-pk", )


# current_date = models.DateTimeField("ДатаВремя", default=datetime.datetime.now())
# current_date = models.DateTimeField("ДатаВремя", auto_now_add=True)

# python manage.py makemigrations
# python manage.py migrate

# admin.py
# from django.contrib import admin
# # Register your models here.
# from .models import Abc
# admin.site.register(Abc)


# forms.py
# from django.forms import ModelForm
# from .models import Abc
#
# class CreateAbcForm(ModelForm):
#     class Meta:
#         model = Abc
#         fields = ['task', 'a' ,'b' ,'c', 'c_calc']
