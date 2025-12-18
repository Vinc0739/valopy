from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Type

# ======================================== Result ========================================


@dataclass
class Result:
    """HTTP request result wrapper.

    Attributes
    ----------
    status_code : int
        The HTTP status code of the response.
    message : str
        The HTTP status message.
    data : dict
        The response data.
    """

    status_code: int
    message: str = "None"
    data: dict = field(default_factory=dict)


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


# ======================================== Leaderboard ========================================


@dataclass
class LeaderboardPlayer:
    """Leaderboard player structure"""

    PlayerCardID: str
    TitleID: str
    IsBanned: bool
    IsAnonymized: bool
    puuid: str
    gameName: str
    tagLine: str
    leaderboardRank: int
    rankedRating: int
    numberOfWins: int
    competitiveTier: int


@dataclass
class LeaderboardData:
    """Leaderboard data structure"""

    last_update: int = 0
    next_update: int = 0
    total_players: int = 0
    immortal_threshold: int = 0
    radiant_threshold: int = 0
    players: List[LeaderboardPlayer] = field(default_factory=list)


@dataclass
class LeaderboardResponse:
    """Leaderboard response"""

    status: int
    data: LeaderboardData = field(default_factory=lambda: LeaderboardData())


# ======================================== Match History ========================================


@dataclass
class MatchMap:
    """Match map info"""

    id: str
    name: str


@dataclass
class MatchSeason:
    """Match season info"""

    id: str
    short: str


@dataclass
class MatchMeta:
    """Match metadata"""

    id: str
    map: MatchMap
    version: str
    mode: str
    started_at: str
    season: MatchSeason
    region: str
    cluster: str


@dataclass
class MatchCharacter:
    """Match character info"""

    id: str
    name: str


@dataclass
class MatchShots:
    """Match shots statistics"""

    head: int
    body: int
    leg: int


@dataclass
class MatchDamage:
    """Match damage statistics"""

    dealt: int
    received: int


@dataclass
class MatchStats:
    """Match player statistics"""

    puuid: str
    team: str
    level: int
    character: MatchCharacter
    tier: int
    score: int
    kills: int
    deaths: int
    assists: int
    shots: MatchShots
    damage: MatchDamage


@dataclass
class MatchTeams:
    """Match teams scores"""

    red: int
    blue: int


@dataclass
class MatchHistoryEntry:
    """Match history entry structure"""

    meta: MatchMeta
    stats: MatchStats
    teams: MatchTeams


@dataclass
class MatchHistoryData:
    """Match history data structure"""

    name: str = ""
    tag: str = ""
    results: List[MatchHistoryEntry] = field(default_factory=list)


@dataclass
class MatchHistoryResponse:
    """Match history response"""

    status: int
    data: MatchHistoryData = field(default_factory=lambda: MatchHistoryData())


# ======================================== Match Details ========================================


@dataclass
class PremierInfo:
    """Premier match info"""

    tournament_id: str
    matchup_id: str


@dataclass
class MatchMetadata:
    """Match metadata structure"""

    map: str
    game_version: str
    game_length: int
    game_start: int
    game_start_patched: str
    rounds_played: int
    mode: str
    mode_id: str
    queue: str
    season_id: str
    platform: str
    matchid: str
    premier_info: Optional[PremierInfo] = None
    region: str = ""
    cluster: str = ""


@dataclass
class SessionPlaytime:
    """Session playtime structure"""

    minutes: int
    seconds: int
    milliseconds: int


@dataclass
class CardAssets:
    """Card assets structure"""

    small: str
    large: str
    wide: str


@dataclass
class AgentAssets:
    """Agent assets structure"""

    small: str
    bust: str
    full: str
    killfeed: str


@dataclass
class PlayerAssets:
    """Player assets structure"""

    card: CardAssets
    agent: AgentAssets


@dataclass
class FriendlyFire:
    """Friendly fire statistics"""

    incoming: int
    outgoing: int


@dataclass
class PlayerBehaviour:
    """Player behaviour statistics"""

    afk_rounds: int
    friendly_fire: FriendlyFire
    rounds_in_spawn: int


@dataclass
class PlatformOS:
    """Platform OS info"""

    name: str
    version: str


@dataclass
class PlayerPlatform:
    """Player platform info"""

    type: str
    os: PlatformOS


@dataclass
class AbilityCasts:
    """Ability casts statistics"""

    c_cast: int
    q_cast: int
    e_cast: int
    x_cast: int


