#!/bin/sh

pkg=$(dirname $(realpath "$0"))

pip uninstall nutrinfo || pip uninstall --break-system-packages nutrinfo
