from setuptools import setup, find_packages


long_description = ''
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='django_po_translator',
    version='1.0.1',
    description='Translate Django PO files and resolve fuzziness with ease.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=2.2.0',
        'beautifulsoup4',
        'halo',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    url='https://github.com/waseem-hamoolaila/django-po-translator',
    author='Waseem Hamoolaila',
    author_email='waseem.97.laila@gmail.com',
)