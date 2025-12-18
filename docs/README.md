# ValoPy Documentation

This directory contains the Sphinx documentation for ValoPy.

## Building the Documentation

### Prerequisites

Install the documentation dependencies:

```bash
pip install sphinx sphinx-rtd-theme sphinx-autodoc-typehints aiohttp
```

Or if using UV:

```bash
uv sync --group docs
```

### Build HTML Documentation

To build the HTML documentation:

```bash
cd docs
make html
```

The generated documentation will be in `build/html/`. Open `build/html/index.html` in your browser to view it.

### Clean Build

To clean previous builds and rebuild from scratch:

```bash
cd docs
make clean
make html
```

### Other Formats

You can also build other formats:

- `make latexpdf` - Build PDF documentation (requires LaTeX)
- `make epub` - Build EPUB documentation
- `make man` - Build man pages

Run `make help` to see all available build targets.

## Documentation Structure

- `source/` - Documentation source files
  - `index.rst` - Main documentation page with overview and quick start
  - `examples.rst` - Comprehensive usage examples
  - `api/` - API reference documentation
    - `client.rst` - Client class documentation
    - `models.rst` - Data models documentation
    - `exceptions.rst` - Exception classes documentation
    - `enums.rst` - Enumeration types documentation
  - `conf.py` - Sphinx configuration
- `build/` - Generated documentation (not committed to git)

## Theme

The documentation uses the [Read the Docs theme](https://sphinx-rtd-theme.readthedocs.io/), which provides a clean, modern look with excellent navigation features.

## Contributing

When adding new modules or features to valopy, please update the documentation:

1. Add docstrings to your code following the NumPy/Google style
2. Update the relevant `.rst` files in `source/api/` if needed
3. Add usage examples to `examples.rst`
4. Build the docs locally to verify everything looks correct
