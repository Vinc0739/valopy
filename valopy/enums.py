from enum import Enum


class AllowedMethods(Enum):
    """Allowed HTTP methods.

    Members
    -------
    GET : str
        HTTP GET method.
    POST : str
        HTTP POST method.
    """

    GET = "GET"
    POST = "POST"


class Locale(str, Enum):
    """Supported locale codes for internationalization.

    Members
    -------
    AR_AE : str
        Arabic (United Arab Emirates)
    DE_DE : str
        German (Germany)
    EN_GB : str
        English (Great Britain)
    EN_US : str
        English (United States)
    ES_ES : str
        Spanish (Spain)
    ES_MX : str
        Spanish (Mexico)
    FR_FR : str
        French (France)
    ID_ID : str
        Indonesian (Indonesia)
    IT_IT : str
        Italian (Italy)
    JA_JP : str
        Japanese (Japan)
    KO_KR : str
        Korean (South Korea)
    PL_PL : str
        Polish (Poland)
    PT_BR : str
        Portuguese (Brazil)
    RU_RU : str
        Russian (Russia)
    TH_TH : str
        Thai (Thailand)
    TR_TR : str
        Turkish (Turkey)
    VI_VN : str
        Vietnamese (Vietnam)
    ZH_CN : str
        Chinese Simplified (China)
    ZH_TW : str
        Chinese Traditional (Taiwan)
    """

    AR_AE = "ar-AE"
    DE_DE = "de-DE"
    EN_GB = "en-GB"
    EN_US = "en-US"
    ES_ES = "es-ES"
    ES_MX = "es-MX"
    FR_FR = "fr-FR"
    ID_ID = "id-ID"
    IT_IT = "it-IT"
    JA_JP = "ja-JP"
    KO_KR = "ko-KR"
    PL_PL = "pl-PL"
    PT_BR = "pt-BR"
    RU_RU = "ru-RU"
    TH_TH = "th-TH"
    TR_TR = "tr-TR"
    VI_VN = "vi-VN"
    ZH_CN = "zh-CN"
    ZH_TW = "zh-TW"


class Region(str, Enum):
    """Available regions.

    Members
    -------
    EU : str
        Europe
    NA : str
        North America
    LATAM : str
        Latin America
    BR : str
        Brazil
    AP : str
        Asia Pacific
    KR : str
        Korea
    """

    EU = "eu"
    NA = "na"
    LATAM = "latam"
    BR = "br"
    AP = "ap"
    KR = "kr"


class Platform(str, Enum):
    """Available platforms.

    Members
    -------
    PC : str
        Personal Computer
    CONSOLE : str
        Console
    """

    PC = "pc"
    CONSOLE = "console"


class Season(str, Enum):
    """Available Valorant seasons.

    Members
    -------
    E1A1 : str
        Episode 1 Act 1
    E1A2 : str
        Episode 1 Act 2
    E1A3 : str
        Episode 1 Act 3

    (and more through E9A3)
    """

    E1A1 = "e1a1"
    E1A2 = "e1a2"
    E1A3 = "e1a3"
    E2A1 = "e2a1"
    E2A2 = "e2a2"
    E2A3 = "e2a3"
    E3A1 = "e3a1"
    E3A2 = "e3a2"
    E3A3 = "e3a3"
    E4A1 = "e4a1"
    E4A2 = "e4a2"
    E4A3 = "e4a3"
    E5A1 = "e5a1"
    E5A2 = "e5a2"
    E5A3 = "e5a3"
    E6A1 = "e6a1"
    E6A2 = "e6a2"
    E6A3 = "e6a3"
    E7A1 = "e7a1"
    E7A2 = "e7a2"
    E7A3 = "e7a3"
    E8A1 = "e8a1"
    E8A2 = "e8a2"
    E8A3 = "e8a3"
    E9A1 = "e9a1"
    E9A2 = "e9a2"
    E9A3 = "e9a3"


class GameMode(str, Enum):
    """Available game modes.

    Members
    -------
    COMPETITIVE : str
        Ranked competitive mode
    UNRATED : str
        Unrated practice mode
    SPIKERUSH : str
        Spike Rush mode
    DEATHMATCH : str
        Deathmatch mode
    ESCALATION : str
        Escalation mode
    REPLICATION : str
        Replication mode
    SNOWBALL : str
        Snowball mode
    CUSTOM : str
        Custom game
    SWIFTPLAY : str
        Swift Play mode
    PREMIER : str
        Premier mode
    """

    COMPETITIVE = "competitive"
    UNRATED = "unrated"
    SPIKERUSH = "spikerush"
    DEATHMATCH = "deathmatch"
    ESCALATION = "escalation"
    REPLICATION = "replication"
    SNOWBALL = "snowball"
    CUSTOM = "custom"
    SWIFTPLAY = "swiftplay"
    PREMIER = "premier"


