import versioneer
from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tv-extract',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Team Viewer - Data Extract for analysis',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/rappdw/tv-extract',

    author='rappdw',
    author_email='rappdw@gmail.com',

    license='MIT',
    keywords='library',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Version Control :: Git',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,

    install_requires=[
        'dataclasses;python_version<"3.7"',
        'gitpython',
        'multiprocessing_logging',
        'ordered-set',
    ],

    extras_require={
        'dev': [
            'wheel>=0.30.0',
            'twine'
        ],
        'test': [
            'pytest',
            'pytest-cov',
        ],
    },

    entry_points={
        'console_scripts': [
            'extract = tv_extract.extract:extract',
        ],
    },
)
