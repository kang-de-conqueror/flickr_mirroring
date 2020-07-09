#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetching Information from Flickr API"""

import logging


# Set logging
logging.basicConfig(
    filename='debug.log',
    level=logging.DEBUG,
    filemode='w',
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%H:%M:%S')


class FlickrInfo:
    KEY = 'fe3a4ac5b4c6b00883b55ffc36d61d5b'
    SECRECT = '542f483981d6a56d'
    USER_ID = '188102681@N02'
    END_POINT = 'https://www.flickr.com/services/rest'



class FlickrApi:
    """A Class of Key and Secrect of a Flickr API"""

    def __init__(self, consumer_key, consumer_secret):
        """The constructor of FlickApi

        Args:
            consumer_key (str): A Flickr member key
            consumer_secret (str): A Flickr menter secrect
        """
        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret

