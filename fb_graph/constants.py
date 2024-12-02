from enum import StrEnum, unique

class MediaType(StrEnum):
    CAROUSSEL_ALBUM = 'CAROUSEL_ALBUM'
    IMAGE = 'IMAGE'
    VIDEO = 'VIDEO'
    
    
class MediaProductType(StrEnum):
    AD = 'AD'
    FEED = 'FEED'
    STORY = 'STORY'
    REELS = 'REELS'
    

@unique
class Metric(StrEnum):
    clips_replays_count = 'clips_replays_count'
    plays = 'plays'
    ig_reels_aggregated_all_plays_count = 'ig_reels_aggregated_all_plays_count'
    ig_reels_avg_watch_time = 'ig_reels_avg_watch_time'
    ig_reels_video_view_total_time = 'ig_reels_video_view_total_time'
    comments = 'comments'
    likes = 'likes'
    reach = 'reach'
    saved = 'saved'
    shares = 'shares'
    total_interactions = 'total_interactions'
    video_views = 'video_views'
    impressions = 'impressions'
    follows = 'follows'
    profile_activity = 'profile_activity'
    profile_visits = 'profile_visits'
    replies = 'replies'
    navigation = 'navigation'
    
    
# mapping of metrics available for each media product type and media type
MEDIAPRODUCTTYPE_TO_METRICS = {
    (MediaProductType.REELS, MediaType.VIDEO): [
        Metric.clips_replays_count,
        Metric.plays,
        Metric.ig_reels_aggregated_all_plays_count,
        Metric.ig_reels_avg_watch_time,
        Metric.ig_reels_video_view_total_time,
        Metric.comments,
        Metric.likes,
        Metric.reach,
        Metric.saved,
        Metric.shares,
        Metric.total_interactions,
        Metric.video_views,
    ],
    (MediaProductType.FEED, MediaType.IMAGE): [
        Metric.impressions,
        Metric.reach,
        Metric.saved,
        Metric.comments,
        Metric.follows,
        Metric.likes,
        Metric.profile_activity,
        Metric.profile_visits,
        Metric.shares,
        Metric.total_interactions,    
    ],
    (MediaProductType.FEED, MediaType.CAROUSSEL_ALBUM): [
        Metric.impressions,
        Metric.reach,
        Metric.saved,
        Metric.comments,
        Metric.follows,
        Metric.likes,
        Metric.profile_activity,
        Metric.profile_visits,
        Metric.shares,
        Metric.total_interactions,    
    ],
    (MediaProductType.STORY, MediaType.IMAGE): [
        Metric.impressions,
        Metric.reach,
        Metric.replies,
        Metric.follows,
        Metric.navigation,
        Metric.profile_activity,
        Metric.profile_visits,
        Metric.shares,
        Metric.total_interactions,
    ],
    (MediaProductType.STORY, MediaType.VIDEO): [
        Metric.impressions,
        Metric.reach,
        Metric.replies,
        Metric.follows,
        Metric.navigation,
        Metric.profile_activity,
        Metric.profile_visits,
        Metric.shares,
        Metric.total_interactions,
    ],
}