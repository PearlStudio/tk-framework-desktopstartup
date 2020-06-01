# -*- coding: utf-8 -*-

name = 'tk_framework_desktopstartup'

version = '1.11.0'

description = 'tk-framework-desktopstartup'

authors = ['Shotgunsoftware']

tools = []

requires = []

build_command = "python {root}/rezbuild.py {install}"

def commands():
    # Allows to override the Shotgun Desktop's tk-framework-desktopstartup
    # and use any one you want. This disables updates.
    env.SGTK_DESKTOP_STARTUP_LOCATION = '{root}'
    # env.SHOTGUN_DESKTOP_CONFIG_FALLBACK_DESCRIPTOR =
    # 'sgtk:descriptor:app_store?name=tk-config-basic&version=v1.1.10'
    env.SHOTGUN_DESKTOP_CONFIG_FALLBACK_DESCRIPTOR = 'sgtk:descriptor:path?path=$TK_CONFIG_BASIC_ROOT'


format_version = 2
