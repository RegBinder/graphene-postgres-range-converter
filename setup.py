from setuptools import find_packages, setup

setup(
    name='graphene-postgres-range-converter',
    version='1.0',

    description='Graphene Postgres Range Object Converter',
    long_description=open('README.rst').read(),

    url='https://github.com/RegBinder/graphene-postgres-range-converter.git',

    author='Greg Svitak',
    author_email='greg@complion.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    keywords='api graphql protocol rest relay graphene',

    packages=find_packages(exclude=['tests']),

    install_requires=[
        'six>=1.10.0',
        'graphene>=1.0',
        'singledispatch>=3.4.0.3',
        'psycopg2>=2.5'
    ],
    tests_require=[
        'pytest>=2.7.2',
        'mock'
    ],
)
