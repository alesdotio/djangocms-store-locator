========================
django CMS Store locator
========================

A simple store locator plugin for django CMS that uses Google Maps.
The code is heavily inspired by a similar plugin by Mark Ransom, https://github.com/MegaMark16/django-cms-storelocator.

Installation
============

* ``pip install djangocms_store_locator`` (requires ``django-filer`` and ``django-sekizai``)
* add ``'djangocms_store_locator'`` to your INSTALLED_APPS
* ``python manage.py syncdb`` or ``python manage.py migrate djangocms_store_locator`` if you are using South
* add something like this to your urls.py

::

    url(r'^store-locator/', include('djangocms_store_locator.urls')),

* done!


Usage
=====

* add some locations in the admin
* insert the Store Locator Map Plugin on a page


Optional settings
=================

* see ``settings.py``
