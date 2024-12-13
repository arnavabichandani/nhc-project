"""
Helper Functions
Formatting: Black
"""

import time
import logging


def func_timer(func):
    """
    A decorator that times how long a function takes to run
    and logs the execution time.
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        logging.info(f"Starting '{func.__name__}'...")
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(
            f"Finished '{func.__name__}'. Elapsed time: {elapsed_time:.4f} seconds"
        )
        return result

    return wrapper
