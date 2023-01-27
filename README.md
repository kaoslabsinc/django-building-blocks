# Django Building Blocks

Abstract Django base models to act as building blocks for rapid development of Django database models

```bash
pip install django-building-blocks
```

Documentation: [https://django-building-blocks.readthedocs.io/]()

## Development and Testing

Version numbers follow [Semantic Versioning 2.0.0](https://semver.org/)

Note: Releases with major version zero (`0.y.z`) are in experimental public API. There is no guarantee of API
compatibility between `0.y.z` and `0.b.c` where `y != z`. You may expect the public API to be backwards compatible
between `0.y.z` and `0.y.c` where `c >= z`.

### IDE Setup

Add the `example` directory to the `PYTHONPATH` in your IDE to avoid seeing import warnings in the `tests` modules. If
you are using PyCharm, this is already set up.

### Running the Tests

Install requirements

```
pip install -r requirements.txt
```

For local environment

```
pytest
```

For all supported environments

```
tox
```
