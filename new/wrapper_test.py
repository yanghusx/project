import logging
def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warning("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator

# @use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)

# foo()
decorator = use_logging(level="warn")
dee = decorator(foo)
dee()
