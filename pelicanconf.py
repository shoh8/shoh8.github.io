#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# site information
AUTHOR = 'shoh8'
SITENAME = 'shoh8 github portal'
## in develop, siteurl blank
SITEURL_ABS = SITEURL = 'https://shoh8.github.io'

# pelican configuration
PATH = 'content'

THEME = 'theme'
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True

# location lang settings
TIMEZONE = 'Asia/Tokyo'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'ja': '%Y-%m-%d(%a)',
}
DEFAULT_LANG = 'ja'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None 
AUTHOR_FEED_ATOM = None 
AUTHOR_FEED_RSS = None 
# Blogroll 
LINKS = (
         ('wish to connect to everywhere.', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/shoh8'),
        ('github', 'https://github.com/shoh8'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
