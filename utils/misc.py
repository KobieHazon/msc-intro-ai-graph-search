"""
misc utility functions.
"""
import threading

try:
    import thread
except ImportError:
    import _thread as thread


# dict on python 3.7+ preserves insertion order.
# This is a quick way to create a set which preserves it as well.
# required for presentation purposes only.
def ordered_set(coll):
    """
    returns ordered set from collection.
    taken from course github.
    """
    return dict.fromkeys(coll).keys()


def quit_function():
    thread.interrupt_main()  # raises KeyboardInterrupt


def exit_after(s):
    """
    use as decorator to exit process if function takes longer than s seconds.
    Notice that it disables the ability to use ctrl-c to exit code running inside decorated function.
    can't catch KeyboardInterrupt. Need to kill with SIGKILL.
    """

    def outer(fn):
        def inner(*args, **kwargs):
            timer = threading.Timer(s, quit_function)
            timer.start()
            result = None
            try:
                try:
                    result = fn(*args, **kwargs)
                finally:
                    timer.cancel()
            except KeyboardInterrupt:
                pass
            return result

        return inner

    return outer