@dataclass
class PlayerStats:
    """Player statistics"""

    score: int
    kills: int
    deaths: int
    assists: int
    bodyshots: int
    headshots: int
    legshots: int
    damage_made: int
    damage_received: int


@dataclass
class EconomySpent:
    """Economy spent statistics"""

    overall: int
    average: int


@dataclass
class EconomyLoadout:
    """Economy loadout value"""

    overall: int
    average: int


@dataclass
class PlayerEconomy:
    """Player economy statistics"""

    spent: EconomySpent
    loadout_value: EconomyLoadout


@dataclass
class MatchPlayer:
    """Match player structure"""

    puuid: str
    name: str
    tag: str
    team: str
    level: int
    character: str
    currenttier: int
    currenttier_patched: str
    player_card: str
    player_title: str
    party_id: str
    session_playtime: SessionPlaytime
    assets: PlayerAssets
    behaviour: PlayerBehaviour
    platform: PlayerPlatform
    ability_casts: AbilityCasts
    stats: PlayerStats
    economy: PlayerEconomy


@dataclass
class TeamCustomization:
    """Team customization structure"""

    icon: str = ""
    image: str = ""
    primary_color: str = ""
    secondary_color: str = ""
    tertiary_color: str = ""


@dataclass
class TeamRoster:
    """Team roster structure"""

    members: List[str] = field(default_factory=list)
    name: str = ""
    tag: str = ""
    customization: TeamCustomization = field(default_factory=lambda: TeamCustomization())


@dataclass
class MatchTeam:
    """Match team structure"""

    has_won: bool = False
    rounds_won: int = 0
    rounds_lost: int = 0
    roster: Optional[TeamRoster] = None


@dataclass
class Location:
    """Location coordinates"""

    x: int
    y: int


@dataclass
class PlayerInfo:
    """Player info structure"""

    puuid: str
    display_name: str
    team: str


@dataclass
class PlantEvents:
    """Plant events structure"""

    plant_location: Location
    planted_by: PlayerInfo
    plant_site: str
    plant_time_in_round: int
    player_locations_on_plant: List[Any] = field(default_factory=list)


@dataclass
class DefuseEvents:
    """Defuse events structure"""

    defuse_location: Location
    defused_by: PlayerInfo
    defuse_time_in_round: int
    player_locations_on_defuse: List[Any] = field(default_factory=list)


@dataclass
class WeaponAssets:
    """Weapon assets structure"""

    display_icon: str
    killfeed_icon: str


@dataclass
class RoundWeapon:
    """Round weapon structure"""

    id: str
    name: str
    assets: WeaponAssets


@dataclass
class ArmorAssets:
    """Armor assets structure"""

    display_icon: str


@dataclass
class RoundArmor:
    """Round armor structure"""

    id: str
    name: str
    assets: ArmorAssets


@dataclass
class RoundEconomy:
    """Round economy structure"""

    loadout_value: int = 0
    weapon: RoundWeapon = field(default_factory=lambda: RoundWeapon(id="", name="", assets=WeaponAssets("", "")))
    armor: RoundArmor = field(default_factory=lambda: RoundArmor(id="", name="", assets=ArmorAssets("")))
    remaining: int = 0
    spent: int = 0


@dataclass
class RoundAbilityCasts:
    """Round ability casts structure"""

    c_casts: int = 0
    q_casts: int = 0
    e_casts: int = 0
    x_casts: int = 0


@dataclass
class RoundPlayerStats:
    """Round player statistics"""

    player_puuid: str
    player_display_name: str
    player_team: str
    damage_events: List[Any] = field(default_factory=list)
    kill_events: List[Any] = field(default_factory=list)
    economy: RoundEconomy = field(default_factory=lambda: RoundEconomy())
    ability_casts: RoundAbilityCasts = field(default_factory=lambda: RoundAbilityCasts())
    was_afk: bool = False
    was_penalized: bool = False
    stayed_in_spawn: bool = False


@dataclass
class Round:
    """Round structure"""

    winning_team: str
    end_type: str
    bomb_planted: bool
    bomb_defused: bool
    plant_events: Optional[PlantEvents] = None
    defuse_events: Optional[DefuseEvents] = None
    player_stats: List[RoundPlayerStats] = field(default_factory=list)


@dataclass
class Assistant:
    """Kill assistant structure"""

    assistant_puuid: str
    assistant_display_name: str
    assistant_team: str


