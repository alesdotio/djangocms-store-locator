========================
django CMS Store locator
========================

A simple store locator plugin for django CMS that uses Google Maps.
The code is heavily inspired by a similar plugin by Mark Ransom, https://github.com/MegaMark16/django-cms-storelocator.

Features
========

* django CMS Plugin displays a google map with locations
* search for locations in range of an address
* locations can be grouped and searched by location types
* setting for kilometers or miles


Installation
============

* ``pip install djangocms-store-locator`` (requires ``django-filer`` and ``django-sekizai``)
* add ``'djangocms_store_locator'`` to your INSTALLED_APPS
* ``python manage.py syncdb`` or ``python manage.py migrate djangocms_store_locator`` if you are using South
* add something like this to your urls.py

::

    url(r'^store-locator/', include('djangocms_store_locator.urls')),

* done!


Usage
=====

* add some locations in the admin
* insert the "Store Locator Plugin" on a page


Optional settings
=================

* see ``settings.py``
