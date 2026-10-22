import tomllib, tomli_w

from pathlib import Path
from platformdirs import user_config_path, user_documents_path

APP_NAME = "quick-tape"
CONFIG_DIR = user_config_path(APP_NAME)
CONFIG_FILE = Path(CONFIG_DIR) / "config.toml"

DEFAULT_CONFIG = {
    "download": {
        "path": str(user_documents_path() / "quick-tape"),
    },
    "prepare": {
        "cassette-type": {"label": "C60", "value": 60}
    }
}

def load_config() -> dict:
    if not CONFIG_FILE.exists():
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()

    with CONFIG_FILE.open("rb") as f:
        return tomllib.load(f)


def save_config(config: dict) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with CONFIG_FILE.open("wb") as f:
        tomli_w.dump(config, f)



