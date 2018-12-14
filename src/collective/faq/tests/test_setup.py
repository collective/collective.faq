# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.faq.testing import COLLECTIVEFAQ_CORE_INTEGRATION_TESTING  # noqa
# from plone import api

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:  # Plone < 5.1
    HAS_INSTALLER = False
else:
    HAS_INSTALLER = True

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.faq is properly installed."""

    layer = COLLECTIVEFAQ_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        # self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer = get_installer(self.portal)

    def test_product_installed(self):
        """Test if collective.faq is installed."""
        self.assertTrue(
            # self.installer.isProductInstalled(
            #     'collective.faq'
            # )
            self.installer.is_product_installed('collective.faq')
        )

    def test_browserlayer(self):
        """Test that ICollectivefaqCoreLayer is registered."""
        from collective.faq.interfaces import (
            ICollectivefaqCoreLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectivefaqCoreLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVEFAQ_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = get_installer(self.portal)
        # self.installer = api.portal.get_tool('portal_quickinstaller')
        # self.installer.uninstallProducts(['collective.faq'])
        self.installer.uninstall_product('collective.faq')

    def test_product_uninstalled(self):
        """Test if collective.faq is cleanly uninstalled."""
        self.assertFalse(
            self.installer.is_product_installed('collective.faq')
        )

    def test_browserlayer_removed(self):
        """Test that ICollectivefaqCoreLayer is removed."""
        from collective.faq.interfaces import ICollectivefaqCoreLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectivefaqCoreLayer, utils.registered_layers())
