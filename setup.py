import re
from setuptools import setup, find_packages

with open('gopad/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(),
                        re.MULTILINE).group(1)

if not version:
    raise RuntimeError('cannot find version information')

setup(
    name='gopad',
    version=version,
    author='Thomas Boerger',
    author_email='thomas@webhippie.de',
    description='etherpad for markdown with go',
    long_description=open('README.rst').read(),
    license='Apache License 2.0',
    keywords='etherpad markdown',
    url='https://github.com/gopad/gopad-python',
    install_requires=[],
    entry_points={},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(exclude=['tests']),
    package_data={'': ['LICENSE', '*.txt', '*.rst']},
    tests_require=['nose'],
    test_suite='nose.collector',
)
