# YouTube Blog Creation Crew

This project uses [CrewAI](https://www.crewai.com/) to turn YouTube channel content into a concise technical blog post. A researcher agent finds relevant content, then a writer agent summarizes it and saves the result to `new-blog-post.md`.

The YouTube source is currently configured in `tools.py` as the Krishnaik06 channel:

```text
https://www.youtube.com/@krishnaik06
```

## Requirements

- Python 3.13 or newer
- A [Groq API key](https://console.groq.com/keys)
- `uv` for environment and dependency management

The project uses the Groq model `groq/openai/gpt-oss-20b` through CrewAI.

## Setup

1. Clone or open the project directory.
2. Create a `.env` file in the project root:

	```env
	GROQ_API_KEY=your_groq_api_key
	```

3. Install the project dependencies:

	```powershell
	uv sync
	```

## Run

Run the CrewAI workflow with:

```powershell
uv run run_crew
```

The same workflow can be started directly with Python:

```powershell
uv run python crew.py
```

The current topic is set in `crew.py`:

```python
inputs={"topic": "What is AI Security?"}
```

Change that value to generate a post about another topic from the configured channel.

## Output

The writing task writes the generated post to:

```text
new-blog-post.md
```

The file may be overwritten each time the crew runs.

## Project structure

| File | Purpose |
| --- | --- |
| `crew.py` | Builds and runs the sequential CrewAI crew |
| `agent.py` | Defines the researcher and writer agents |
| `tasks.py` | Defines the research and writing tasks |
| `tools.py` | Configures the YouTube channel search and embedding tool |
| `new-blog-post.md` | Generated blog post output |
| `pyproject.toml` | Project metadata, dependencies, and `run_crew` command |

## Notes

- The first run may download the `all-MiniLM-L6-v2` sentence-transformer model used for semantic search.
- `tools.py` restricts searches to the configured YouTube channel.
- `main.py` only contains a hello-world example; use `crew.py` to run the blog generation workflow.
