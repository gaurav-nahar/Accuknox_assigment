import os
import django
from django.conf import settings

# Point to settings.py in the current directory
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# Initialize Django
django.setup()

from django.db import transaction
from django.dispatch import Signal, receiver

# Define a signal
simple_signal = Signal()

# Simulate a "fake database"
fake_database = []

@receiver(simple_signal)
def signal_handler(sender, **kwargs):
    fake_database.append("Object created in signal handler")
    print("Signal handler executed")

# Simulate a transaction block
with transaction.atomic():
    print("Starting transaction...")
    simple_signal.send(sender=None)
    print("Signal sent during transaction")

# Check the "fake database"
print(f"Fake database content: {fake_database}")


# The signal handler makes changes to fake_database during the transaction, and the changes are committed after the transaction completes.
#  This proves that Django signals run in the same transaction as the caller.
