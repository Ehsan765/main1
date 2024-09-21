#Django signals are a way to allow different parts of your application to communicate,When a signal is emitted, the functions that respond to that signal run in the same thread where the signal was triggered,This means that if you're working in a background thread and you emit a signal, the handler for that signal will also run in that background thread, not in the main thread or any other thread.


from django.dispatch import Signal,receiver
import threading
signals=Signal()
@receiver(signals)
def signal_handler(sender, **ehsan):
    print(f"Handler running in thread:{threading.current_thread().name}")

def emit_signal():
    print(f"Emitting signal in thread:{threading.current_thread().name}")
    signals.send(sender=None)
new_thread = threading.Thread(target=emit_signal, name='MyThread')
new_thread.start()
new_thread.join()