@dataclass
class Kill:
    """Kill structure"""

    kill_time_in_round: int
    kill_time_in_match: int
    killer_puuid: str
    killer_display_name: str
    killer_team: str
    victim_puuid: str
    victim_display_name: str
    victim_team: str
    victim_death_location: Location
    damage_weapon_id: str
    damage_weapon_name: str
    damage_weapon_assets: WeaponAssets
    secondary_fire_mode: bool
    player_locations_on_kill: List[Any] = field(default_factory=list)
    assistants: List[Assistant] = field(default_factory=list)


@dataclass
class MatchPlayers:
    """Match players structure"""

    all_players: List[MatchPlayer] = field(default_factory=list)
    red: List[MatchPlayer] = field(default_factory=list)
    blue: List[MatchPlayer] = field(default_factory=list)


@dataclass
class MatchTeamsData:
    """Match teams data structure"""

    red: MatchTeam = field(default_factory=lambda: MatchTeam())
    blue: MatchTeam = field(default_factory=lambda: MatchTeam())


@dataclass
class MatchData:
    """Match data structure"""

    metadata: MatchMetadata = field(
        default_factory=lambda: MatchMetadata(
            map="",
            game_version="",
            game_length=0,
            game_start=0,
            game_start_patched="",
            rounds_played=0,
            mode="",
            mode_id="",
            queue="",
            season_id="",
            platform="",
            matchid="",
        )
    )
    players: MatchPlayers = field(default_factory=lambda: MatchPlayers())
    teams: MatchTeamsData = field(default_factory=lambda: MatchTeamsData())
    rounds: List[Round] = field(default_factory=list)
    kills: List[Kill] = field(default_factory=list)


@dataclass
class MatchResponse:
    """Match response"""

    status: int
    data: MatchData = field(default_factory=lambda: MatchData())


# ======================================== MMR History ========================================


@dataclass
class MMRImages:
    """MMR tier images"""

    small: str
    large: str
    triangle_down: str
    triangle_up: str


@dataclass
class MMRHistoryEntry:
    """MMR history entry structure"""

    currenttier: int
    currenttierpatched: str
    images: MMRImages
    ranking_in_tier: int
    mmr_change_to_last_game: int
    elo: int
    date: str
    date_raw: int


@dataclass
class MMRHistoryData:
    """MMR history data structure"""

    name: str = ""
    tag: str = ""
    data: List[MMRHistoryEntry] = field(default_factory=list)


@dataclass
class MMRHistoryResponse:
    """MMR history response"""

    status: int
    data: MMRHistoryData = field(default_factory=lambda: MMRHistoryData())


# ======================================== Current MMR ========================================


@dataclass
class CurrentMMRData:
    """Current MMR data structure"""

    currenttier: int
    currenttierpatched: str
    images: MMRImages
    ranking_in_tier: int
    mmr_change_to_last_game: int
    elo: int
    games_needed_for_rating: int
    old: bool


@dataclass
class HighestRank:
    """Highest rank structure"""

    old: bool
    tier: int
    patched_tier: str
    season: str


@dataclass
class ActRankWin:
    """Act rank win structure"""

    patched_tier: str
    tier: int


@dataclass
class SeasonData:
    """Season data structure"""

    error: Optional[str] = None
    wins: int = 0
    number_of_games: int = 0
    final_rank: int = 0
    final_rank_patched: str = ""
    act_rank_wins: List[ActRankWin] = field(default_factory=list)
    old: bool = False


@dataclass
class MMRData:
    """MMR data structure"""

    name: str = ""
    tag: str = ""
    current_data: CurrentMMRData = field(
        default_factory=lambda: CurrentMMRData(
            currenttier=0,
            currenttierpatched="",
            images=MMRImages("", "", "", ""),
            ranking_in_tier=0,
            mmr_change_to_last_game=0,
            elo=0,
            games_needed_for_rating=0,
            old=False,
        )
    )
    highest_rank: HighestRank = field(
        default_factory=lambda: HighestRank(
            old=False,
            tier=0,
            patched_tier="",
            season="",
        )
    )
    by_season: Dict[str, SeasonData] = field(default_factory=dict)


@dataclass
class MMRResponse:
    """MMR response"""

    status: int
    data: MMRData = field(default_factory=lambda: MMRData())


# ======================================== Premier ========================================


@dataclass
class PremierStats:
    """Premier team stats"""

    wins: int
    losses: int
    matches: int
    rating: int
    standing: int


