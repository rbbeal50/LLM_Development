def greet(name):
    return f"Hello, {name}. Welcome to the Python sandbox."


def main():
    print(greet("Robert"))
    for step in range(1, 4):
        print(f"Step {step}: write a small script and run it.")


if __name__ == "__main__":
    main()
