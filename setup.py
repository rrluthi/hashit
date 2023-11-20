from setuptools import setup, find_packages
from sfed.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='sfed',
    version=VERSION,
    description='SFED encodes, decodes, hashes strings and files and generates unique identifiers.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Rudolf Luthi',
    author_email='rudy@designs-machinations.com',
    url='https://github.com/rrluthi/sfed/',
    license='mit',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'sfed': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        sfed= sfed.main:main
    """,
)
