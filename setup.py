
from setuptools import setup, find_packages
from hashit.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='hashit',
    version=VERSION,
    description='MyApp Does Amazing Things!',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Rudolf Luthi',
    author_email='rudy@designs-machinations.com',
    url='https://github.com/rrluthi/hashit/',
    license='mit',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'hashit': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        hashit = hashit.main:main
    """,
)
