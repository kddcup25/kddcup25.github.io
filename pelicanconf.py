#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = "Kai Sun"
# SITENAME = u'KDD Cup 2024 CRAG Workshop' #u'KDD Cup 2024 Workshop' #u'Meta KDD Cup 2024'
SITENAME = "CRAG: Comprehensive RAG Challenge"

if "SITEURL" in os.environ:
    SITEURL = os.environ["SITEURL"]
else:
    SITEURL = "https://kddcup24.github.io/"

OUTPUT_PATH = "2024/"
PATH = "2024_content/"

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "themes/customized-pelican-alchemy/alchemy"

SITEIMAGE = "/images/logo.png"

STATIC_PATHS = ["images", "pdf"]  #'extra/favicon.ico',

# EXTRA_PATH_METADATA = {
#    'extra/favicon.ico': {'path': 'favicon.ico'}
# }

# Theme-specific settings
# SITESUBTITLE = '<b>CRAG: Comprehensive RAG Challenge</b> | August 27, 2024, Barcelona, Spain' #'CRAG: Comprehensive RAG Challenge' # 'CRAG: Comprehensive RAG Benchmark' # 'Meta Comprehensive RAG Challenge' #'Workshop at KDD 2024'
DISPLAY_ARCHIVES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

DESCRIPTION = "Meta KDD Cup 2024 Workshop"
# Links
# LINKS = [('prorgram committee', '/pages/program-committee.html')]
# LINKS = ()
#        ('somedates', 'call-for-papers.html#dates'),
#        ('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#        )
ICONS = ()
SOCIAL = ()
HIDE_AUTHORS = True

CATEGORIES_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
TAGS_SAVE_AS = ""
