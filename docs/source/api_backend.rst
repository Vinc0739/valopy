About the Valorant API
======================

ValoPy is built as an async Python wrapper for the `unofficial-valorant-api <https://github.com/Henrik-3/unofficial-valorant-api>`_ 
developed by `Henrik-3 <https://github.com/Henrik-3>`_. This is an unofficial API that interacts with Valorant's in-game API.

API Overview
============

**Version:** 4.3.0

**Repository:** https://github.com/Henrik-3/unofficial-valorant-api

**Documentation:** https://docs.henrikdev.xyz

**Discord:** https://discord.gg/X3GaVkX2YN

**API Status:** https://status.henrikdev.xyz

What You Can Do
===============

The unofficial-valorant-api provides access to:

- Player account information
- Match history and statistics
- Store information (cosmetics, pricing)
- Competitive rank data
- Content information (maps, agents, weapons)
- And much more!

ValoPy wraps all of these features with:

- ✅ Full async/await support
- ✅ Type hints for better IDE support
- ✅ Easy-to-use Pythonic interface
- ✅ Automatic error handling

Authentication & Rate Limits
============================

The API uses a **key-based authentication system**. You need to obtain an API key from the official Discord server.

Rate limits depend on your API key tier:

**Basic Key:**
   - 30 requests per minute
   - Suitable for: Educational purposes, private Discord bots, learning
   - Instant generation

**Advanced Key:**
   - 90 requests per minute
   - Suitable for: Public Discord bots, public websites
   - Approval within 24-48 hours

**Production Key:**
   - Custom rate limit (negotiate with API author)
   - Suitable for: Large applications with significant user bases
   - Requires valid justification and potentially a Patreon subscription (Level 4/5)

For more information on custom rate limits and project support, visit:
https://www.patreon.com/henrikdev

Important Usage Guidelines
===========================

Before using this API, please ensure:

1. **User Consent**: Users must give explicit consent for their data to be collected and used
2. **Prohibited Uses**:
   
   - Large analytic projects without RSO (Riot Sign-On) authorization - data privacy concerns
   - Public store checkers - high risk of credential leaks
   - Any use case that violates Riot Games' terms

3. **Respect Rate Limits**: Don't exceed your tier's rate limits to keep the API available for everyone

Legal Notice
============

This API is **not endorsed by Riot Games** and does not reflect the views or opinions of Riot Games or anyone officially involved in producing or managing Riot Games properties.

Riot Games and all associated properties are trademarks or registered trademarks of Riot Games, Inc.

ValoPy is also an unofficial wrapper and is not affiliated with or endorsed by Riot Games.

Credits
=======

Special thanks to:

- **Henrik-3** - Creator and maintainer of the unofficial-valorant-api
- **Contributors:** @liamcottle, @RumbleMike, @Hamper
- **valorant-api.com** - For game imagery and assets

Support
=======

For API issues, questions, or support:

**HenrikDev Discord:** https://discord.gg/X3GaVkX2YN

**Contact:** contact@henrikdev.xyz or @henrik3 on Discord

Additional Resources
====================

- **API Endpoint Documentation:** https://docs.henrikdev.xyz/valorant/general
- **OpenAPI Specification:** https://app.swaggerhub.com/apis-docs/Henrik-3/HenrikDev-API
- **Other Wrappers:** JavaScript, Java, C#, Go versions available on GitHub
