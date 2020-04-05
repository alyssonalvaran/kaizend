def debug_input_output(function):
    
    def wrapper(*args, **kwargs):

        print(f"[INPUT] ARGS: {args}")
        print(f"[INPUT] KWARGS: {kwargs}")
        
        output = function(*args, **kwargs)
        
        print(f"[OUTPUT]: {output}")

        return output

    return wrapper

@debug_input_output
def say_something(word):
    print(word)

def main():
    say_something("hello")


if __name__ == "__main__":
    main()
