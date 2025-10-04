import sys
from pathlib import Path


def get_asset_path(relative_path: str) -> str:
    """
    Returns the absolute path to an asset.
    Search order:
      1. User's ./assets/ folder (CWD)
      2. PyInstaller _MEIPASS assets folder
      3. Development package assets folder
    """
    # 1️⃣ Check user's ./assets/ folder
    cwd_asset_path = Path.cwd() / "assets" / relative_path
    if cwd_asset_path.exists():
        return str(cwd_asset_path)

    # 2️⃣ Check PyInstaller bundle
    base_path = getattr(sys, "_MEIPASS", None)
    if base_path:
        pyinstaller_path = Path(base_path) / "oneforall" / "assets" / relative_path
        if pyinstaller_path.exists():
            return str(pyinstaller_path)

    # 3️⃣ Check package assets folder (development)
    dev_path = Path(__file__).parent / "assets" / relative_path
    if dev_path.exists():
        return str(dev_path)

    # 4️⃣ Not found
    raise FileNotFoundError(
        f"Asset not found: '{relative_path}'. Searched ./assets/, PyInstaller bundle, and package assets."
    )
