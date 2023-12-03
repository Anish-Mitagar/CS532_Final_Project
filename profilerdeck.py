import uuid
import cProfile
import os
from functools import wraps

# This came from TA Andy Zane

# Fun fact, you can't use this directly on async functions, only on sync functions that call async functions.


# Profile decorator
def profile(func):
    @wraps(func)
    def function_to_profile(*args, **kwargs):

        profile_ = cProfile.Profile()
        profile_.enable()

        try:
            val = func(*args, **kwargs)
            return val
        finally:

            profile_.disable()

            filename = func.__name__ + "-" + uuid.uuid4().hex + ".prof"

            dir_ = os.path.abspath("_profiles")
            # print("writing", filename, "to", dir_)
            if not os.path.isdir(dir_):
                os.makedirs(dir_, exist_ok=True)

            profile_.dump_stats(os.path.join(dir_, filename))

    return function_to_profile