class HttpStatus(int, Enum):
    """HTTP status codes.

    Members
    -------
    OK : int
        200 OK
    BAD_REQUEST : int
        400 Bad Request
    FORBIDDEN : int
        403 Forbidden
    NOT_FOUND : int
        404 Not Found
    REQUEST_TIMEOUT : int
        408 Request Timeout
    TOO_MANY_REQUESTS : int
        429 Too Many Requests
    NOT_IMPLEMENTED : int
        501 Not Implemented
    SERVICE_UNAVAILABLE : int
        503 Service Unavailable
    """

    OK = 200
    BAD_REQUEST = 400
    FORBIDDEN = 403
    NOT_FOUND = 404
    REQUEST_TIMEOUT = 408
    TOO_MANY_REQUESTS = 429
    NOT_IMPLEMENTED = 501
    SERVICE_UNAVAILABLE = 503


class Endpoint(str, Enum):
    """API endpoints.

    Contains all available Valorant API endpoints organized by category.
    """

    # Account endpoints
    ACCOUNT_BY_NAME_V1 = "/v1/account/{name}/{tag}"
    ACCOUNT_BY_NAME_V2 = "/v2/account/{name}/{tag}"
    ACCOUNT_BY_PUUID_V1 = "/v1/by-puuid/account/{puuid}"
    ACCOUNT_BY_PUUID_V2 = "/v2/by-puuid/account/{puuid}"

    # Content endpoints
    CONTENT_V1 = "/v1/content"

    # Crosshair endpoints
    CROSSHAIR_V1 = "/v1/crosshair/generate"

    # Esports endpoints
    ESPORTS_SCHEDULE_V1 = "/v1/esports/schedule"

    # Leaderboard endpoints
    LEADERBOARD_V1 = "/v1/leaderboard/{affinity}"
    LEADERBOARD_V2 = "/v2/leaderboard/{affinity}"
    LEADERBOARD_V3 = "/v3/leaderboard/{affinity}"

    # Matchlist endpoints
    MATCHES_V3 = "/v3/matches/{region}/{name}/{tag}"
    MATCHES_V4 = "/v4/matches/{region}/{platform}/{name}/{tag}"
    MATCHES_BY_PUUID_V3 = "/v3/by-puuid/matches/{region}/{puuid}"
    MATCHES_BY_PUUID_V4 = "/v4/by-puuid/matches/{region}/{platform}/{puuid}"

    # Match endpoints
    MATCH_V2 = "/v2/match/{matchid}"
    MATCH_V4 = "/v4/match/{region}/{matchid}"

    # MMR History endpoints
    MMR_HISTORY_V1 = "/v1/mmr-history/{region}/{name}/{tag}"
    MMR_HISTORY_BY_PUUID_V1 = "/v1/by-puuid/mmr-history/{region}/{puuid}"
    MMR_HISTORY_BY_PUUID_V2 = "/v2/by-puuid/mmr-history/{region}/{platform}/{puuid}"

    # MMR endpoints
    MMR_V2 = "/v2/mmr/{region}/{name}/{tag}"
    MMR_V3 = "/v3/mmr/{region}/{platform}/{name}/{tag}"
    MMR_BY_PUUID_V2 = "/v2/by-puuid/mmr/{region}/{puuid}"
    MMR_BY_PUUID_V3 = "/v3/by-puuid/mmr/{region}/{platform}/{puuid}"

    # Premier endpoints
    PREMIER_TEAM = "/v1/premier/{team_id}"
    PREMIER_TEAM_HISTORY = "/v1/premier/{team_id}/history"
    PREMIER_CONFERENCE_LEADERBOARD = "/v1/premier/conferences/{affinity}/{conference}"
    PREMIER_SEARCH = "/v1/premier/search"

    # Queue Status endpoints
    QUEUE_STATUS_V1 = "/v1/queue-status/{affinity}"

    # Raw endpoints
    RAW_MATCH_V1 = "/v1/raw"

    # Status endpoints
    STATUS_V1 = "/v1/status/{region}"

    # Stored Data endpoints
    STORED_MATCHES_V1 = "/v1/stored-matches/{affinity}"
    STORED_MMR_HISTORY_V1 = "/v1/stored-mmr-history/{affinity}"

    # Store endpoints
    STORE_OFFERS_V1 = "/v1/store-offers"
    STORE_OFFERS_V2 = "/v2/store-offers"

    # Version endpoints
    VERSION_V1 = "/v1/version/{region}"

    # Website endpoints
    WEBSITE_V1 = "/v1/website/{countrycode}"
