import os
import sys
import django

# Add current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_itinerary.settings')

try:
    django.setup()
    print("SUCCESS: Django setup successful!")
except Exception as e:
    print(f"ERROR: Django setup failed: {e}")
    exit(1)

from django.core.mail import send_mail

# Test email with REAL sending
try:
    send_mail(
        'REAL EMAIL TEST - Travel Itinerary',
        'Congratulations! success hello prithvi and adithya from roshan',
        'roshanmohammed038@gmail.com',  # From email
        ['roshanmohammed038@gmail.com'],  # To email (send to yourself)
        fail_silently=False,
    )
    print("SUCCESS: REAL EMAIL SENT! Check your Gmail inbox!")
except Exception as e:
    print(f"ERROR: Failed to send real email: {e}")
    print("Please check:")
    print("1. Gmail app password is correct")
    print("2. Less secure apps is enabled or 2-factor auth with app password")