from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, TypeVar


@dataclass
class Result:
    """HTTP request result wrapper.

    Attributes
    ----------
    status_code : :class:`int`
        The HTTP status code of the response.
    message : :class:`str`
        The HTTP status message.
    data : :class:`Any`
        The response data (dict or deserialized dataclass).
    """

    status_code: int
    message: str = "None"
    data: Any = field(
        default_factory=dict
    )  # either dict or deserialized dataclass of type ValoPyModel


@dataclass
class ResultMetadata:
    """Pagination and results metadata.

    Attributes
    ----------
    total : :class:`int`
        Total number of results available.
    returned : :class:`int`
        Number of results returned in this response.
    before : :class:`int`
        Number of results before this page.
    after : :class:`int`
        Number of results after this page.
    """

    total: int
    returned: int
    before: int
    after: int


# ======================================== Card Data ========================================


@dataclass
class CardData:
    """Player card data.

    Attributes
    ----------
    small : :class:`str`
        Small card image URL.
    large : :class:`str`
        Large card image URL.
    wide : :class:`str`
        Wide card image URL.
    id : :class:`str`
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
    puuid : :class:`str`
        The player's unique identifier.
    region : :class:`str`
        The player's region.
    account_level : :class:`int`
        The player's account level.
    name : :class:`str`
        The player's game name.
    tag : :class:`str`
        The player's tag.
    card : :class:`CardData`
        The player's card data with image URLs.
    last_update : :class:`datetime.datetime`
        Last update timestamp. Note: This is an approximation calculated from relative time strings
        (e.g., "3 minutes ago") returned by the API, so accuracy may vary by seconds/minutes.
    last_update_raw : :class:`int`
        Last update timestamp (raw).
    """

    puuid: str
    region: str
    account_level: int
    name: str
    tag: str
    card: CardData
    last_update: datetime
    last_update_raw: int


@dataclass
class AccountV2:
    """Account V2 information.

    Attributes
    ----------
    puuid : :class:`str`
        The player's unique identifier.
    region : :class:`str`
        The player's region.
    account_level : :class:`int`
        The player's account level.
    name : :class:`str`
        The player's game name.
    tag : :class:`str`
        The player's tag.
    card : :class:`str`
        The player's card ID.
    title : :class:`str`
        The player's title.
    platforms : List[:class:`str`]
        Available platforms.
    updated_at : :class:`datetime.datetime`
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
    updated_at: datetime


# ======================================== Content ========================================


@dataclass
class ContentCharacter:
    """Content character structure.

    Attributes
    ----------
    name : :class:`str`
        Character name.
    id : :class:`str`
        Character ID.
    assetName : :class:`str`
        Asset name.
    localizedNames : Dict[:class:`str`, :class:`str`]
        Character names in different locales.
    isPlayableCharacter : :class:`bool`
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
    name : :class:`str`
        Map name.
    id : :class:`str`
        Map ID.
    assetName : :class:`str`
        Asset name.
    assetPath : :class:`str`
        Asset path.
    localizedNames : Dict[:class:`str`, :class:`str`]
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
    name : :class:`str`
        Item name.
    id : :class:`str`
        Item ID.
    assetName : :class:`str`
        Asset name.
    assetPath : :class:`str`
        Asset path.
    localizedNames : Dict[:class:`str`, :class:`str`]
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
    name : :class:`str`
        Title name.
    id : :class:`str`
        Title ID.
    assetName : :class:`str`
        Asset name.
    titleText : :class:`str`
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
    name : :class:`str`
        Act name.
    id : :class:`str`
        Act ID.
    localizedNames : Dict[:class:`str`, :class:`str`]
        Act names in different locales.
    isActive : :class:`bool`
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
    version : :class:`str`
        Content version.
    characters : List[:class:`ContentCharacter`]
        Available characters.
    maps : List[:class:`ContentMap`]
        Available maps.
    chromas : List[:class:`ContentItem`]
        Available chromas.
    skins : List[:class:`ContentItem`]
        Available skins.
    skin_levels : List[:class:`ContentItem`]
        Available skin levels.
    equips : List[:class:`ContentItem`]
        Available equips.
    game_modes : List[:class:`ContentItem`]
        Available game modes.
    sprays : List[:class:`ContentItem`]
        Available sprays.
    spray_levels : List[:class:`ContentItem`]
        Available spray levels.
    charms : List[:class:`ContentItem`]
        Available charms.
    charm_levels : List[:class:`ContentItem`]
        Available charm levels.
    player_cards : List[:class:`ContentItem`]
        Available player cards.
    player_titles : List[:class:`ContentPlayerTitle`]
        Available player titles.
    acts : List[:class:`ContentAct`]
        Available acts.
    ceremonies : List[:class:`ContentItem`]
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
    """Version response

    Attributes
    ----------
    region : :class:`str`
        The region of the version data.
    branch : :class:`str`
        The branch of the version data.
    build_date : :class:`datetime.datetime`
        The build date of the version.
    build_ver : :class:`str`
        The build version.
    last_checked : :class:`datetime.datetime`
        The last checked timestamp.
    version : :class:`int`
        The version number.
    version_for_api : :class:`str`
        The version string for API usage.
    """

    region: str
    branch: str
    build_date: datetime
    build_ver: str
    last_checked: datetime
    version: int
    version_for_api: str


