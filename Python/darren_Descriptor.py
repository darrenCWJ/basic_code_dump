import functools
import logging
from time import time

def functionruntime(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'running {func.__name__} with variables \narguments:{args} \nand kwargs:{kwargs}')
        result = func(*args, **kwargs)
        print(f'finish runnning {func.__name__}')
        return result
    return wrapper

def create_logger(): 
    #logging.config.fileConfig('logging.conf')
    #create a logger object
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
      
    #create a file to store all the 
    # logged exceptions
    logfile = logging.FileHandler('exc_logger.log')
      
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
      
    logfile.setFormatter(formatter)
    logger.addHandler(logfile)
      
    return logger


def get_default_logger():
    return create_logger()

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = get_default_logger()
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logger.info(f"function {func.__name__} called with args {signature}")
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.exception(f"Exception raised in {func.__name__}. exception: {str(e)}")
            raise e
    return wrapper


def timetorun(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):   
        ts = time()
        result = func(*args, **kwargs)
        te = time()
        print(f'finish runnning {func.__name__} in {(te - ts):.2f} seconds')
        return result
    return wrapper

def repeat(num_times = 1):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat
