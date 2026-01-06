from enum import Enum
from typing import Type

from .models import (
    AccountV1,
    AccountV2,
    Content,
    EsportsEvent,
    Leaderboard,
    QueueData,
    Status,
    ValoPyModel,
    Version,
    WebsiteContent,
)


class AllowedMethod(Enum):
    """Allowed HTTP methods.

    Members
    -------
    GET : :class:`str`
        HTTP GET method.
    POST : :class:`str`
        HTTP POST method.
    """

    GET = "GET"
    POST = "POST"


class Locale(str, Enum):
    """Supported locale codes for internationalization.

    Members
    -------
    AR_AE : :class:`str`
        Arabic (United Arab Emirates)
    DE_DE : :class:`str`
        German (Germany)
    EN_GB : :class:`str`
        English (Great Britain)
    EN_US : :class:`str`
        English (United States)
    ES_ES : :class:`str`
        Spanish (Spain)
    ES_MX : :class:`str`
        Spanish (Mexico)
    FR_FR : :class:`str`
        French (France)
    ID_ID : :class:`str`
        Indonesian (Indonesia)
    IT_IT : :class:`str`
        Italian (Italy)
    JA_JP : :class:`str`
        Japanese (Japan)
    KO_KR : :class:`str`
        Korean (South Korea)
    PL_PL : :class:`str`
        Polish (Poland)
    PT_BR : :class:`str`
        Portuguese (Brazil)
    RU_RU : :class:`str`
        Russian (Russia)
    TH_TH : :class:`str`
        Thai (Thailand)
    TR_TR : :class:`str`
        Turkish (Turkey)
    VI_VN : :class:`str`
        Vietnamese (Vietnam)
    ZH_CN : :class:`str`
        Chinese Simplified (China)
    ZH_TW : :class:`str`
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
    EU : :class:`str`
        Europe
    NA : :class:`str`
        North America
    LATAM : :class:`str`
        Latin America
    BR : :class:`str`
        Brazil
    AP : :class:`str`
        Asia Pacific
    KR : :class:`str`
        Korea
    """

    EU = "eu"
    NA = "na"
    LATAM = "latam"
    BR = "br"
    AP = "ap"
    KR = "kr"


class Platform(str, Enum):
    """Supported Valorant platforms.

    Members
    -------
    PC : :class:`str`
        Personal Computer (PC)
    CONSOLE : :class:`str`
        Console
    """

    PC = "pc"
    CONSOLE = "console"


