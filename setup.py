from ensurepip import version
from setuptools import setup
from setuptools import find_packages

setup(
    name="teste-tecnico-byne",
    version="1",
    author="Matheus Nascimento S. M. de Lima",
    author_email="matheus.marques_96@hotmail.com",
    packages=find_packages(),
    install_requires=[
        "Flask",
        "Click",
        "gunicorn",
        "itsdangerous",
        "Jinja2",
        "Werkzeug",
        "flask-restx",
        "requests",
        "MarkupSafe",
        "pip",
        "setuptools",
        "python-dotenv",
        "motor",
        "pymongo",
        "dnspython",
        "nest_asyncio",
    ],
)
