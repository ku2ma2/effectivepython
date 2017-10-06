#!/bin/sh

coverage run -m unittest discover test/

# reporting coverage
coverage report -m

# remove .coverage file
coverage erase

