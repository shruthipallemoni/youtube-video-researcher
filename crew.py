# Workaround: Groq doesn't support CrewAI's newer prompt-cache marker yet.
# This disables that marker so it's never added to messages sent to Groq.
import crewai.llms.cache as _cache_patch
_cache_patch.mark_cache_breakpoint = lambda message: message

# ... rest of your existing imports and code below

from crewai import Crew,Process
from agent import blog_writer,blog_researcher
from tasks import research_task,write_task
from tools import yt_tool
from dotenv import load_dotenv
load_dotenv()

crew=Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,
    memory=False,
    cache=True,
    max_rpm=100,
    share_crew=True
)

def run():
    """Start the crew execution."""
    result = crew.kickoff(inputs={'topic': 'What is AI Security?'})
    print(result)


if __name__ == '__main__':
    run()
