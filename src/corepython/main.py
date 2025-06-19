# main.py

def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

def main():
    try:
        user_name = input("Enter your name: ")
        print(greet(user_name))
    except Exception as e:
        print(f"An error occurred: {e}")

def test_greet():
    """Test the greet function."""
    try:
        assert greet("Alice") == "Hello, Alice!"
        assert greet("Bob") == "Hello, Bob!"
        assert greet("") == "Hello, !"
        print("All tests passed!")
    except AssertionError as e:
        print(f"Test failed: {e}")
        print("Test failed due to an assertion error.")
        print("An unexpected error occurred during testing.")

if __name__ == "__main__":
    main()
    test_greet()