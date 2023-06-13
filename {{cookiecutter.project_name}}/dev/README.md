# Development

This directory contains a number of scripts to make the development work on {{cookiecutter.project_name}} a bit easier.

## Initial Setup
After checking out the right branch or version of the {{cookiecutter.project_name}} repository, make sure you update the dependency files, package files and test files. This is done by executing the ``pull_*.bat`` files in the dependency, {{cookiecutter.package_name}}/data and tests/data folders, respectively.

It is preferred to develop and test {{cookiecutter.project_name}} in a separate virtual environment. The ``0_create_environment.bat`` script creates a new environment ``{{cookiecutter.package_name}}_env``, overwriting it if it already exists, based on python 3.8. The following assumes you run the development python scripts within this environment.

## Development and Testing
### Development Installation
To be able to develop the ``{{cookiecutter.package_name}}`` package and test it at the same time, you should install the package in editable mode. This can be done with the ``1_install_editable.py`` script. 

### Testing
Testing can be done by running pytest on the test folder, as illustrated by the example script ``testing/x_test_console.py``. Some simple test functions are already provided to test the workings of the console entrypoint to the package.

## Packaging
### Building the Installation Wheel
After development is complete, a proper installation file, or wheel, can be built of the ``{{cookiecutter.package_name}}`` package. We propose to use the pip build system, which is provided in the ``2a_build_wheel.py`` script. This script will generate an intermediate build folder and a final dist folder, both not tracked by git. The final dist folder will also contain all dependencies the ``{{cookiecutter.package_name}}`` package relies on.  

### Final Installation
To test a final installation, install ``{{cookiecutter.package_name}}`` as a proper python package. Again, this can be done by running the ``2b_install_wheel.py`` and note that it uses the currently activated environment.

## Other tasks
### Build Documentation
It is always a good thing to provide documentation to your end-user and to your future self or colleague. In the docs folder, you can create custom documentation using reStructuredText (.rst) files. A basic configuration of the documentation is already provided that collects the main README of {{cookiecutter.project_name}} and generates an API reference page of the ``{{cookiecutter.package_name}}`` package. To build the documentation, simply run ``3a_build_documentation.py``.

## Release Package
When ready, the ``{{cookiecutter.package_name}}`` wheel file together with the dependencies and documentation can be deployed to a remote pypi server or network share.