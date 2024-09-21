#Django signals are executed synchronously. This means that when a signal is sent, the connected signal handlers are executed immediately in the same thread that sent the signal.

from django.dispatch import Signal, receiver
import time

my_signal = Signal()

@receiver(my_signal)
def my_signal_receiver(sender, **kwargs):
    print("Signal received, starting processing...")
    time.sleep(2)
    print("Processing complete.")

print("Sending signal...")
my_signal.send(sender=None)
print("Signal sent.")
