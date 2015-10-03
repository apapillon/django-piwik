# -*- coding: utf-8 -*-
"""Piwik template tag."""

import logging

from django import template
from django.conf import settings

register = template.Library()


def _tracking_code():
    if settings.DEBUG:
        return {'error': 'DEBUG mode'}
    try:
        id_ = settings.PIWIK_SITE_ID
    except AttributeError:
        error = 'PIWIK_SITE_ID does not exist.'
        logging.error(error)
        return {'error': error}
    try:
        url = settings.PIWIK_URL
    except AttributeError:
        error = 'PIWIK_URL does not exist.'
        logging.error(error)
        return {'error': error}

    try:
        without_javascript = settings.PIWIK_WITHOUT_JS
    except AttributeError:
        without_javascript = False

    try:
        set_document_title = settings.PIWIK_SET_DOCUMENT_TITLE
    except AttributeError:
        set_document_title = False

    try:
        do_not_track = settings.PIWIK_SET_DO_NOT_TRACK
    except AttributeError:
        do_not_track = False

    try:
        disable_cookies = settings.PIWIK_DISABLE_COOKIES
    except AttributeError:
        disable_cookies = False
    
    return {'id': id_, 'url': url, 'setDocumentTitle': set_document_title,
        'setDoNotTrack': do_not_track, 'disableCookies': disable_cookies,
        'withoutJS': without_javascript}


@register.inclusion_tag('piwik/tracking_code.html')
def tracking_code():
    return _tracking_code()


@register.inclusion_tag('piwik/tracking_code_404.html')
def tracking_code_404():
    return _tracking_code()
