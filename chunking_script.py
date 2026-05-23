from pathlib import Path

OBSIDIAN_PATH = Path(r"/Users/luco/llmwiki")
RAW_DIR = OBSIDIAN_PATH / "raw"
WORK_DAILY = RAW_DIR / "WORK DAILY.md"
CHUNKS_PATH = OBSIDIAN_PATH / "chunks"
CHUNKS_SIZE = 200


with open(WORK_DAILY) as f:
    lines = [line.strip() for line in f if line.strip()]
    chunk_offset = CHUNKS_SIZE
    file_num = 0
    for i in range(0,len(lines),chunk_offset):
        forward_offset= i+chunk_offset
        page = lines[i:forward_offset]
        new_chunk_path = CHUNKS_PATH / f"chunk_{file_num}.md"
        new_chunk_path.parent.mkdir(parents=True, exist_ok=True)
        with open(new_chunk_path, "w") as chunk_file:
            chunk_file.write("\n".join(page))
        file_num += 1

