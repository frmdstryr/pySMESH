import re
from setuptools import setup


def get_version():
    with open("SMESH/__init__.py") as f:
        for line in f:
            m = re.match(r"__version__ = ['\"](.+)['\"]", line)
            if m:
                return m.group(1)
    raise ValueError("Could not find version")


setup(
    name='SMESH',
    version=get_version(),
    packages=['SMESH', 'SMESH.Visualization'],
    package_data={'SMESH': ['*.so', '*.pyd', '*.dll', 'Visualization/_resources/*']},
    author='Trevor Laughlin',
    description='Python bindings for SMESH.',
    url='https://github.com/trelau/pySMESH',
    license='LGPL v2.1',
    platforms=['Windows', 'Linux']
)
