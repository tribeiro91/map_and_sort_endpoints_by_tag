# map_and_sort_endpoints_by_tag

The script is responsible for read the OpenAPI file, get the tags, get the endpoints details and, with all this information, sort ascending the endpoints grouped by tags. You can use this script to get information about the OpenAPI file or map the site navigation for your documentation site.

This script is compatible with OpenAPI Specification version 2.

## Version
1.0.0

## Prerequisites
Python 3

### Installing Python 3

Make sure that you have Python3 installed on your machine.

You might want to use venv standard Python library to create virtual environments and have Python, pip and all dependent packages to be installed and served from the local project directory to avoid messing with system wide packages and their versions.

Depending on your installation you might have access to Python3 interpreter either by running python or python3. The same goes for pip package manager - it may be accessible either by running pip or pip3.

You may check your Python version by running:

`python --version`
Note that in this repository whenever you see python it will be assumed that it is Python 3.

## Running the code

`python .\map_endpoint_by_group.py`



