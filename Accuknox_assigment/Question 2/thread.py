import threading
from django.dispatch import Signal, receiver

# Define a signal
simple_signal = Signal()

@receiver(simple_signal)
def signal_handler(sender, **kwargs):
    print(f"Handler running in thread: {threading.current_thread().name}")

# Send the signal
print(f"Signal sent from thread: {threading.current_thread().name}")
simple_signal.send(sender=None)

# Both the signal sender and the handler run in the MainThread. This demonstrates that Django signals execute in the same thread as the caller.

