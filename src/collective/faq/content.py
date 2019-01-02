# -*- coding: utf-8 -*-
from .interfaces import IFAQ
from .interfaces import IFAQItem
from plone.dexterity.content import Container
from plone.dexterity.content import Item
from zope.interface import implementer


@implementer(IFAQ)
class FAQ(Container):
    """FAQ content type."""


@implementer(IFAQItem)
class FAQItem(Item):
    """FAQ Item content type."""
