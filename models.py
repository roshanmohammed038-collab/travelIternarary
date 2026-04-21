
from django.db import models
from django.contrib.auth.models import User

# User model (usually already exists via Django's built-in User)
# If you have a custom user model, it might look like this:
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

# Train Booking Model
class TrainBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_station = models.CharField(max_length=100)
    to_station = models.CharField(max_length=100)
    journey_date = models.DateField()
    train_class = models.CharField(max_length=20, choices=[
        ('Sleeper', 'Sleeper'),
        ('3A', 'AC 3 Tier'),
        ('2A', 'AC 2 Tier'),
        ('1A', 'First Class AC')
    ])
    passengers = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Confirmed')
    pnr_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.from_station} to {self.to_station} - {self.user.username}"

# Flight Booking Model
class FlightBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_airport = models.CharField(max_length=100)
    to_airport = models.CharField(max_length=100)
    departure_date = models.DateField()
    travel_class = models.CharField(max_length=20, choices=[
        ('Economy', 'Economy'),
        ('Premium Economy', 'Premium Economy'),
        ('Business', 'Business'),
        ('First Class', 'First Class')
    ])
    passengers = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Confirmed')
    flight_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.from_airport} to {self.to_airport} - {self.user.username}"
    from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    dob = models.DateField()