# ======================================== Website ========================================


@dataclass
class WebsiteContent:
    """Website content structure.

    Attributes
    ----------
    id : :class:`str`
        The unique identifier for the website content.
    banner_url : :class:`str`
        The URL of the banner image.
    category : :class:`str`
        The category of the website content.
    date : :class:`datetime.datetime`
        Release date of the content.
    title : :class:`str`
        Title of the content.
    url : :class:`str`
        The URL of the content.
    description : :class:`str`
        Description of the content.
    external_link : :class:`str`
        External link related to the content.
    """

    id: str
    banner_url: str
    category: str
    date: datetime
    title: str
    url: str
    description: str = ""
    external_link: str = ""


# ======================================== Status ========================================


@dataclass
class StatusTranslation:
    """Translation content for status updates.

    Attributes
    ----------
    content : :class:`str`
        The translated content message.
    locale : :class:`str`
        The locale code (e.g., 'en_US').
    """

    content: str
    locale: str


@dataclass
class StatusTitle:
    """Title content for status entries.

    Attributes
    ----------
    content : :class:`str`
        The title text.
    locale : :class:`str`
        The locale code (e.g., 'en_US').
    """

    content: str
    locale: str


@dataclass
class StatusUpdate:
    """Individual status update entry.

    Attributes
    ----------
    created_at : :class:`datetime.datetime`
        When the update was created.
    updated_at : :class:`datetime.datetime`
        When the update was last modified.
    publish : :class:`bool`
        Whether the update is published.
    id : :class:`int`
        Unique identifier for the update.
    translations : List[:class:`StatusTranslation`]
        Translated content messages.
    publish_locations : List[:class:`str`]
        Where the update is published (e.g., 'riotclient').
    author : :class:`str`
        Author of the update.
    """

    created_at: datetime
    updated_at: datetime
    publish: bool
    id: int
    translations: List[StatusTranslation] = field(default_factory=list)
    publish_locations: List[str] = field(default_factory=list)
    author: str = ""


@dataclass
class StatusEntry:
    """Status entry for maintenance or incident.

    Attributes
    ----------
    created_at : :class:`datetime.datetime`
        When the entry was created.
    archive_at : :class:`datetime.datetime`
        When the entry will be archived.
    updates : List[:class:`StatusUpdate`]
        List of status updates.
    platforms : List[:class:`str`]
        Affected platforms (e.g., 'windows').
    updated_at : :class:`datetime.datetime`
        When the entry was last modified.
    id : :class:`int`
        Unique identifier for the entry.
    titles : List[:class:`StatusTitle`]
        Titles for the entry.
    maintenance_status : :class:`str`
        Current maintenance status (e.g., 'in_progress').
    incident_severity : :class:`str`
        Severity level (e.g., 'warning').
    """

    created_at: datetime
    archive_at: datetime
    updates: List[StatusUpdate] = field(default_factory=list)
    platforms: List[str] = field(default_factory=list)
    updated_at: datetime = datetime.fromisoformat("1970-01-01T00:00:00+00:00")
    id: int = 0
    titles: List[StatusTitle] = field(default_factory=list)
    maintenance_status: str = ""
    incident_severity: str = ""


@dataclass
class Status:
    """Server status response.

    Attributes
    ----------
    maintenances : List[:class:`StatusEntry`]
        List of current maintenance announcements.
    incidents : List[:class:`StatusEntry`]
        List of current incidents.
    """

    maintenances: List[StatusEntry] = field(default_factory=list)
    incidents: List[StatusEntry] = field(default_factory=list)


# ======================================== Queue ========================================


@dataclass
class QueuePartySize:
    """Party size constraints for a queue.

    Attributes
    ----------
    max : :class:`int`
        Maximum party size allowed.
    min : :class:`int`
        Minimum party size allowed.
    invalid : List[:class:`int`]
        Party sizes that are not allowed.
    full_party_bypass : :class:`bool`
        Whether full parties bypass certain restrictions.
    """

    max: int
    min: int
    invalid: List[int] = field(default_factory=list)
    full_party_bypass: bool = False


