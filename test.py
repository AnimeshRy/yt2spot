# from youtube_title_parse import get_artist_title
# from googleapiclient.discovery import build
# import json

# api_service_name = "youtube"
# api_version = "v3"

# youtube = build(
#     api_service_name, api_version, developerKey=DEVELOPER_KEY)

# request = youtube.playlistItems().list(
#     part="snippet",
#     maxResults=300,
#     playlistId="PLc2sKlfFc01q2vgCacU2a2OI3QBIaltcN",
#     pageToken=None
# )
# response = request.execute()
from collections import namedtuple

ab = 23
rank = 'dnsjd'

Point = namedtuple('Point', ['x', 'y'])
print(Point)
