from functools import wraps

class IntendedException(Exception):
    """
    Generic exception. If allowed exceptions is None,
    will try again if this exception is raised.
    """

class pyagain:
    """
    Decorator for retrying a specified number of times if specific errors occur.
    """
    def __init__(self, number_of_retries, allowed_exceptions=None, verbose=False):
        self.number_of_retries = number_of_retries
        self.allowed_exceptions = allowed_exceptions or (IntendedException,)
        self.verbose=verbose

    def __call__(self, func):
        @wraps(func)
        def func_again(*args, **kwargs):
            for _ in range(self.number_of_retries):
                try:
                    return func(*args, **kwargs)
                except self.allowed_exceptions as e:
                    if self.verbose:
                        print("Retrying {} after exception of type {}".format(func.__qualname__,type(e).__name__))
                    last_raised = e
            raise last_raised
        return func_again

