from django.db import models
from django.contrib.auth.models import User
# from django.contrib.gis.db import models
# from django.contrib.gis.geos import Point

# Create your models here.
class Category(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Event(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    date = models.DateField(null=True)
    all_day = models.BooleanField()
    latitude = models.DecimalField(null=True, max_digits=8, decimal_places=5)
    longitude = models.DecimalField(null=True, max_digits=8, decimal_places=5)
    # location = models.PointField()
    # latitude = models.FloatField(min_value=-90, max_value=90)
    # latitude = models.FloatField(max_digits=3, decimal_places = 4)
    # longitude = models.FloatField(min_value=-180, max_value=180)
    # duration = models.DurationField()
    # location = models.Point()

    def __str__(self):
        return self.title

class Note(models.Model):
    # user.id???
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    note_title = models.CharField(max_length = 100)
    note_text = models.CharField(blank=True, max_length = 255)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    completed = models.BooleanField(default=False)
    due_by = models.DateTimeField(null=True)
    note_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    CHOICE_SELECTION = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]
    priority_choices = models.IntegerField(
        choices = CHOICE_SELECTION,
        default = 1
    )

    def __str__(self):
        return f"{self.note_title} - {self.note_text}"



# class Point(x=None, y=None, z=None, srid=None)¶
# Point objects are instantiated using arguments that represent the component coordinates of the point or with a single sequence coordinates. For example, the following are equivalent:

# >>> pnt = Point(5, 23)
# >>> pnt = Point([5, 23])