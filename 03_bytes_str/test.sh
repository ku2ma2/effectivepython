#!/bin/sh

coverage run -m unittest discover tests/

# reporting coverage
coverage report

# remove .coverage file
coverage erase

