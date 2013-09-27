#!/usr/bin/env python
# PyUptimeRobot, a small UptimeRobot API client.
#
#Copyright (C) 2013 Enric Morales
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program. If not, see <http://www.gnu.org/licenses/>.

import requests
import configparser

# Try to import the colorama module for nice colours, or
# just set a blank color to continue loading the program without
# this module.
try:
    import colorama
    colorama.init(autoreset=True)
    color_yellow = colorama.Fore.YELLOW
    color_red = colorama.Fore.RED
    color_green = colorama.Fore.GREEN
    color_magenta = colorama.Fore.MAGENTA
    color_cyan = colorama.Fore.CYAN
except ImportError as NameError:
    print('[INFO] Install the "colorama" module for pretty colors.')
    color_yellow = ''
    color_red = ''
    color_green = ''
    color_magenta = ''
    color_cyan = ''


# Read the configuration file. Edit pyuptimerobot.conf accordingly.
config = configparser.ConfigParser()
config_file = 'pyuptimerobot.conf'
config.read(config_file)
url = config['main']['api_url']
api_key = config['main']['api_key']

# Default payload the requests module will provide.
def_payload = {'apiKey': api_key,
               'format': 'json',
               'noJsonCallback': '1'}

# A table which translates machine names into human terms.
humanize = {'id': 'ID',
            'friendlyname': 'Alias',
            'url': 'Address',
            'status': 'Status',
            'alltimeuptimeratio': 'All-Time'}


def format_monitor(d):
    """
    (d) -> (d)

    Humanizes and alters the values of the monitor
    dictionary (d) it is passed.
    """

    status_values = {'0': color_yellow + 'Paused',
                     '1': 'Not checked yet',
                     '2': color_green + 'Up',
                     '8': color_magenta + 'Seems down',
                     '9': color_red + 'Down'}

    cur_status = d['status']
    d['status'] = status_values[cur_status]

    d['alltimeuptimeratio'] = d['alltimeuptimeratio'] + '%'

    return d


def get_request_json(action, payload=def_payload):
    r = requests.get(url + action, params=payload)
    return r.json()


def get_monitors():
    """
    () -> lots of str ;)

    Retrieves and prints the information about all monitors.
    """
    print('[INFO] Requesting stats from UptimeRobot.')
    reply = get_request_json('getMonitors')

    # If the request was successful, proceed.
    if reply['stat'] == 'ok':
        monitors = reply['monitors']['monitor']
        print('[INFO] Received info for', len(monitors), 'monitors.')

        # Order in which the output will be displayed. You can add more
        # things to output by adding strings to this list
        out_order = ['friendlyname', 'url',
                     'status', 'alltimeuptimeratio']

        for monitor in monitors:
            # Now we pass the monitor dictionary for some formatting and
            # editing.
            monitor = format_monitor(monitor)
            print('')
            print('Monitor #' + monitor['id'])
            print('-' * 18)
            for key in out_order:
                # We could output the JSON key names, but maybe human
                # concepts would be nicer.
                print('{:>9}: {:}'.format(humanize[key], monitor[key]))
    else:
        print("[ERROR]: Couldn't get the monitors from UptimeRobot. Please")
        print("check your API keys.")

if __name__ == '__main__':
    get_monitors()
