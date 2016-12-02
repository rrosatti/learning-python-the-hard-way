try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Advanced User Input',
    'author': 'Rodrigo R. Galvão',
    'author_email': 'rodrigo_rosatti@hotmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'name': 'ex48'
}
