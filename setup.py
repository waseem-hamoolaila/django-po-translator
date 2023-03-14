from setuptools import setup

setup(
    name='django-po-translator',
    version='1.0.0',
    description='Your package description',
    packages=['po_translator'],
    install_requires=[
        'Django>=2.2.0',
        'beautifulsoup4',
        'hola',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Framework :: Django',
    ],
    url='https://github.com/your_username/your_package_name',
    author='Waseem Hamoolaila',
    author_email='waseem.97.laila@gmai.com',
)