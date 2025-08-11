#!/bin/sh

pkg=$(dirname $(realpath "$0"))

pip install --user $pkg || pip install --user --break-system-packages $pkg 
