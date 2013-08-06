*Appmag.in*
=====================

Description:
------------------
Appmag is a one stop shop for the Mobile App lovers. Mobile Apps of all the leading platforms can be
accessed at a single place at appmag. Apps can be searched basing on the category, platform, device and
developer. 

Installation:
------------------
* `pip install -r requirements`
* `cp local_settings.py-dist local_settings.py`
* `edit local_settings.py as required`
* `python manage.py syncdb --noinput`
* `python manage.py collectstatic`
* `python manage.py runserver`


Features:
-------------------
- List of Platforms.
- Categories.
- Developers.
- Device.
- Related Apps
- Search basing on users need.
- Availability of all leading platforms.


Running Tests:
-------------------
python manage.py test

