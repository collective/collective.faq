# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from kitconcept.faq.testing import KITCONCEPTFAQ_CORE_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that kitconcept.faq is properly installed."""

    layer = KITCONCEPTFAQ_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if kitconcept.faq is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'kitconcept.faq'))

    def test_browserlayer(self):
        """Test that IKitconceptfaqCoreLayer is registered."""
        from kitconcept.faq.interfaces import (
            IKitconceptfaqCoreLayer)
        from plone.browserlayer import utils
        self.assertIn(IKitconceptfaqCoreLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = KITCONCEPTFAQ_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['kitconcept.faq'])

    def test_product_uninstalled(self):
        """Test if kitconcept.faq is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'kitconcept.faq'))

    def test_browserlayer_removed(self):
        """Test that IKitconceptfaqCoreLayer is removed."""
        from kitconcept.faq.interfaces import IKitconceptfaqCoreLayer
        from plone.browserlayer import utils
        self.assertNotIn(IKitconceptfaqCoreLayer, utils.registered_layers())
