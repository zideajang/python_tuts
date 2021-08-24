import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter() #1
        value = func(*args,**kwargs)
        end_time = time.perf_counter() #2
        run_time = end_time - start_time#3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        
        signatre = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signatre})")
        
        value = func(*args,**kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        res_1 = func(*args, **kwargs)
        res_2 = func(*args, **kwargs)
        return res_1, res_2
    return wrapper_do_twice

@do_twice
@debug
def greet(name):
    print(f"Hello {name}")


def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)

@repeat
def greet(name):
    print(f"Hello {name}")

greet("mike")