@dataclass
class PremierPlacement:
    """Premier team placement"""

    points: int
    conference: str
    division: int
    place: int


@dataclass
class PremierMember:
    """Premier team member"""

    puuid: str
    name: str
    tag: str


@dataclass
class PremierTeamData:
    """Premier team data structure"""

    id: str = ""
    name: str = ""
    tag: str = ""
    enrolled: bool = False
    stats: PremierStats = field(default_factory=lambda: PremierStats(wins=0, losses=0, matches=0, rating=0, standing=0))
    placement: PremierPlacement = field(
        default_factory=lambda: PremierPlacement(
            points=0,
            conference="",
            division=0,
            place=0,
        )
    )
    customization: TeamCustomization = field(default_factory=lambda: TeamCustomization())
    member: List[PremierMember] = field(default_factory=list)


@dataclass
class PremierTeamResponse:
    """Premier team response"""

    status: int
    data: PremierTeamData = field(default_factory=lambda: PremierTeamData())


# ======================================== Queue Status ========================================


@dataclass
class QueueStatusData:
    """Queue status data structure"""

    isDisabled: bool = False


@dataclass
class QueueStatusResponse:
    """Queue status response"""

    status: int
    data: QueueStatusData = field(default_factory=lambda: QueueStatusData())


# ======================================== Status ========================================


@dataclass
class StatusTranslation:
    """Status translation structure"""

    content: str
    locale: str


@dataclass
class StatusUpdate:
    """Status update structure"""

    created_at: str
    updated_at: str
    publish: bool
    id: int
    translations: List[StatusTranslation] = field(default_factory=list)
    publish_locations: List[str] = field(default_factory=list)
    author: str = ""


@dataclass
class StatusIncident:
    """Status incident structure"""

    created_at: str
    archive_at: str
    updates: List[StatusUpdate] = field(default_factory=list)
    platforms: List[str] = field(default_factory=list)
    updated_at: str = ""
    id: int = 0
    titles: List[StatusTranslation] = field(default_factory=list)
    maintenance_status: Optional[str] = None
    incident_severity: Optional[str] = None


@dataclass
class StatusData:
    """Status data structure"""

    maintenances: List[StatusIncident] = field(default_factory=list)
    incidents: List[StatusIncident] = field(default_factory=list)


@dataclass
class StatusResponse:
    """Status response"""

    status: int
    region: str
    data: StatusData = field(default_factory=StatusData)


# ======================================== Stored Matches ========================================


@dataclass
class StoredMatchesData:
    """Stored matches data structure"""

    results: List[MatchHistoryEntry] = field(default_factory=list)


@dataclass
class StoredMatchesResponse:
    """Stored matches response"""

    status: int
    data: StoredMatchesData = field(default_factory=StoredMatchesData)


# ======================================== Store ========================================


@dataclass
class OfferReward:
    """Offer reward structure"""

    ItemTypeID: str
    ItemID: str
    Quantity: int


@dataclass
class StoreOfferV1Data:
    """Store offer V1 structure"""

    OfferID: str
    IsDirectPurchase: bool
    StartDate: str
    Cost: Dict[str, int]
    Rewards: List[OfferReward] = field(default_factory=list)


@dataclass
class StoreOfferV1:
    """Store offer V1 wrapper"""

    Offer: StoreOfferV1Data


@dataclass
class OfferType:
    """Offer type structure"""

    id: str
    name: str


@dataclass
class ContentTier:
    """Content tier structure"""

    name: str
    dev_name: str
    icon: str


@dataclass
class StoreOfferV2:
    """Store offer V2 structure"""

    offer_id: str
    cost: Dict[str, int]
    name: str
    icon: str
    type: OfferType
    skin_id: str
    content_tier: ContentTier


@dataclass
class StoreOffersV1Response:
    """Store offers V1 response"""

    status: int
    data: List[StoreOfferV1] = field(default_factory=list)


@dataclass
class StoreOffersV2Response:
    """Store offers V2 response"""

    status: int
    data: List[StoreOfferV2] = field(default_factory=list)


# ======================================== Version ========================================


@dataclass
class VersionData:
    """Version data structure"""

    manifestId: str = ""
    branch: str = ""
    version: str = ""
    buildVersion: str = ""
    engineVersion: str = ""
    riotClientVersion: str = ""
    riotClientBuild: str = ""
    buildDate: str = ""


@dataclass
class VersionResponse:
    """Version response"""

    status: int
    data: VersionData = field(default_factory=lambda: VersionData())


