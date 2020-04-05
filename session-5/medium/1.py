from time import sleep
from functools import wraps


def delay(seconds):
    output = None

    print(f"Sleeping for {seconds} second(s)")
    sleep(seconds)

    def inner_function(function):

        @wraps(function)
        def wrapper(*args, **kwargs):
            print("[START]")

            output = function(*args, **kwargs)

            print("[END]")

            return output

        return wrapper
    
    return inner_function

@delay(seconds=2)
def say_something(word):
    print(word)

def main():
    say_something("hello")


if __name__ == "__main__":
    main()
