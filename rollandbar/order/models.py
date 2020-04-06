from datetime import datetime

from django.db import models


class CreatedUpdatedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(CreatedUpdatedModel):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Dish(CreatedUpdatedModel):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True, upload_to='static/dishes')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.FloatField(null=True, blank=True)
    ingredients = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name

    @property
    def discount(self):
        current_time = datetime.now()
        return Discount.objects.where(
            dish=self,
            start_time__lte=current_time,
            deadline__gte=current_time,
        ).first()


class Discount(CreatedUpdatedModel):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    percent = models.FloatField(null=True, blank=True)
    fix_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deadline = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return f'{self.dish} - {self.deadline}'

    # @property
    def total_dish_price(self):
        if self.fix_price:
            return self.fix_price
        elif self.percent:
            return self.dish.price / 100 * self.percent
        else:
            ValueError('Discount does have fix_price or percent')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # TODO проверять что за выбраный период нет скидок
        pass


class Client(CreatedUpdatedModel):
    name = models.CharField(max_length=256, blank=True)
    phone = models.CharField(max_length=256)
    address = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Order(CreatedUpdatedModel):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    receiving_date = models.DateTimeField(
        help_text='Дата/время получения заказа', blank=True, null=True,
    )
    is_delivery = models.BooleanField(help_text='Доставка или самовывоз')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Position(CreatedUpdatedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dish = models.ForeignKey(Dish, on_delete=models.PROTECT)
    discount = models.ForeignKey(Discount, blank=True, null=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'

    def save(self, *args, **kwargs):
        discount

        if self.discount and (self.discount.fix or self.discount.percent):
            if self.discount.fix:
                self.final_price = self.discount.fix
            else:
                self.final_price = self.dish.price / 100 * self.discount.percent
        else:
            self.final_price = self.dish.price

        return super().save(*args, **kwargs)
