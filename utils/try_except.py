# utils/try_except.py
class TryExcept:
    def __init__(self, error_message=None):
        self.error_message = error_message

    def __call__(self, func):
        def wrapped_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if self.error_message:
                    print(self.error_message)
                print(f"Error: {e}")
                return None
        return wrapped_func