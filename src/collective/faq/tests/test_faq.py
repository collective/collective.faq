# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from collective.faq.testing import COLLECTIVEFAQ_CORE_INTEGRATION_TESTING  # noqa
from collective.faq.interfaces import IFAQ

import unittest


class FAQIntegrationTest(unittest.TestCase):

    layer = COLLECTIVEFAQ_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer = api.portal.get_tool("portal_quickinstaller")
        fti = queryUtility(IDexterityFTI, name="FAQ")
        fti.global_allow = True

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name="FAQ")
        schema = fti.lookupSchema()
        self.assertEqual(IFAQ, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name="FAQ")
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name="FAQ")
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IFAQ.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory("FAQ", "faq")
        self.assertTrue(IFAQ.providedBy(self.portal["faq"]))
