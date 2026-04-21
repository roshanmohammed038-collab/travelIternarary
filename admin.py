from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import CustomUser, TrainBooking, FlightBooking

# Customize User display in admin
class CustomUserInline(admin.StackedInline):
    model = CustomUser
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (CustomUserInline,)  # Fixed: changed 'inline' to 'inlines'
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')  # Fixed: 'date_jointed' to 'date_joined'
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')  # Fixed: 'date_jointed' to 'date_joined'

# Train Booking Admin
class TrainBookingAdmin(admin.ModelAdmin):
    list_display = ('pnr_number', 'user', 'from_station', 'to_station', 'journey_date', 'train_class', 'booking_date')  # Fixed: 'pmr_number' to 'pnr_number', 'training_date' to 'train_class'
    list_filter = ('train_class', 'status', 'journey_date', 'booking_date')
    search_fields = ('pnr_number', 'user__username', 'from_station', 'to_station')  # Fixed: 'pmr_number' to 'pnr_number', 'user_username' to 'user__username'
    readonly_fields = ('booking_date',)  # Fixed: added comma to make it a tuple

# Flight Booking Admin
class FlightBookingAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'user', 'from_airport', 'to_airport', 'departure_date', 'travel_class', 'passengers', 'booking_date', 'status')
    list_filter = ('travel_class', 'status', 'departure_date', 'booking_date')
    search_fields = ('flight_number', 'user__username', 'from_airport', 'to_airport')
    readonly_fields = ('booking_date',)

# Unregister default User admin and register with custom admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register your models
admin.site.register(TrainBooking, TrainBookingAdmin)
admin.site.register(FlightBooking, FlightBookingAdmin)