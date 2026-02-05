"""
Main Example Script

This script demonstrates importing and using functions from a custom module.
It shows best practices for module usage and script structure.
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))  # Add current directory to path

import example_module

def main():
    """Main function to run the script logic."""
    print("This is the main script.")
    # Use the greet function from the imported module
    greeting = example_module.greet("Python Learner")
    print(greeting)

if __name__ == "__main__":
    main()