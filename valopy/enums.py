from enum import Enum

from .models import AccountV1, AccountV2, Content, EsportsEvent, QueueData, Status, ValoPyModel, Version, WebsiteContent


class AllowedMethod(Enum):
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


class CountryCode(str, Enum):
    """Country codes for content localization.

    Attributes
    ----------
    EN_US : str
        English (United States)
    EN_GB : str
        English (Great Britain)
    DE_DE : str
        German (Germany)
    ES_ES : str
        Spanish (Spain)
    ES_MX : str
        Spanish (Mexico)
    FR_FR : str
        French (France)
    IT_IT : str
        Italian (Italy)
    JA_JP : str
        Japanese (Japan)
    KO_KR : str
        Korean (South Korea)
    PT_BR : str
        Portuguese (Brazil)
    RU_RU : str
        Russian (Russia)
    TR_TR : str
        Turkish (Turkey)
    VI_VN : str
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
    INTERNATIONAL : str
        International region
    NORTH_AMERICA : str
        North America
    EMEA : str
        Europe, Middle East, and Africa
    BRAZIL : str
        Brazil
    JAPAN : str
        Japan
    KOREA : str
        Korea
    LATIN_AMERICA : str
        Latin America
    LATIN_AMERICA_SOUTH : str
        Latin America South
    LATIN_AMERICA_NORTH : str
        Latin America North
    SOUTHEAST_ASIA : str
        Southeast Asia
    VIETNAM : str
        Vietnam
    OCEANIA : str
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
    VCT_AMERICAS : str
        VCT Americas
    CHALLENGERS_NA : str
        Challengers North America
    GAME_CHANGERS_NA : str
        Game Changers North America
    VCT_EMEA : str
        VCT EMEA
    VCT_PACIFIC : str
        VCT Pacific
    CHALLENGERS_BR : str
        Challengers Brazil
    CHALLENGERS_JPN : str
        Challengers Japan
    CHALLENGERS_KR : str
        Challengers Korea
    CHALLENGERS_LATAM : str
        Challengers Latin America
    CHALLENGERS_LATAM_N : str
        Challengers Latin America North
    CHALLENGERS_LATAM_S : str
        Challengers Latin America South
    CHALLENGERS_APAC : str
        Challengers APAC
    CHALLENGERS_SEA_ID : str
        Challengers SEA Indonesia
    CHALLENGERS_SEA_PH : str
        Challengers SEA Philippines
    CHALLENGERS_SEA_SG_AND_MY : str
        Challengers SEA Singapore and Malaysia
    CHALLENGERS_SEA_TH : str
        Challengers SEA Thailand
    CHALLENGERS_SEA_HK_AND_TW : str
        Challengers SEA Hong Kong and Taiwan
    CHALLENGERS_SEA_VN : str
        Challengers SEA Vietnam
    VALORANT_OCEANIA_TOUR : str
        Valorant Oceania Tour
    CHALLENGERS_SOUTH_ASIA : str
        Challengers South Asia
    GAME_CHANGERS_SEA : str
        Game Changers SEA
    GAME_CHANGERS_SERIES_BRAZIL : str
        Game Changers Series Brazil
    GAME_CHANGERS_EAST_ASIA : str
        Game Changers East Asia
    GAME_CHANGERS_EMEA : str
        Game Changers EMEA
    GAME_CHANGERS_JPN : str
        Game Changers Japan
    GAME_CHANGERS_KR : str
        Game Changers Korea
    GAME_CHANGERS_LATAM : str
        Game Changers Latin America
    GAME_CHANGERS_CHAMPIONSHIP : str
        Game Changers Championship
    MASTERS : str
        Masters
    LAST_CHANCE_QUALIFIER_APAC : str
        Last Chance Qualifier APAC
    LAST_CHANCE_QUALIFIER_EAST_ASIA : str
        Last Chance Qualifier East Asia
    LAST_CHANCE_QUALIFIER_EMEA : str
        Last Chance Qualifier EMEA
    LAST_CHANCE_QUALIFIER_NA : str
        Last Chance Qualifier North America
    LAST_CHANCE_QUALIFIER_BR_AND_LATAM : str
        Last Chance Qualifier Brazil and Latin America
    VCT_LOCK_IN : str
        VCT Lock In
    CHAMPIONS : str
        Champions
    VRL_SPAIN : str
        VRL Spain
    VRL_NORTHERN_EUROPE : str
        VRL Northern Europe
    VRL_DACH : str
        VRL DACH
    VRL_FRANCE : str
        VRL France
    VRL_EAST : str
        VRL East
    VRL_TURKEY : str
        VRL Turkey
    VRL_CIS : str
        VRL CIS
    MENA_RESILIENCE : str
        MENA Resilience
    CHALLENGERS_ITALY : str
        Challengers Italy
    CHALLENGERS_PORTUGAL : str
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
    url : str
        The URL path of the endpoint with placeholders for formatting.
    model_class : type[ValoPyModel]
        The dataclass model associated with the endpoint for response deserialization.
    """

    def __init__(self, url: str, model_class: type[ValoPyModel]) -> None:
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
