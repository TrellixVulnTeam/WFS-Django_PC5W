from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})	

class Job(models.Model):
	company_name = models.CharField(max_length=120)
	job_description = models.TextField()
	creator = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.company_name


# class Item(models.Model):
# 	name = models.CharField(max_length=120)
# 	description = models.TextField()
# 	price = models.IntegerField()

# 	def __str__(self):
# 		return self.name.description.price

# class Order(models.Model):
# 	item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
# 	order_quantity = models.IntegerField()
# 	# order_details = models.ManyToManyField(through=OrderDetails)

# class OrderDetails(models.Model):
# 	order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
# 	item_id = models.ForeignKey(Item, on_delete=models.CASCADE)