# ======================================== Website ========================================


@dataclass
class WebsiteArticle:
    """Website article structure"""

    banner_url: str
    category: str
    date: str
    external_link: str
    title: str
    url: str


@dataclass
class WebsiteResponse:
    """Website response"""

    status: int
    data: List[WebsiteArticle] = field(default_factory=list)


# ======================================== Endpoint Mapping ========================================


def _get_endpoint_model_map() -> dict[str, Type[Any]]:
    """Get the mapping of API endpoints to their response model classes.

    Returns
    -------
    dict[str, Type[Any]]
        Dictionary mapping endpoint paths to model classes for automatic deserialization.
    """
    # Import here to avoid circular imports
    from .enums import Endpoint

    return {
        # Account endpoints
        Endpoint.ACCOUNT_BY_NAME_V1.value: AccountV1,
        Endpoint.ACCOUNT_BY_NAME_V2.value: AccountV2,
        Endpoint.ACCOUNT_BY_PUUID_V1.value: AccountV1,
        Endpoint.ACCOUNT_BY_PUUID_V2.value: AccountV2,
        # Content endpoints
        Endpoint.CONTENT_V1.value: Content,
        # Leaderboard endpoints
        Endpoint.LEADERBOARD_V1.value: LeaderboardResponse,
        Endpoint.LEADERBOARD_V2.value: LeaderboardResponse,
        Endpoint.LEADERBOARD_V3.value: LeaderboardResponse,
        # Match history endpoints
        Endpoint.MATCHES_V3.value: MatchHistoryResponse,
        Endpoint.MATCHES_V4.value: MatchHistoryResponse,
        Endpoint.MATCHES_BY_PUUID_V3.value: MatchHistoryResponse,
        Endpoint.MATCHES_BY_PUUID_V4.value: MatchHistoryResponse,
        # Match detail endpoints
        Endpoint.MATCH_V2.value: MatchResponse,
        Endpoint.MATCH_V4.value: MatchResponse,
        # MMR history endpoints
        Endpoint.MMR_HISTORY_V1.value: MMRHistoryResponse,
        Endpoint.MMR_HISTORY_BY_PUUID_V1.value: MMRHistoryResponse,
        Endpoint.MMR_HISTORY_BY_PUUID_V2.value: MMRHistoryResponse,
        # MMR endpoints
        Endpoint.MMR_V2.value: MMRResponse,
        Endpoint.MMR_V3.value: MMRResponse,
        Endpoint.MMR_BY_PUUID_V2.value: MMRResponse,
        Endpoint.MMR_BY_PUUID_V3.value: MMRResponse,
        # Premier endpoints
        Endpoint.PREMIER_TEAM.value: PremierTeamResponse,
        Endpoint.PREMIER_TEAM_HISTORY.value: PremierTeamResponse,
        Endpoint.PREMIER_CONFERENCE_LEADERBOARD.value: LeaderboardResponse,
        Endpoint.PREMIER_SEARCH.value: PremierTeamResponse,
        # Queue status endpoints
        Endpoint.QUEUE_STATUS_V1.value: QueueStatusResponse,
        # Status endpoints
        Endpoint.STATUS_V1.value: StatusResponse,
        # Stored data endpoints
        Endpoint.STORED_MATCHES_V1.value: StoredMatchesResponse,
        Endpoint.STORED_MMR_HISTORY_V1.value: MMRHistoryResponse,
        # Store endpoints
        Endpoint.STORE_OFFERS_V1.value: StoreOffersV1Response,
        Endpoint.STORE_OFFERS_V2.value: StoreOffersV2Response,
        # Version endpoints
        Endpoint.VERSION_V1.value: VersionResponse,
        # Website endpoints
        Endpoint.WEBSITE_V1.value: WebsiteResponse,
    }


# Cached endpoint model map
_ENDPOINT_MODEL_MAP: dict[str, Type[Any]] | None = None


def get_endpoint_model_map() -> dict[str, Type[Any]]:
    """Get the cached endpoint model map, creating it if necessary.

    Returns
    -------
    dict[str, Type[Any]]
        Dictionary mapping endpoint paths to model classes.
    """
    global _ENDPOINT_MODEL_MAP
    if _ENDPOINT_MODEL_MAP is None:
        _ENDPOINT_MODEL_MAP = _get_endpoint_model_map()
    return _ENDPOINT_MODEL_MAP
