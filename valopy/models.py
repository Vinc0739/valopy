from dataclasses import dataclass, field
from datetime import datetime
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


@dataclass
class ResultMetadata:
    """Pagination and results metadata.

    Attributes
    ----------
    total : int
        Total number of results available.
    returned : int
        Number of results returned in this response.
    before : int
        Number of results before this page.
    after : int
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
    last_update : datetime
        Last update timestamp. Note: This is an approximation calculated from relative time strings
        (e.g., "3 minutes ago") returned by the API, so accuracy may vary by seconds/minutes.
    last_update_raw : int
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
    updated_at : datetime
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
    """Version response

    Attributes
    ----------
    region : str
        The region of the version data.
    branch : str
        The branch of the version data.
    build_date : datetime
        The build date of the version.
    build_ver : str
        The build version.
    last_checked : datetime
        The last checked timestamp.
    version : int
        The version number.
    version_for_api : str
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
    id : str
        The unique identifier for the website content.
    banner_url : str
        The URL of the banner image.
    category : str
        The category of the website content.
    date : datetime
        Release date of the content.
    title : str
        Title of the content.
    url : str
        The URL of the content.
    description : str
        Description of the content.
    external_link : str
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
    content : str
        The translated content message.
    locale : str
        The locale code (e.g., 'en_US').
    """

    content: str
    locale: str


@dataclass
class StatusTitle:
    """Title content for status entries.

    Attributes
    ----------
    content : str
        The title text.
    locale : str
        The locale code (e.g., 'en_US').
    """

    content: str
    locale: str


@dataclass
class StatusUpdate:
    """Individual status update entry.

    Attributes
    ----------
    created_at : datetime
        When the update was created.
    updated_at : datetime
        When the update was last modified.
    publish : bool
        Whether the update is published.
    id : int
        Unique identifier for the update.
    translations : List[StatusTranslation]
        Translated content messages.
    publish_locations : List[str]
        Where the update is published (e.g., 'riotclient').
    author : str
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
    created_at : datetime
        When the entry was created.
    archive_at : datetime
        When the entry will be archived.
    updates : List[StatusUpdate]
        List of status updates.
    platforms : List[str]
        Affected platforms (e.g., 'windows').
    updated_at : datetime
        When the entry was last modified.
    id : int
        Unique identifier for the entry.
    titles : List[StatusTitle]
        Titles for the entry.
    maintenance_status : str
        Current maintenance status (e.g., 'in_progress').
    incident_severity : str
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
    maintenances : List[StatusEntry]
        List of current maintenance announcements.
    incidents : List[StatusEntry]
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
    max : int
        Maximum party size allowed.
    min : int
        Minimum party size allowed.
    invalid : List[int]
        Party sizes that are not allowed.
    full_party_bypass : bool
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
    max_party_size : int
        Maximum party size for high skill players.
    min_tier : int
        Minimum tier affected by high skill restrictions.
    max_tier : int
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
    id : int
        Tier identifier.
    name : str
        Tier name.
    """

    id: int
    name: str


@dataclass
class QueueSkillDisparity:
    """Skill disparity restrictions for a queue.

    Attributes
    ----------
    tier : int
        The tier identifier.
    name : str
        Tier name.
    max_tier : QueueSkillDisparityTier
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
    overtime_win_by_two : bool
        Whether overtime requires winning by two.
    allow_lenient_surrender : bool
        Whether lenient surrender is allowed.
    allow_drop_out : bool
        Whether dropping out is allowed.
    assign_random_agents : bool
        Whether agents are randomly assigned.
    skip_pregame : bool
        Whether pregame is skipped.
    allow_overtime_draw_vote : bool
        Whether overtime draw voting is allowed.
    overtime_win_by_two_capped : bool
        Whether overtime win by two is capped.
    premier_mode : bool
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
    id : str
        Map UUID.
    name : str
        Map display name.
    """

    id: str
    name: str


@dataclass
class QueueMap:
    """Map configuration for a queue.

    Attributes
    ----------
    map : QueueMapInfo
        Map information.
    enabled : bool
        Whether the map is enabled in this queue.
    """

    map: QueueMapInfo
    enabled: bool


@dataclass
class QueueData:
    """Individual queue configuration.

    Attributes
    ----------
    mode : str
        Queue mode name (e.g., "Competitive").
    mode_id : str
        Queue mode identifier (e.g., "competitive").
    enabled : bool
        Whether the queue is currently enabled.
    team_size : int
        Number of players per team.
    number_of_teams : int
        Number of teams in a match.
    party_size : QueuePartySize
        Party size constraints.
    high_skill : QueueHighSkill
        High skill tier restrictions.
    ranked : bool
        Whether this is a ranked queue.
    tournament : bool
        Whether this is a tournament queue.
    skill_disparity : List[QueueSkillDisparity]
        Skill disparity restrictions by tier.
    required_account_level : int
        Minimum account level required.
    game_rules : QueueGameRules
        Game rules configuration.
    platforms : List[str]
        Available platforms (e.g., ["pc"]).
    maps : List[QueueMap]
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
    name : str
        League name.
    identifier : str
        League identifier.
    icon : str
        League icon URL.
    region : str
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
    name : str
        Tournament name.
    season : str
        Tournament season.
    """

    name: str
    season: str


@dataclass
class EsportsGameType:
    """Esports game type configuration.

    Attributes
    ----------
    type : str
        Game type (e.g., "playAll", "bestOf").
    count : int
        Number of games.
    """

    type: str
    count: int


@dataclass
class EsportsTeamRecord:
    """Esports team record.

    Attributes
    ----------
    wins : int
        Number of wins.
    losses : int
        Number of losses.
    """

    wins: int
    losses: int


@dataclass
class EsportsTeam:
    """Esports team information.

    Attributes
    ----------
    name : str
        Team name.
    code : str
        Team code.
    icon : str
        Team icon URL.
    has_won : bool
        Whether the team has won.
    game_wins : int
        Number of games won.
    record : EsportsTeamRecord
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
    id : str
        Match ID.
    game_type : EsportsGameType
        Game type configuration.
    teams : List[EsportsTeam]
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
    date : datetime
        Event date (ISO 8601 format).
    state : str
        Event state (e.g., "completed", "upcoming").
    type : str
        Event type (e.g., "match").
    vod : str
        Video on demand URL.
    league : EsportsLeague
        League information.
    tournament : EsportsTournament
        Tournament information.
    match : EsportsMatch
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
    id : int
        Tier ID.
    name : str
        Tier name (e.g., "Immortal 1", "Radiant").
    """

    id: int
    name: str


@dataclass
class LeaderboardThreshold:
    """Leaderboard tier threshold.

    Attributes
    ----------
    tier : LeaderboardTier
        Tier information.
    start_index : int
        Starting index for this tier.
    threshold : int
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
    puuid : str
        Player's unique identifier.
    name : str
        Player's game name.
    tag : str
        Player's tag.
    card : str
        Player card ID.
    title : str
        Player title ID.
    is_banned : bool
        Whether the player is banned.
    is_anonymized : bool
        Whether the player is anonymized.
    leaderboard_rank : int
        Current leaderboard rank.
    tier : int
        Current rank tier.
    rr : int
        Ranking rating points.
    wins : int
        Number of wins.
    updated_at : datetime
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
    results : ResultMetadata
        Pagination metadata (total, returned, before, after).
    updated_at : datetime
        When the leaderboard was last updated.
    thresholds : List[LeaderboardThreshold]
        Tier threshold information.
    players : List[LeaderboardPlayer]
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