@dataclass
class QueueHighSkill:
    """High skill tier restrictions for a queue.

    Attributes
    ----------
    max_party_size : :class:`int`
        Maximum party size for high skill players.
    min_tier : :class:`int`
        Minimum tier affected by high skill restrictions.
    max_tier : :class:`int`
        Maximum tier affected by high skill restrictions.
    """

    max_party_size: int
    min_tier: int
    max_tier: int


@dataclass
class QueueSkillDisparityTier:
    """Tier information for skill disparity.

    Attributes
    ----------
    id : :class:`int`
        Tier identifier.
    name : :class:`str`
        Tier name.
    """

    id: int
    name: str


@dataclass
class QueueSkillDisparity:
    """Skill disparity restrictions for a queue.

    Attributes
    ----------
    tier : :class:`int`
        The tier identifier.
    name : :class:`str`
        Tier name.
    max_tier : :class:`QueueSkillDisparityTier`
        Maximum tier allowed to queue with this tier.
    """

    tier: int
    name: str
    max_tier: QueueSkillDisparityTier


@dataclass
class QueueGameRules:
    """Game rules configuration for a queue.

    Attributes
    ----------
    overtime_win_by_two : :class:`bool`
        Whether overtime requires winning by two.
    allow_lenient_surrender : :class:`bool`
        Whether lenient surrender is allowed.
    allow_drop_out : :class:`bool`
        Whether dropping out is allowed.
    assign_random_agents : :class:`bool`
        Whether agents are randomly assigned.
    skip_pregame : :class:`bool`
        Whether pregame is skipped.
    allow_overtime_draw_vote : :class:`bool`
        Whether overtime draw voting is allowed.
    overtime_win_by_two_capped : :class:`bool`
        Whether overtime win by two is capped.
    premier_mode : :class:`bool`
        Whether this is premier mode.
    """

    overtime_win_by_two: bool = False
    allow_lenient_surrender: bool = False
    allow_drop_out: bool = False
    assign_random_agents: bool = False
    skip_pregame: bool = False
    allow_overtime_draw_vote: bool = False
    overtime_win_by_two_capped: bool = False
    premier_mode: bool = False


@dataclass
class QueueMapInfo:
    """Map identifier and name.

    Attributes
    ----------
    id : :class:`str`
        Map UUID.
    name : :class:`str`
        Map display name.
    """

    id: str
    name: str


@dataclass
class QueueMap:
    """Map configuration for a queue.

    Attributes
    ----------
    map : :class:`QueueMapInfo`
        Map information.
    enabled : :class:`bool`
        Whether the map is enabled in this queue.
    """

    map: QueueMapInfo
    enabled: bool


@dataclass
class QueueData:
    """Individual queue configuration.

    Attributes
    ----------
    mode : :class:`str`
        Queue mode name (e.g., "Competitive").
    mode_id : :class:`str`
        Queue mode identifier (e.g., "competitive").
    enabled : :class:`bool`
        Whether the queue is currently enabled.
    team_size : :class:`int`
        Number of players per team.
    number_of_teams : :class:`int`
        Number of teams in a match.
    party_size : :class:`QueuePartySize`
        Party size constraints.
    high_skill : :class:`QueueHighSkill`
        High skill tier restrictions.
    ranked : :class:`bool`
        Whether this is a ranked queue.
    tournament : :class:`bool`
        Whether this is a tournament queue.
    skill_disparity : List[:class:`QueueSkillDisparity`]
        Skill disparity restrictions by tier.
    required_account_level : :class:`int`
        Minimum account level required.
    game_rules : :class:`QueueGameRules`
        Game rules configuration.
    platforms : List[:class:`str`]
        Available platforms (e.g., ["pc"]).
    maps : List[:class:`QueueMap`]
        Available maps in this queue.
    """

    mode: str
    mode_id: str
    enabled: bool
    team_size: int
    number_of_teams: int
    party_size: QueuePartySize
    high_skill: QueueHighSkill
    ranked: bool
    tournament: bool
    skill_disparity: List[QueueSkillDisparity]
    required_account_level: int
    game_rules: QueueGameRules
    platforms: List[str] = field(default_factory=list)
    maps: List[QueueMap] = field(default_factory=list)


# ======================================== Esports ========================================


@dataclass
class EsportsLeague:
    """Esports league information.

    Attributes
    ----------
    name : :class:`str`
        League name.
    identifier : :class:`str`
        League identifier.
    icon : :class:`str`
        League icon URL.
    region : :class:`str`
        League region.
    """

    name: str
    identifier: str
    icon: str
    region: str


@dataclass
class EsportsTournament:
    """Esports tournament information.

    Attributes
    ----------
    name : :class:`str`
        Tournament name.
    season : :class:`str`
        Tournament season.
    """

    name: str
    season: str


