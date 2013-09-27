PyUptimeRobot
=============

What?
-----

This short Python script lets you fetch information about your
UptimeRobot monitors. I wrote it to freshen my Python n00b skills and
play with the UptimeRobot API. I would love it if you sent patches, pull
requests, etc, but there is a very nice UptimeRobot client on GitHub
already.

How?
----

1.  Verify you have:
    -   Python 2.7 or Python 3.
    -   The `requests` module, that you can install with
        `pip install requests`.
    -   The `colorama` module, optionally, for colors.

2.  Clone this Git repository.

3.  Edit `pyuptimerobot.conf` so that:
    -   The `api_url` points to the UptimeRobot API URL. You don't need
        to change this from the default value.
    -   The `api_key` string is your account key, that you can find in
        your [UptimeRobot settings][] page.

4.  Run this script without arguments (./pyuptimerobot.py)

  [UptimeRobot settings]: http://uptimerobot.com/mySettings.asp
