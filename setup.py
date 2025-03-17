"""Installer for the collective.faq package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="collective.faq",
    version="3.0.0",
    description="Plone addon package for managing FAQ sections",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: 6.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone",
    author="kitconcept GmbH",
    author_email="info@kitconcept.com",
    url="https://github.com/collective/collective.faq",
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["collective"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "plone.api",
        "plone.app.textfield",
        "plone.base",
        "plone.dexterity",
        "plone.supermodel",
        "Products.GenericSetup>=1.8.2",
        "setuptools",
        "zope.i18nmessageid",
        "zope.interface",
        "zope.publisher",
        "zope.schema",
    ],
    python_requires=">=3.9",
    extras_require={
        "test": [
            "plone.app.testing",
            "plone.app.contenttypes[test]",
            "plone.browserlayer",
            "zope.component",
        ],
    },
    entry_points="""
    [plone.autoinclude.plugin]
    target = plone
    """,
)
