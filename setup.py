from setuptools import setup, find_packages
import os
import djangocms_store_locator

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]

setup(
    author="Ales Kocjancic",
    author_email="alesdotio@gmail.com",
    name='djangocms-store-locator',
    version=djangocms_store_locator.__version__,
    description='A simple store locator django CMS plugin that uses Google Maps.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='http://www.django-cms.org/',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'django-filer>=0.8',
        'django-sekizai>=0.6.1',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

