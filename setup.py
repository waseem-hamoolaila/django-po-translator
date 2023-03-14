from setuptools import setup, find_packages

setup(
    name='django_po_translator',
    version='2.1.2',
    description='Your package description',
    packages=find_packages(),
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