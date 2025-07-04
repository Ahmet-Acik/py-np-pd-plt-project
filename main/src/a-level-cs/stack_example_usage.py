from stack import Stack

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print("Top item:", stack.peek())
    print("Popped:", stack.pop())
    print("Is empty?", stack.is_empty())
