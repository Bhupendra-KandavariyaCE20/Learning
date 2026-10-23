import logging
from pathlib import Path


logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler(),
        ],
    )

logger = logging.getLogger(__name__)

def read_file(filename: str)->str|None:
    logger.info("Reading file: %s", filename)

    try:
        return Path(filename).read_text(encoding="utf-8")
    except FileNotFoundError:
        logger.exception("File not found: %s", filename)
        return None

if __name__ == "__main__":
    content = read_file("data.txt")
