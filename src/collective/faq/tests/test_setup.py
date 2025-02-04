"""Setup tests for this package."""

from collective.faq.testing import COLLECTIVEFAQ_CORE_INTEGRATION_TESTING
from plone.base.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.faq is properly installed."""

    layer = COLLECTIVEFAQ_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal)

    def test_product_installed(self):
        """Test if collective.faq is installed."""
        self.assertTrue(self.installer.is_product_installed("collective.faq"))

    def test_browserlayer(self):
        """Test that ICollectivefaqCoreLayer is registered."""
        from collective.faq.interfaces import ICollectivefaqCoreLayer
        from plone.browserlayer import utils

        self.assertIn(ICollectivefaqCoreLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVEFAQ_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal)
        self.installer.uninstall_product("collective.faq")

    def test_product_uninstalled(self):
        """Test if collective.faq is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("collective.faq"))

    def test_browserlayer_removed(self):
        """Test that ICollectivefaqCoreLayer is removed."""
        from collective.faq.interfaces import ICollectivefaqCoreLayer
        from plone.browserlayer import utils

        self.assertNotIn(ICollectivefaqCoreLayer, utils.registered_layers())