@dataclass
class EsportsGameType:
    """Esports game type configuration.

    Attributes
    ----------
    type : :class:`str`
        Game type (e.g., "playAll", "bestOf").
    count : :class:`int`
        Number of games.
    """

    type: str
    count: int


@dataclass
class EsportsTeamRecord:
    """Esports team record.

    Attributes
    ----------
    wins : :class:`int`
        Number of wins.
    losses : :class:`int`
        Number of losses.
    """

    wins: int
    losses: int


@dataclass
class EsportsTeam:
    """Esports team information.

    Attributes
    ----------
    name : :class:`str`
        Team name.
    code : :class:`str`
        Team code.
    icon : :class:`str`
        Team icon URL.
    has_won : :class:`bool`
        Whether the team has won.
    game_wins : :class:`int`
        Number of games won.
    record : :class:`EsportsTeamRecord`
        Team's win/loss record.
    """

    name: str
    code: str
    icon: str
    has_won: bool
    game_wins: int
    record: EsportsTeamRecord


@dataclass
class EsportsMatch:
    """Esports match information.

    Attributes
    ----------
    id : :class:`str`
        Match ID.
    game_type : :class:`EsportsGameType`
        Game type configuration.
    teams : List[:class:`EsportsTeam`]
        List of teams in the match.
    """

    id: str
    game_type: EsportsGameType
    teams: List[EsportsTeam]


@dataclass
class EsportsEvent:
    """Esports event data.

    Attributes
    ----------
    date : :class:`datetime.datetime`
        Event date (ISO 8601 format).
    state : :class:`str`
        Event state (e.g., "completed", "upcoming").
    type : :class:`str`
        Event type (e.g., "match").
    vod : :class:`str`
        Video on demand URL.
    league : :class:`EsportsLeague`
        League information.
    tournament : :class:`EsportsTournament`
        Tournament information.
    match : :class:`EsportsMatch`
        Match information.
    """

    date: datetime
    state: str
    type: str
    vod: str
    league: EsportsLeague
    tournament: EsportsTournament
    match: EsportsMatch


# ======================================== Leaderboard ========================================


@dataclass
class LeaderboardTier:
    """Leaderboard tier information.

    Attributes
    ----------
    id : :class:`int`
        Tier ID.
    name : :class:`str`
        Tier name (e.g., "Immortal 1", "Radiant").
    """

    id: int
    name: str


@dataclass
class LeaderboardThreshold:
    """Leaderboard tier threshold.

    Attributes
    ----------
    tier : :class:`LeaderboardTier`
        Tier information.
    start_index : :class:`int`
        Starting index for this tier.
    threshold : :class:`int`
        RR threshold to reach this tier.
    """

    tier: LeaderboardTier
    start_index: int
    threshold: int


@dataclass
class LeaderboardPlayer:
    """Leaderboard player entry.

    Attributes
    ----------
    puuid : :class:`str`
        Player's unique identifier.
    name : :class:`str`
        Player's game name.
    tag : :class:`str`
        Player's tag.
    card : :class:`str`
        Player card ID.
    title : :class:`str`
        Player title ID.
    is_banned : :class:`bool`
        Whether the player is banned.
    is_anonymized : :class:`bool`
        Whether the player is anonymized.
    leaderboard_rank : :class:`int`
        Current leaderboard rank.
    tier : :class:`int`
        Current rank tier.
    rr : :class:`int`
        Ranking rating points.
    wins : :class:`int`
        Number of wins.
    updated_at : :class:`datetime.datetime`
        Last update timestamp.
    """

    puuid: str
    name: str
    tag: str
    card: str
    title: str
    is_banned: bool
    is_anonymized: bool
    leaderboard_rank: int
    tier: int
    rr: int
    wins: int
    updated_at: datetime


@dataclass
class Leaderboard:
    """Leaderboard response.

    Attributes
    ----------
    results : :class:`ResultMetadata`
        Pagination metadata (total, returned, before, after).
    updated_at : :class:`datetime.datetime`
        When the leaderboard was last updated.
    thresholds : List[:class:`LeaderboardThreshold`]
        Tier threshold information.
    players : List[:class:`LeaderboardPlayer`]
        List of leaderboard players.
    """

    results: ResultMetadata
    updated_at: datetime = datetime.fromisoformat("1970-01-01T00:00:00+00:00")
    thresholds: List[LeaderboardThreshold] = field(default_factory=list)
    players: List[LeaderboardPlayer] = field(default_factory=list)


# ======================================== TypeVar ========================================

ValoPyModel = TypeVar(
    "ValoPyModel",
    AccountV1,
    AccountV2,
    Content,
    Version,
    WebsiteContent,
    Status,
    QueueData,
    EsportsEvent,
    Leaderboard,
    ResultMetadata,
)
