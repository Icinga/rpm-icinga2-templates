#!/bin/bash
# this script runs in the rpm_test environment

install_package icinga2-templates

ls -al /usr/share/icinga2/include
cat /usr/share/icinga2/include/itl
if [ -e /usr/share/doc/packages/icinga2-templates ]; then
  # docroot on SUSE
  ls -al /usr/share/doc/packages/icinga2-templates
else
  ls -al /usr/share/doc/icinga2-templates*/
fi
