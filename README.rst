Django-Piwik
============

A simple app to add the Piwik JS tracking code to your template.


Requirements
------------

 * Django


Installation
------------

Using PyPI you can simply type into a terminal:

    pip install git+https://github.com/apapillon/django-piwik.git

or (source)

    pip install django-piwik

or

    easy_install django-piwik


Configuration
-------------

Add ``piwik`` to the list of ``INSTALLED_APPS`` in your ``settings.py`` file.

Also ``PIWIK_SITE_ID`` (e.g. ``1``) and ``PIWIK_URL`` (e.g. ``'piwik.example.com'``) are required.

``PIWIK_SET_DOCUMENT_TITLE`` 
Set to True to prepend the site domain to the page title when tracking (default: False)

``PIWIK_SET_DO_NOT_TRACK`` 
Set to True to enable client side DoNotTrack detection (default: False)

``PIWIK_DISABLE_COOKIES`` 
Set to True to disable all tracking cookies (default: False)

``PIWIK_WITHOUT_JS`` 
Set to True to not use JavaScript to track visitors (default: False)

In the template, put ``{% load piwik_tags %}`` to the top and add ``{% tracking_code %}`` before the ``</body>`` tag.


That's it. Happy tracking!

TODOs
-----
Add this options :

``PIWIK_SET_COOKIE_DOMAINS``
To track visitors across all subdomains of your site

``PIWIK_SET_DOMAINS``
To hide clicks to known alias URLs of your site in the "Outlinks" report

Author
------

Copyright 2013 Raphael Jasjukaitis <webmaster@raphaa.de>
Copyright 2015 Jørn Åne de Jong <jornane@uninett.no>
Copyright 2015 Anthony Papillon <apapillon@perhonen.fr>


Released under the BSD license.
