# Working Wiki

A lightweight personal knowledge base generator for Obsidian-style notes, built on Python and LangChain.

This project helps you extract structured project and technology updates from raw daily notes, then build a searchable wiki from those summaries.

## What it does

- Reads raw Markdown notes from an Obsidian workspace.
- Splits longer notes into chunks for easier processing.
- Sends each chunk through a structured LLM pipeline to extract:
  - daily `pulse` summaries
  - `projects` updates
  - `technologies` learned or applied
- Writes the extracted knowledge back into a wiki-style Markdown structure.

## Key files

- `llm_builder.ipynb` — the main notebook workflow using LangChain, OpenAI, and Pydantic structured output.
- `chunking_script.py` — a helper script to break a single daily note into fixed-size Markdown chunks.
- `main.py` — a small entry point placeholder for the repository.
- `pyproject.toml` — dependency and package metadata.

## Dependencies

This project uses Python 3.12+ and these packages:

- `dotenv`
- `ipykernel`
- `langchain`
- `langchain-core`
- `langchain-openai`
- `pydantic`

## Setup

1. Clone the repository.
2. Install dependencies from `pyproject.toml`:

```bash
python -m pip install -U pip
python -m pip install -e .
```

> If you use `uv`, sync with the project metadata:

```bash
uv sync
```

3. Create a `.env` file with your OpenAI API key if needed.

## Usage

### Chunk raw notes

Run `chunking_script.py` to slice a large note into smaller Markdown chunks.

```bash
python chunking_script.py
```

### Process notes with the LLM

Open `llm_builder.ipynb` and run the notebook cells to generate structured wiki content from your note chunks.

The notebook builds prompt context, calls LangChain’s structured output model, and writes pulse pages to the `AI Wiki` folder.

## Notes

- The notebook currently uses a custom `Pulse` model to structure output.
- The current setup includes a sample OpenAI model name: `gpt-5.4-mini`.
- The workspace paths are currently hard-coded and may need updating to match your local Obsidian directories.

## License

This repository is currently unlicensed. Add a license file if you want to share it publicly.
