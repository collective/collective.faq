# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
from DateTime import DateTime
from plone import api
from plone.app.event.dx.behaviors import IEventBasic
from plone.app.portlets.utils import assignment_mapping_from_key
from plone.app.textfield.value import RichTextValue
from plone.namedfile.file import NamedBlobImage
from plone.portlets.constants import CONTEXT_CATEGORY
from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.portlets.interfaces import IPortletManager
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.WorkflowCore import WorkflowException
from Products.CMFPlone.interfaces import INonInstallable
from zope.component import getMultiAdapter
from zope.component import getUtility
from zope.component import queryUtility
from zope.component.interfaces import IFactory
from zope.container.interfaces import INameChooser
from zope.interface import implementer
from zope.interface import alsoProvides
from plone.dexterity.utils import createContentInContainer

import os
import pytz


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'kitconcept.faq:uninstall',
        ]


def post_install(context):
    """Post install script"""


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.


def add_catalog_indexes(context, wanted=None):
    """Method to add our wanted indexes to the portal_catalog.
    """
    catalog = api.portal.get_tool('portal_catalog')
    indexes = catalog.indexes()
    indexables = []
    for name, meta_type in wanted:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
    if len(indexables) > 0:
        catalog.manage_reindexIndex(ids=indexables)
