from setuptools import setup, find_packages

setup(
    name="emotion-detector",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "flask>=2.0.0",
        "watson-nlp>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pylint>=2.0.0",
            "flake8>=5.0.0",
        ]
    },
    python_requires=">=3.8",
)
