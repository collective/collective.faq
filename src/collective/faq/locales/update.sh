#!/bin/bash
# For every language you want to translate into you need a
# locales/[language]/LC_MESSAGES/collectivefaq.po
# (e.g. locales/de/LC_MESSAGES/collectivefaq.po)

# Use i18ndude when it is on the PATH, else call it via uvx.
if test "$(which i18ndude)" != ""; then
    I18NDUDE=i18ndude
else
    I18NDUDE="uvx i18ndude"
fi

domain=collective.faq

$I18NDUDE rebuild-pot --pot $domain.pot --create $domain ../
$I18NDUDE sync --pot $domain.pot */LC_MESSAGES/$domain.po