class Season(str, Enum):
    """Valorant competitive seasons.

    Episode 10 (Season 2025) is separated into 6 acts for 2025.
    This will likely continue for future seasons.

    Members
    -------
    E1A1 : :class:`str`
        Episode 1 Act 1
    E1A2 : :class:`str`
        Episode 1 Act 2
    E1A3 : :class:`str`
        Episode 1 Act 3
    E2A1 : :class:`str`
        Episode 2 Act 1
    E2A2 : :class:`str`
        Episode 2 Act 2
    E2A3 : :class:`str`
        Episode 2 Act 3
    E3A1 : :class:`str`
        Episode 3 Act 1
    E3A2 : :class:`str`
        Episode 3 Act 2
    E3A3 : :class:`str`
        Episode 3 Act 3
    E4A1 : :class:`str`
        Episode 4 Act 1
    E4A2 : :class:`str`
        Episode 4 Act 2
    E4A3 : :class:`str`
        Episode 4 Act 3
    E5A1 : :class:`str`
        Episode 5 Act 1
    E5A2 : :class:`str`
        Episode 5 Act 2
    E5A3 : :class:`str`
        Episode 5 Act 3
    E6A1 : :class:`str`
        Episode 6 Act 1
    E6A2 : :class:`str`
        Episode 6 Act 2
    E6A3 : :class:`str`
        Episode 6 Act 3
    E7A1 : :class:`str`
        Episode 7 Act 1
    E7A2 : :class:`str`
        Episode 7 Act 2
    E7A3 : :class:`str`
        Episode 7 Act 3
    E8A1 : :class:`str`
        Episode 8 Act 1
    E8A2 : :class:`str`
        Episode 8 Act 2
    E8A3 : :class:`str`
        Episode 8 Act 3
    E9A1 : :class:`str`
        Episode 9 Act 1
    E9A2 : :class:`str`
        Episode 9 Act 2
    E9A3 : :class:`str`
        Episode 9 Act 3
    E10A1 : :class:`str`
        Episode 10 Act 1
    E10A2 : :class:`str`
        Episode 10 Act 2
    E10A3 : :class:`str`
        Episode 10 Act 3
    E10A4 : :class:`str`
        Episode 10 Act 4
    E10A5 : :class:`str`
        Episode 10 Act 5
    E10A6 : :class:`str`
        Episode 10 Act 6
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
    E10A1 = "e10a1"
    E10A2 = "e10a2"
    E10A3 = "e10a3"
    E10A4 = "e10a4"
    E10A5 = "e10a5"
    E10A6 = "e10a6"


class CountryCode(str, Enum):
    """Country codes for content localization.

    Attributes
    ----------
    EN_US : :class:`str`
        English (United States)
    EN_GB : :class:`str`
        English (Great Britain)
    DE_DE : :class:`str`
        German (Germany)
    ES_ES : :class:`str`
        Spanish (Spain)
    ES_MX : :class:`str`
        Spanish (Mexico)
    FR_FR : :class:`str`
        French (France)
    IT_IT : :class:`str`
        Italian (Italy)
    JA_JP : :class:`str`
        Japanese (Japan)
    KO_KR : :class:`str`
        Korean (South Korea)
    PT_BR : :class:`str`
        Portuguese (Brazil)
    RU_RU : :class:`str`
        Russian (Russia)
    TR_TR : :class:`str`
        Turkish (Turkey)
    VI_VN : :class:`str`
        Vietnamese (Vietnam)
    """

    EN_US = "en-us"
    EN_GB = "en-gb"
    DE_DE = "de-de"
    ES_ES = "es-es"
    ES_MX = "es-mx"
    FR_FR = "fr-fr"
    IT_IT = "it-it"
    JA_JP = "ja-jp"
    KO_KR = "ko-kr"
    PT_BR = "pt-br"
    RU_RU = "ru-ru"
    TR_TR = "tr-tr"
    VI_VN = "vi-vn"


class EsportsRegion(str, Enum):
    """Esports event regions.

    Members
    -------
    INTERNATIONAL : :class:`str`
        International region
    NORTH_AMERICA : :class:`str`
        North America
    EMEA : :class:`str`
        Europe, Middle East, and Africa
    BRAZIL : :class:`str`
        Brazil
    JAPAN : :class:`str`
        Japan
    KOREA : :class:`str`
        Korea
    LATIN_AMERICA : :class:`str`
        Latin America
    LATIN_AMERICA_SOUTH : :class:`str`
        Latin America South
    LATIN_AMERICA_NORTH : :class:`str`
        Latin America North
    SOUTHEAST_ASIA : :class:`str`
        Southeast Asia
    VIETNAM : :class:`str`
        Vietnam
    OCEANIA : :class:`str`
        Oceania
    """

    INTERNATIONAL = "international"
    NORTH_AMERICA = "north_america"
    EMEA = "emea"
    BRAZIL = "brazil"
    JAPAN = "japan"
    KOREA = "korea"
    LATIN_AMERICA = "latin_america"
    LATIN_AMERICA_SOUTH = "latin_america_south"
    LATIN_AMERICA_NORTH = "latin_america_north"
    SOUTHEAST_ASIA = "southeast_asia"
    VIETNAM = "vietnam"
    OCEANIA = "oceania"


class League(str, Enum):
    """Esports leagues.

    Members
    -------
    VCT_AMERICAS : :class:`str`
        VCT Americas
    CHALLENGERS_NA : :class:`str`
        Challengers North America
    GAME_CHANGERS_NA : :class:`str`
        Game Changers North America
    VCT_EMEA : :class:`str`
        VCT EMEA
    VCT_PACIFIC : :class:`str`
        VCT Pacific
    CHALLENGERS_BR : :class:`str`
        Challengers Brazil
    CHALLENGERS_JPN : :class:`str`
        Challengers Japan
    CHALLENGERS_KR : :class:`str`
        Challengers Korea
    CHALLENGERS_LATAM : :class:`str`
        Challengers Latin America
    CHALLENGERS_LATAM_N : :class:`str`
        Challengers Latin America North
    CHALLENGERS_LATAM_S : :class:`str`
        Challengers Latin America South
    CHALLENGERS_APAC : :class:`str`
        Challengers APAC
    CHALLENGERS_SEA_ID : :class:`str`
        Challengers SEA Indonesia
    CHALLENGERS_SEA_PH : :class:`str`
        Challengers SEA Philippines
    CHALLENGERS_SEA_SG_AND_MY : :class:`str`
        Challengers SEA Singapore and Malaysia
    CHALLENGERS_SEA_TH : :class:`str`
        Challengers SEA Thailand
    CHALLENGERS_SEA_HK_AND_TW : :class:`str`
        Challengers SEA Hong Kong and Taiwan
    CHALLENGERS_SEA_VN : :class:`str`
        Challengers SEA Vietnam
    VALORANT_OCEANIA_TOUR : :class:`str`
        Valorant Oceania Tour
    CHALLENGERS_SOUTH_ASIA : :class:`str`
        Challengers South Asia
    GAME_CHANGERS_SEA : :class:`str`
        Game Changers SEA
    GAME_CHANGERS_SERIES_BRAZIL : :class:`str`
        Game Changers Series Brazil
    GAME_CHANGERS_EAST_ASIA : :class:`str`
        Game Changers East Asia
    GAME_CHANGERS_EMEA : :class:`str`
        Game Changers EMEA
    GAME_CHANGERS_JPN : :class:`str`
        Game Changers Japan
    GAME_CHANGERS_KR : :class:`str`
        Game Changers Korea
    GAME_CHANGERS_LATAM : :class:`str`
        Game Changers Latin America
    GAME_CHANGERS_CHAMPIONSHIP : :class:`str`
        Game Changers Championship
    MASTERS : :class:`str`
        Masters
    LAST_CHANCE_QUALIFIER_APAC : :class:`str`
        Last Chance Qualifier APAC
    LAST_CHANCE_QUALIFIER_EAST_ASIA : :class:`str`
        Last Chance Qualifier East Asia
    LAST_CHANCE_QUALIFIER_EMEA : :class:`str`
        Last Chance Qualifier EMEA
    LAST_CHANCE_QUALIFIER_NA : :class:`str`
        Last Chance Qualifier North America
    LAST_CHANCE_QUALIFIER_BR_AND_LATAM : :class:`str`
        Last Chance Qualifier Brazil and Latin America
    VCT_LOCK_IN : :class:`str`
        VCT Lock In
    CHAMPIONS : :class:`str`
        Champions
    VRL_SPAIN : :class:`str`
        VRL Spain
    VRL_NORTHERN_EUROPE : :class:`str`
        VRL Northern Europe
    VRL_DACH : :class:`str`
        VRL DACH
    VRL_FRANCE : :class:`str`
        VRL France
    VRL_EAST : :class:`str`
        VRL East
    VRL_TURKEY : :class:`str`
        VRL Turkey
    VRL_CIS : :class:`str`
        VRL CIS
    MENA_RESILIENCE : :class:`str`
        MENA Resilience
    CHALLENGERS_ITALY : :class:`str`
        Challengers Italy
    CHALLENGERS_PORTUGAL : :class:`str`
        Challengers Portugal
    """

    VCT_AMERICAS = "vct_americas"
    CHALLENGERS_NA = "challengers_na"
    GAME_CHANGERS_NA = "game_changers_na"
    VCT_EMEA = "vct_emea"
    VCT_PACIFIC = "vct_pacific"
    CHALLENGERS_BR = "challengers_br"
    CHALLENGERS_JPN = "challengers_jpn"
    CHALLENGERS_KR = "challengers_kr"
    CHALLENGERS_LATAM = "challengers_latam"
    CHALLENGERS_LATAM_N = "challengers_latam_n"
    CHALLENGERS_LATAM_S = "challengers_latam_s"
    CHALLENGERS_APAC = "challengers_apac"
    CHALLENGERS_SEA_ID = "challengers_sea_id"
    CHALLENGERS_SEA_PH = "challengers_sea_ph"
    CHALLENGERS_SEA_SG_AND_MY = "challengers_sea_sg_and_my"
    CHALLENGERS_SEA_TH = "challengers_sea_th"
    CHALLENGERS_SEA_HK_AND_TW = "challengers_sea_hk_and_tw"
    CHALLENGERS_SEA_VN = "challengers_sea_vn"
    VALORANT_OCEANIA_TOUR = "valorant_oceania_tour"
    CHALLENGERS_SOUTH_ASIA = "challengers_south_asia"
    GAME_CHANGERS_SEA = "game_changers_sea"
    GAME_CHANGERS_SERIES_BRAZIL = "game_changers_series_brazil"
    GAME_CHANGERS_EAST_ASIA = "game_changers_east_asia"
    GAME_CHANGERS_EMEA = "game_changers_emea"
    GAME_CHANGERS_JPN = "game_changers_jpn"
    GAME_CHANGERS_KR = "game_changers_kr"
    GAME_CHANGERS_LATAM = "game_changers_latam"
    GAME_CHANGERS_CHAMPIONSHIP = "game_changers_championship"
    MASTERS = "masters"
    LAST_CHANCE_QUALIFIER_APAC = "last_chance_qualifier_apac"
    LAST_CHANCE_QUALIFIER_EAST_ASIA = "last_chance_qualifier_east_asia"
    LAST_CHANCE_QUALIFIER_EMEA = "last_chance_qualifier_emea"
    LAST_CHANCE_QUALIFIER_NA = "last_chance_qualifier_na"
    LAST_CHANCE_QUALIFIER_BR_AND_LATAM = "last_chance_qualifier_br_and_latam"
    VCT_LOCK_IN = "vct_lock_in"
    CHAMPIONS = "champions"
    VRL_SPAIN = "vrl_spain"
    VRL_NORTHERN_EUROPE = "vrl_northern_europe"
    VRL_DACH = "vrl_dach"
    VRL_FRANCE = "vrl_france"
    VRL_EAST = "vrl_east"
    VRL_TURKEY = "vrl_turkey"
    VRL_CIS = "vrl_cis"
    MENA_RESILIENCE = "mena_resilience"
    CHALLENGERS_ITALY = "challengers_italy"
    CHALLENGERS_PORTUGAL = "challengers_portugal"


class Endpoint(Enum):
    """API endpoints with associated response models.

    Attributes
    ----------
    url : :class:`str`
        The URL path of the endpoint with placeholders for formatting.
    model : Type[:class:`ValoPyModel`]
        The dataclass model class associated with the endpoint for response deserialization.
    """

    def __init__(self, url: str, model_class: Type[ValoPyModel]) -> None:
        self.url = url
        self.model = model_class

    # Account endpoints
    ACCOUNT_BY_NAME_V1 = ("/v1/account/{name}/{tag}", AccountV1)
    ACCOUNT_BY_NAME_V2 = ("/v2/account/{name}/{tag}", AccountV2)
    ACCOUNT_BY_PUUID_V1 = ("/v1/by-puuid/account/{puuid}", AccountV1)
    ACCOUNT_BY_PUUID_V2 = ("/v2/by-puuid/account/{puuid}", AccountV2)

    # Content endpoint
    CONTENT_V1 = ("/v1/content", Content)

    # Version endpoint
    VERSION_V1 = ("/v1/version/{region}", Version)

    # Website endpoint
    WEBSITE = ("/v1/website/{countrycode}", WebsiteContent)

    # Status endpoint
    STATUS = ("/v1/status/{region}", Status)

    # Queue endpoint
    QUEUE_STATUS = ("/v1/queue-status/{region}", QueueData)

    # Esports endpoint
    ESPORTS_SCHEDULE = ("/v1/esports/schedule", EsportsEvent)

    # Leaderboard endpoint
    LEADERBOARD_V3 = ("/v3/leaderboard/{region}/{platform}", Leaderboard)
