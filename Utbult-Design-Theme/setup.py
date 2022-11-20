from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
    name="mkdocs-utbult-design",
    version=VERSION,
    url='https://website.com',
    license='None',
    description='Theme for Utbult Design site',
    author='Josef Utbult',
    author_email='josef@utbult.design',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'utbult-design = utbult_design_theme',
        ]
    },
    zip_safe=False
)