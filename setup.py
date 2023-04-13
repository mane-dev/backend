from setuptools import setup, find_packages

setup(
    name="meticulous_backend",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'meticulous-backend=core.meticulous_backend:main',
        ],
    },
    classifiers=[
        # See: https://pypi.org/classifiers/
    ],
    author="Meticulous Home",
    author_email="your.email@example.com",
    description="A brief description of your project",
    license="MIT",
)
