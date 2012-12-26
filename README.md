Flaskberry
==========

A simple web application to manage your Raspberry Pi.

Features:
 - shutdown and reboot
 - mount and unmout disks, USB drives, etc.

Please bear in mind, that by running Flaskberry you are exposing an
unsecured power off switch to your Raspberry Pi to the network and
possibly to the whole internet when connected. Commands are executed
via sudo with with root privileges which is another potential security
problem. Please use Flaskberry only if your not storing any valuable
information on it.

Flaskberry is written in Python an uses the [Flask][1] framework.

To run Flaskberry you need Python 2.7 and Flask 0.9, a web-server and
some WSGI-Container to run the application in and ideally something for
monitoring.
I recommend [nginx][2], [uWSGI][3] or [gunicorn][4] and [supervisor][5].
There are sample configurations in the directory examples/ which assume
the application (and the file you are reading now) is stored in
/home/pi/flaskberry.

Change the SECRET_KEY in settings.py to something random.

The application itself is released under the MIT License.
It ships with a copy of [Twitter Bootstrap][6], which is licensed under
the Apache License v2.0. Twitter Bootstrap contains Icons from
Glyphicons Free, licensed under CC BY 3.0.
Raspberry Pi is a trademark of the Raspberry Pi Foundation.

2012, Rupert Angermeier


[1]: http://flask.pocoo.org/
[2]: http://nginx.org/
[3]: http://projects.unbit.it/uwsgi/
[4]: http://gunicorn.org/
[5]: http://supervisord.org/
[6]: http://twitter.github.com/bootstrap/
