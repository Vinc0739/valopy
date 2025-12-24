from dataclasses import dataclass, field
from typing import Any, Dict, List, TypeVar


@dataclass
class Result:
    """HTTP request result wrapper.

    Attributes
    ----------
    status_code : int
        The HTTP status code of the response.
    message : str
        The HTTP status message.
    data : Any
        The response data (dict or deserialized dataclass).
    """

    status_code: int
    message: str = "None"
    data: Any = field(default_factory=dict)  # either dict or deserialized dataclass of type ValoPyModel


# ======================================== Card Data ========================================


@dataclass
class CardData:
    """Player card data.

    Attributes
    ----------
    small : str
        Small card image URL.
    large : str
        Large card image URL.
    wide : str
        Wide card image URL.
    id : str
        Card ID.
    """

    small: str
    large: str
    wide: str
    id: str


# ======================================== Account ========================================


@dataclass
class AccountV1:
    """Account V1 information.

    Attributes
    ----------
    puuid : str
        The player's unique identifier.
    region : str
        The player's region.
    account_level : int
        The player's account level.
    name : str
        The player's game name.
    tag : str
        The player's tag.
    card : CardData
        The player's card data with image URLs.
    last_update : str
        Last update timestamp.
    last_update_raw : int
        Last update timestamp (raw).
    """

    puuid: str
    region: str
    account_level: int
    name: str
    tag: str
    card: CardData
    last_update: str
    last_update_raw: int


@dataclass
class AccountV2:
    """Account V2 information.

    Attributes
    ----------
    puuid : str
        The player's unique identifier.
    region : str
        The player's region.
    account_level : int
        The player's account level.
    name : str
        The player's game name.
    tag : str
        The player's tag.
    card : str
        The player's card ID.
    title : str
        The player's title.
    platforms : List[str]
        Available platforms.
    updated_at : str
        Update timestamp.
    """

    puuid: str
    region: str
    account_level: int
    name: str
    tag: str
    card: str
    title: str
    platforms: List[str]
    updated_at: str


# ======================================== Content ========================================


@dataclass
class ContentCharacter:
    """Content character structure.

    Attributes
    ----------
    name : str
        Character name.
    id : str
        Character ID.
    assetName : str
        Asset name.
    localizedNames : Dict[str, str]
        Character names in different locales.
    isPlayableCharacter : bool
        Whether character is playable.
    """

    name: str
    id: str
    assetName: str = ""
    localizedNames: Dict[str, str] = field(default_factory=dict)
    isPlayableCharacter: bool = False


@dataclass
class ContentMap:
    """Content map structure.

    Attributes
    ----------
    name : str
        Map name.
    id : str
        Map ID.
    assetName : str
        Asset name.
    assetPath : str
        Asset path.
    localizedNames : Dict[str, str]
        Map names in different locales.
    """

    name: str
    id: str
    assetName: str = ""
    assetPath: str = ""
    localizedNames: Dict[str, str] = field(default_factory=dict)


@dataclass
class ContentItem:
    """Generic content item structure.

    Attributes
    ----------
    name : str
        Item name.
    id : str
        Item ID.
    assetName : str
        Asset name.
    assetPath : str
        Asset path.
    localizedNames : Dict[str, str]
        Item names in different locales.
    """

    name: str
    id: str
    assetName: str = ""
    assetPath: str = ""
    localizedNames: Dict[str, str] = field(default_factory=dict)


@dataclass
class ContentPlayerTitle:
    """Content player title structure.

    Attributes
    ----------
    name : str
        Title name.
    id : str
        Title ID.
    assetName : str
        Asset name.
    titleText : str
        Display text for the title.
    """

    name: str
    id: str
    assetName: str = ""
    titleText: str = ""


@dataclass
class ContentAct:
    """Content act structure.

    Attributes
    ----------
    name : str
        Act name.
    id : str
        Act ID.
    localizedNames : Dict[str, str]
        Act names in different locales.
    isActive : bool
        Whether the act is currently active.
    """

    name: str
    id: str
    localizedNames: Dict[str, str] = field(default_factory=dict)
    isActive: bool = False


@dataclass
class Content:
    """In-game content data.

    Attributes
    ----------
    version : str
        Content version.
    characters : List[ContentCharacter]
        Available characters.
    maps : List[ContentMap]
        Available maps.
    chromas : List[ContentItem]
        Available chromas.
    skins : List[ContentItem]
        Available skins.
    skin_levels : List[ContentItem]
        Available skin levels.
    equips : List[ContentItem]
        Available equips.
    game_modes : List[ContentItem]
        Available game modes.
    sprays : List[ContentItem]
        Available sprays.
    spray_levels : List[ContentItem]
        Available spray levels.
    charms : List[ContentItem]
        Available charms.
    charm_levels : List[ContentItem]
        Available charm levels.
    player_cards : List[ContentItem]
        Available player cards.
    player_titles : List[ContentPlayerTitle]
        Available player titles.
    acts : List[ContentAct]
        Available acts.
    ceremonies : List[ContentItem]
        Available ceremonies.
    """

    version: str
    characters: List[ContentCharacter] = field(default_factory=list)
    maps: List[ContentMap] = field(default_factory=list)
    chromas: List[ContentItem] = field(default_factory=list)
    skins: List[ContentItem] = field(default_factory=list)
    skinLevels: List[ContentItem] = field(default_factory=list)
    equips: List[ContentItem] = field(default_factory=list)
    gameModes: List[ContentItem] = field(default_factory=list)
    sprays: List[ContentItem] = field(default_factory=list)
    sprayLevels: List[ContentItem] = field(default_factory=list)
    charms: List[ContentItem] = field(default_factory=list)
    charmLevels: List[ContentItem] = field(default_factory=list)
    playerCards: List[ContentItem] = field(default_factory=list)
    playerTitles: List[ContentPlayerTitle] = field(default_factory=list)
    acts: List[ContentAct] = field(default_factory=list)
    ceremonies: List[ContentItem] = field(default_factory=list)


# ======================================== Version ========================================


@dataclass
class Version:
    """Version response"""

    region: str
    branch: str
    build_date: str
    build_ver: str
    last_checked: str
    version: int
    version_for_api: str


# ======================================== TypeVar ========================================

ValoPyModel = TypeVar("ValoPyModel", AccountV1, AccountV2, Content, Version)
