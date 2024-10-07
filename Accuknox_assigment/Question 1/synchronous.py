from django.dispatch import Signal, receiver

# Define a signal
simple_signal = Signal()

@receiver(simple_signal)
def signal_handler(sender, **kwargs):
    print("Signal handled!")

# Send the signal
print("Sending signal...")
simple_signal.send(sender=None)
print("Signal sent!")


# The handler runs immediately after the signal is sent,
# which is why "Signal handler executed!" appears before "Signal sent!" This confirms that Django signals are executed synchronously.


# # Synchronous Signals**: All signals are executed synchronously by default, meaning the code waits for signal handlers to finish.