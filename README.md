<div align="center">
    
  # ValoPy
  An async Python wrapper for the unofficial Valorant API.
  
  <!-- Markdown Badges -->
  <img src="https://m3-markdown-badges.vercel.app/stars/8/2/Vinc0739/valopy">
  <img src="https://ziadoua.github.io/m3-Markdown-Badges/badges/LicenceMIT/licencemit3.svg">
  <img src="https://m3-markdown-badges.vercel.app/issues/1/1/Vinc0739/valopy">
  <p></p>

  <!-- Library Badges -->
  <!-- Python Version -->
  <img src="https://img.shields.io/badge/python-3.11--3.14-blue.svg?style=for-the-badge&logo=python&color=FFD43B&logoColor=FFFFFF">
  <!-- PyPi Version -->
  <img src="https://img.shields.io/pypi/v/valopy?style=for-the-badge&logo=pypi&color=4B8BBE&logoColor=FFFFFF">
  <!-- PyPi Downloads -->
  <img src="https://img.shields.io/pypi/dm/valopy?style=for-the-badge&logo=pypi&color=FFD43B&logoColor=FFFFFF">

  <!-- Tests -->
  <img src="https://img.shields.io/github/actions/workflow/status/Vinc0739/valopy/jobs.yml?label=Tests&style=for-the-badge&logo=github&color=4B8BBE&logoColor=FFFFFF">

</div>

---

## About

ValoPy is an async Python wrapper designed specifically for the **[Unofficial Valorant API](https://github.com/Henrik-3/unofficial-valorant-api)** created by **[Henrik-3](https://github.com/Henrik-3)**.

Before using this wrapper, you'll need to:
1. Create an API Key from the **[API Dashboard](https://api.henrikdev.xyz/dashboard)**
2. Read the *Before using this API* from the API Github Repository

For help with the API itself, visit the **[Discord Server](https://discord.com/invite/X3GaVkX2YN)** or check the **[API Status](https://status.henrikdev.xyz)**.

## Key Features

- 🚀 Simple async/await interface powered by asyncio
- 📦 Automatic JSON parsing for all responses
- 🔄 Built-in error handling and resilience
- 📚 Full type hints for better IDE support

## Installation

**ValoPy** is compatible **Python 3.11+**.

*This library is in active development and is currently in beta. **Breaking changes will occur** until version 1.0.0 is released. Please pin your dependency to a specific version to avoid unexpected breaking changes.*

```bash
pip install valopy
```

### Optional Dependencies

```bash
# Development (testing, linting, type checking)
pip install valopy[dev]

# Documentation (Sphinx and related tools)
pip install valopy[docs]

```

# Quick Start

```python
import asyncio

from valopy import Client


async def get_account_info():
    async with Client(api_key="your-api-key") as client:
        # Fetch account information
        account = await client.get_account_v1("PlayerName", "TAG")

        print(f"Player: {account.name}#{account.tag}")
        print(f"PUUID: {account.puuid}")
        print(f"Region: {account.region}")
        print(f"Level: {account.account_level}")
        print(f"Last Update: {account.last_update}")


asyncio.run(get_account_info())
```


For additional examples and use cases, check out the:
- **[/examples](/examples)** directory with complete examples
- **[Documentation](https://valopy.readthedocs.io/en/latest/examples/index.html)** with more details

## Links

### ValoPy
- [Documentation](https://valopy.readthedocs.io)
- [PyPI](https://pypi.org/project/valopy)
- [Issues](https://github.com/Vinc0739/valopy/issues)
- [Discussions](https://github.com/Vinc0739/valopy/discussions)

### Unofficial Valorant API
- [Repository](https://github.com/Henrik-3/unofficial-valorant-api)
- [Dashboard](https://api.henrikdev.xyz/dashboard)
- [Documentation](https://docs.henrikdev.xyz)
- [Status](https://status.henrikdev.xyz)
- [Discord](https://discord.com/invite/X3GaVkX2YN)

---

> ValoPy is an unofficial wrapper. It is **not affiliated with or endorsed by Riot Games**. Use at your own risk and ensure compliance with the unofficial Valorant API's terms of service.
