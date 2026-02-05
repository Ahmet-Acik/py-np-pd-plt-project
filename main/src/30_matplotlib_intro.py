"""
Matplotlib Introduction

This file provides an introduction to Matplotlib, a plotting library for Python.
It covers basic plots, customization, and best practices for data visualization.
"""

import matplotlib.pyplot as plt
import numpy as np

def demonstrate_basic_plots():
    """Demonstrate basic plotting with Matplotlib."""
    print("=== Basic Plots ===")

    # Line plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)
    plt.title('Sine Wave')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

def demonstrate_multiple_plots():
    """Demonstrate multiple plots in one figure."""
    print("=== Multiple Plots ===")

    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.figure(figsize=(12, 5))

    # Subplot 1
    plt.subplot(1, 2, 1)
    plt.plot(x, y1, 'r-', label='sin(x)')
    plt.title('Sine Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

    # Subplot 2
    plt.subplot(1, 2, 2)
    plt.plot(x, y2, 'g--', label='cos(x)')
    plt.title('Cosine Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def demonstrate_bar_chart():
    """Demonstrate bar chart creation."""
    print("=== Bar Chart ===")

    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 78, 32]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(categories, values, color=['red', 'green', 'blue', 'orange', 'purple'])

    plt.title('Sample Bar Chart')
    plt.xlabel('Categories')
    plt.ylabel('Values')

    # Add value labels on bars
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                str(value), ha='center', va='bottom')

    plt.show()

def demonstrate_scatter_plot():
    """Demonstrate scatter plot with random data."""
    print("=== Scatter Plot ===")

    np.random.seed(42)
    x = np.random.randn(100)
    y = np.random.randn(100)
    colors = np.random.rand(100)
    sizes = 1000 * np.random.rand(100)

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
    plt.colorbar(label='Color Intensity')

    plt.title('Random Scatter Plot')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.grid(True, alpha=0.3)

    plt.show()

def demonstrate_histogram():
    """Demonstrate histogram plotting."""
    print("=== Histogram ===")

    np.random.seed(42)
    data = np.random.normal(0, 1, 1000)

    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=30, alpha=0.7, color='skyblue', edgecolor='black')

    plt.title('Normal Distribution Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)

    # Add mean line
    mean_val = np.mean(data)
    plt.axvline(float(mean_val), color='red', linestyle='--', linewidth=2,
                label=f'Mean: {mean_val:.2f}')
    plt.legend()

    plt.show()

def demonstrate_pandas_plotting():
    """Demonstrate plotting with Pandas integration."""
    print("=== Pandas Plotting ===")

    try:
        import pandas as pd

        # Create sample data
        dates = pd.date_range('2023-01-01', periods=30)
        values = np.random.randn(30).cumsum()

        df = pd.DataFrame({'Date': dates, 'Value': values})
        df.set_index('Date', inplace=True)

        plt.figure(figsize=(10, 5))
        df['Value'].plot(kind='line', color='purple', linewidth=2)

        plt.title('Time Series Plot with Pandas')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()

    except ImportError:
        print("Pandas not available for this demonstration")

def main():
    """Main function to run all Matplotlib demonstrations."""
    print("Matplotlib Introduction Examples\n")

    try:
        # Note: plt.show() will display plots interactively
        # In a script, you might want to save figures instead
        print("Note: Plots will display in interactive window.")
        print("Close each plot window to continue to the next.\n")

        demonstrate_basic_plots()
        demonstrate_multiple_plots()
        demonstrate_bar_chart()
        demonstrate_scatter_plot()
        demonstrate_histogram()
        demonstrate_pandas_plotting()

        print("All Matplotlib examples completed!")

    except Exception as e:
        print(f"Error in Matplotlib demonstration: {e}")

if __name__ == "__main__":
    main()