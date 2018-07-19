import versioneer
from setuptools import setup, find_packages

setup(
    name='tv-extract',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Team Viewer - Data Extract for analysis',
    long_description='''
tv_extract extracts analytics information for Team Viewer. Currently the data extract source is git repositories, but
other data sources will be added in the future.
''',
    url='',

    author='rappdw',
    author_email='rappdw@gmail.com',

    license='MIT',
    keywords='library',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Python :: Library',
        'License :: MIT',
        'Programming Language :: Python :: 3.7',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,

    setup_requires=[
        # Setuptools 18.0 properly handles Cython extensions.
        'setuptools>=18.0'
    ],
    install_requires=[
        'gitpython',
        'multiprocessing_logging',
        'ordered-set',
    ],

    extras_require={
        'dev': [
            'wheel>=0.30.0'
        ],
        'test': [
        ],
    },

    entry_points={
        'console_scripts': [
            'extract = tv_extract.extract:extract',
        ],
    },
)
