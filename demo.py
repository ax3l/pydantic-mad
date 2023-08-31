#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-

import pydantic

import json
import toml  # Python 3.11 tomllib
import yaml

from schema import Line
from schema.elements import Drift, SBend, Marker

print(pydantic.__version__)


# define
line = Line(line=[
        Drift(ds=1.0),
        SBend(ds=0.5, rc=5),
        Marker(name="midpoint"),
    ]
)
line.line.extend([
    Line(line=[
        Drift(ds=1.0),
        Marker(name="otherpoint"),
        SBend(ds=0.5, rc=5, name="special-bend"),
        SBend(ds=0.5, rc=5),
    ])
])

# doc strings
print(SBend.__doc__)
#help(SBend)  # more to explore for simplified output, like pydantic-autodoc in Sphinx

# export
print(f"Python:\n{line}")
model = line.model_dump(mode='json', exclude_none=True)
print(f"JSON model:\n{model}")
model_py = line.model_dump(mode='python', exclude_none=True)
print(f"Python model:\n{model_py}")


model_json = json.dumps(line.model_dump(exclude_none=True), sort_keys = True, indent = 4)
print(model_json)

with open('line.pmad.json', 'w') as out_file:
    out_file.write(model_json)


# import
with open('line.pmad.json', 'r') as in_file:
    read_json_dict = json.loads(in_file.read())

print(read_json_dict)

# validate
read_json_model = Line(**read_json_dict)
print(read_json_model)

# ensures correctness in construction, read-from-file
# AND in interactive use
try:
    Drift(ds=-1.0)  # fails with: Input should be greater than 0
except pydantic.ValidationError as e:
    print(e)

try:
    d = Drift(ds=1.0)
    d.ds = -1.0  # fails with: Input should be greater than 0
except pydantic.ValidationError as e:
    print(e)
print(d)

# json schema file for validation outside of pydantic
with open('line.pmad.json.schema', 'w') as out_file:
    out_file.write(json.dumps(line.model_json_schema(), sort_keys = True, indent = 4))


# yaml!
#   export
with open('line.pmad.yaml', 'w') as out_file:
    yaml.dump(line.model_dump(exclude_none=True), out_file)

#   import
def read_yaml(file_path: str) -> dict:
    with open(file_path, 'r') as stream:
        config = yaml.safe_load(stream)
    
    return Line(**config).model_dump()
read_yaml_dict = read_yaml('line.pmad.yaml')

read_yaml_model = Line(**read_yaml_dict)
print(read_yaml_model)


# toml! (looks surprisingly ugly -.-)
#   export
with open('line.pmad.toml', 'w') as out_file:
    toml.dump(line.model_dump(exclude_none=True), out_file)

#   import
with open('line.pmad.toml', 'r') as in_file:
    read_toml_dict = toml.load(in_file)

read_toml_model = Line(**read_toml_dict)
print(read_toml_model)

# XML: https://github.com/martinblech/xmltodict
