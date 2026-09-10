from crewai import Agent, LLM
from tools import yt_tool

groq_llm = LLM(
    model="groq/openai/gpt-oss-20b",
    max_tokens=600,
    reasoning_effort="low",
)

blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    llm=groq_llm,
    goal='get the relevant video content for the topic {topic} from YT channel',
    verbose=True,
    memory=False,
    backstory=(
        "Expert in understanding videos in AI Data Science , Machine Learning and GEN AI"
    ),
    tools=[yt_tool],
    allow_delegation=False,
    max_retry_limit=1,
)

blog_writer = Agent(
    role='Blog Writer',
    llm=groq_llm,
    goal='Narrate compelling tech stories about the video {topic} from YT channel',
    verbose=True,
    memory=False,
    backstory=(
        "With a flair for simplifying complex topic ,you craft"
        "engaging narratives that captivate and educate,bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False,
    max_retry_limit=1,
)