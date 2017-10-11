#!/bin/sh

coverage run -m unittest discover tests/

# reporting coverage
coverage report -m

# remove .coverage file
coverage erase

