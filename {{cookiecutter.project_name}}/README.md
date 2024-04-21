# {{cookiecutter.project_name}}

{{cookiecutter.short_description}}

More information can be found on the project's [website]({{cookiecutter.url}}).

## Installation

*Add information on how to install {{cookiecutter.package_name}}.*

You can install {{cookiecutter.package_name}} using the distributed wheel via pip:
```console
python -m pip install {{cookiecutter.package_name}}-0.0.0-py3-non-any.whl
```

This installation should automatically pull and install all required dependencies from PyPI. In the case of custom 
dependencies, you can direct pip to a local server:

```console
python -m pip install {{cookiecutter.package_name}}-0.0.0-py3-none-any.whl --find-links .\dependencies
```

## Getting Started

*Add information on the typical use of {{cookiecutter.package_name}}, either as library or as a console script.*

Import the {{cookiecutter.package_name}} library in python:
```python
import {{cookiecutter.package_name}}
```

Display the help page of the console script:
```console
{{cookiecutter.package_name}} -h
```

Execute the console script:
```console
{{cookiecutter.package_name}} arg1 arg2 --optional_arg arg3
```
