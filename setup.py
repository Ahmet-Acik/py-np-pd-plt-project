from setuptools import setup, find_packages

setup(
    name="python-data-science-tutorial",
    version="1.0.0",
    description="A comprehensive Python tutorial covering fundamentals to data science",
    author="Tutorial Author",
    packages=find_packages(where="main"),
    package_dir={"": "main"},
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
        "scikit-learn>=1.0.0",
        "flask>=3.0.0",
        "jupyter>=1.0.0",
        "pytest>=7.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)