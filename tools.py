import sys
import pytubefix

sys.modules['pytube'] = pytubefix
sys.modules['pytube.contrib'] = pytubefix.contrib
sys.modules['pytube.contrib.channel'] = pytubefix.contrib.channel

from crewai_tools import YoutubeChannelSearchTool
from crewai_tools.rag.data_types import DataType
from crewai_tools.tools.rag.rag_tool import RagTool
from crewai_tools.tools.youtube_channel_search_tool.youtube_channel_search_tool import (
    FixedYoutubeChannelSearchToolSchema,
)

CHANNEL_URL = "https://www.youtube.com/@krishnaik06"

yt_tool = YoutubeChannelSearchTool(
    config={
        "embedding_model": {
            "provider": "sentence-transformer",
            "config": {
                "model_name": "all-MiniLM-L6-v2"
            }
        },
        "vectordb": {
            "provider": "chromadb",
            "config": {
                "collection_name": "yt_blog_sydneyserena_v3"
            }
        }
    }
)

RagTool.add(
    yt_tool,
    CHANNEL_URL,
    data_type=DataType.YOUTUBE_CHANNEL,
)

# Manually re-apply what the constructor would normally do when given a
# working handle directly: lock the tool to this one channel, so the
# model only needs to supply a search query — not guess a channel name.
yt_tool.description = (
    f"A tool that can be used to semantic search a query the {CHANNEL_URL} Youtube Channels content."
)
yt_tool.args_schema = FixedYoutubeChannelSearchToolSchema
yt_tool._generate_description()