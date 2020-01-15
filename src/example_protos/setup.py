import io
from setuptools import setup, find_packages


def read(file_path):
    with io.open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


__version__ = read('__version__')
readme = read('README.md')
requirements = read('requirements.txt')


setup(
    # metadata
    name='example_protos',
    version=__version__,
    author='Andrey Grabovoy',
    description='Proto files for ExamleClient',
    long_description=readme,

    # options
    packages=find_packages(),
    install_requires='\n'.join([requirements]),
    entry_points={
        'console_scripts': [
            'example_client = example_protos.client:start',
        ]
    },
    include_package_data=True,
)