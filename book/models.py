from django.db import models
from category_book.models import CategoryModel
from django.contrib.auth.models import User

class Book_Model(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='book_images/')
    category_name = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def reduce_quantity(self):
        if self.quantity > 0:
            self.quantity -= 1
            self.save()

class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, related_name='purchase_history', on_delete=models.CASCADE)
    book = models.CharField(max_length=50)
    category_name = models.CharField(max_length=50)
    price = models.IntegerField()
    purchased_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car} purchased by {self.user.username} on {self.purchased_on}"

