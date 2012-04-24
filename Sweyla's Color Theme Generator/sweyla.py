import os
import math
import random
import urllib

import sublime
import sublime_plugin

DOWNLOAD_URL = 'http://themes.sweyla.com/textmate/Sweyla%d.tmTheme'
settings = sublime.load_settings('Preferences.sublime-settings')
package_path = os.getcwdu()

for folder in ['Bright', 'Dark']:
    path = os.path.join(package_path, folder)
    if not os.path.exists(path):
        os.mkdir(path)


def generate_seed(dark):
    seed = 100000 + math.floor(399999 * random.random())
    if dark:
        seed += 500000
    return seed


class GenerateThemeCommand(sublime_plugin.ApplicationCommand):
    def run(self, dark):
        url = DOWNLOAD_URL % generate_seed(dark)
        filename = os.path.split(url)[1]

        if dark:
            path = os.path.join(package_path, 'Dark', filename)
        else:
            path = os.path.join(package_path, 'Bright', filename)

        urllib.urlretrieve(url, path)
        settings.set('color_scheme', '/'.join(path.split('\\')[-4:]))
        sublime.save_settings('Preferences.sublime-settings')
