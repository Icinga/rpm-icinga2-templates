#!/bin/bash
# this script runs in the rpm_test environment

install_package icinga2-templates

ls -al /usr/share/icinga2/include
cat /usr/share/icinga2/include/itl
ls -al /usr/share/doc/icinga2-templates*/
