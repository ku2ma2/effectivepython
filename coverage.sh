#!/bin/sh

coverage run -m unittest discover -s tests -p "test_*.py" 

# reporting coverage
coverage report -m

# remove .coverage file
coverage erase

