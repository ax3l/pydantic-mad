# Pydantic <3 MAD

The PMAD (Pydantic <3 MAD) project explores a new, portable data schema for accelerator beamlines:
It modernizes user input and serialization of the universally beloved definitions of [MAD-X](https://mad.web.cern.ch/mad/webguide/manual.html#Pt2) beamline elements (and more).

To define a schema, [Pydantic](https://docs.pydantic.dev) is used to serialize data classes to/from many modern file formats and to automatically validate expected attributes (the schema).
Various modern file formats (e.g., JSON, TOML, XML, ...) are supported, which makes implementation in any modern programming language easy (e.g., Python, Julia, LUA, C++, Javascript, ...).

## Status

This project is a draft, designed for discussion of a potential accelerator beamline standard that simplifies generating, parsing and exchange of accelerator beamline descriptions.


## Motivation

There are many ways to describe beamlines out there, MAD-X, Elegant, SXF, IMPACT, ...
All of them coupled to a *specific* code, most of them with a very custom syntax, non-unified conventions for units, and mixed with additional descriptions.
Especially the custom syntax of many formats makes it pretty hard to implement in a feature-complete way to exchange complex beamlines in the community.

Let's change this.
let's speak about concepts and implement a schema that is file agnostic and can be human-written, human-read, automatically be validated and is easily implemented in multiple programming languages. 
Let's use the element descriptions we love and do not spend time anymore on parsing differences between code conventions.

This will enable us to:
- exchange lattices between codes
- use common GUIs for defining lattices
- use common lattice visualization tools (2D, 3D, etc.)

### FAQ

*But don't we have MAD-X files?*  
Well, while a powerful input language for its time... have you tried implementing a MAD-X reader for a complex accelerator lattice recently?
[We have](https://github.com/ECP-WarpX/impactx/issues/104).
[Here is the reference implementation for the very custom syntax parser in C.](https://github.com/MethodicalAcceleratorDesign/MAD-X/blob/master/src/mad_parse.c)
Pretty custom, so you have to write a new parser for Python, Fortran, Julia, ... and then you still need to validate the actual content.

*What do you mean with "feature-complete"?*  
MAD-X' (and other codes') powerful input supports more than defining beamline elements, lines, sequences, etc.
It supports a custom syntax for limited scripting (e.g., loops, indirections), beam descriptions, code-specific inputs, etc.
That is good for a single code, but cumbersome for exchanging structural data on a beamline itself.
That scripting language is often used to describe complex beamlines.
Implementing a parser for a custom syntax is significant work, which can be fully avoided by using widely-used schemas.
Modern validators of schemas are readily available to the programmer of today, across a variety of programming languages.


## Roadmap

Preliminary roadmap:

1. Define the schema, using Pydantic  
1.1. core features: elements, loops?, references?, MAD-X optic-file like workflows & operations, delayed evaluation of variables for segments?
2. Document well
3. Reference implementation in Python  
3.1. attract additional reference implementations in other languages.
4. Add supporting helpers, which can import existing MAD-X, Elegant, SXF files.  
4.1. Try to be pretty feature complete in these importers (yeah, hard).
5. Implement readers for *PMAD* in active community codes for beamline modeling.
   Reuse the reference implementations.


## Examples

### YAML

```yaml
line:
- ds: 1.0
  element: drift
  nslice: 1
- ds: 0.5
  element: sbend
  nslice: 1
  rc: 5.0
- ds: 0.0
  element: marker
  name: midpoint
- line:
  - ds: 1.0
    element: drift
    nslice: 1
  - ds: 0.0
    element: marker
    name: otherpoint
  - ds: 0.5
    element: sbend
    name: special-bend
    nslice: 1
    rc: 5.0
  - ds: 0.5
    element: sbend
    nslice: 1
    rc: 5.0
```

### JSON

```json
{
    "line": [
        {
            "ds": 1.0,
            "element": "drift",
            "nslice": 1
        },
        {
            "ds": 0.5,
            "element": "sbend",
            "nslice": 1,
            "rc": 5.0
        },
        {
            "ds": 0.0,
            "element": "marker",
            "name": "midpoint"
        },
        {
            "line": [
                {
                    "ds": 1.0,
                    "element": "drift",
                    "nslice": 1
                },
                {
                    "ds": 0.0,
                    "element": "marker",
                    "name": "otherpoint"
                },
                {
                    "ds": 0.5,
                    "element": "sbend",
                    "name": "special-bend",
                    "nslice": 1,
                    "rc": 5.0
                },
                {
                    "ds": 0.5,
                    "element": "sbend",
                    "nslice": 1,
                    "rc": 5.0
                }
            ]
        }
    ]
}
```

### Python Dictionary

```py
{
    "line": [
        {
            "ds": 1.0,
            "element": "drift",
            "nslice": 1
        },
        {
            "ds": 0.5,
            "element": "sbend",
            "nslice": 1,
            "rc": 5.0
        },
        {
            "ds": 0.0,
            "element": "marker",
            "name": "midpoint"
        },
        {
            "line": [
                {
                    "ds": 1.0,
                    "element": "drift",
                    "nslice": 1
                },
                {
                    "ds": 0.0,
                    "element": "marker",
                    "name": "otherpoint"
                },
                {
                    "ds": 0.5,
                    "element": "sbend",
                    "name": "special-bend",
                    "nslice": 1,
                    "rc": 5.0
                },
                {
                    "ds": 0.5,
                    "element": "sbend",
                    "nslice": 1,
                    "rc": 5.0
                }
            ]
        }
    ]
}
```

### Python Dataclass Objects

```py
line=[
    Drift(name=None, ds=1.0, nslice=1, element='drift'),
    SBend(name=None, ds=0.5, nslice=1, element='sbend', rc=5.0),
    Marker(name='midpoint', ds=0.0, element='marker'),
    Line(line=[
        Drift(name=None, ds=1.0, nslice=1, element='drift'),
        Marker(name='otherpoint', ds=0.0, element='marker'),
        SBend(name='special-bend', ds=0.5, nslice=1, element='sbend', rc=5.0),
        SBend(name=None, ds=0.5, nslice=1, element='sbend', rc=5.0)
    ])
]
```
