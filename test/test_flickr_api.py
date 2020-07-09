#!/usr/bin/env python3
"""Tests case for flickr_api"""
import pytest
from flickr_photostream.flickr_api import FlickrInfo, FlickrApi


@pytest.fixture
def flickr_api_object():
    return FlickrApi(FlickrInfo.KEY, FlickrInfo.SECRECT)


def test_FlickrApi(flickr_api_object):
    """Test for FlickrApi object"""
    # Private attributes of consumer_key
    with pytest.raises(AttributeError) as excinfor:
        flickr_api_object.consumer_key
        assert "'FlickrApi' object has no attribute 'consumer_key'"\
            in str(excinfor.value)

