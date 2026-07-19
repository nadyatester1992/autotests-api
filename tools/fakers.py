import time

def get_random_email() -> str:
    return f'test.{round(time.time(),2)}@example.com'