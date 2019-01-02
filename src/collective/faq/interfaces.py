# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from plone.supermodel import model
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectivefaqCoreLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IFAQ(model.Schema):
    """FAQ content type interface."""


class IFAQItem(Interface):
    """FAQ Item content type interface."""
