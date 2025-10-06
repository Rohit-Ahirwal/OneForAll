import base64
import mimetypes
import os

from oneforall.assets_resolver import get_asset_path
from oneforall.exceptions import LargeImageError

from .logger import logger

SIZE_LIMIT_KB = int(os.getenv("SIZE_LIMIT_KB", 200))


def _get_fallback_base64() -> str:
    """
    Returns a tiny transparent PNG (1x1 pixel) as fallback.
    Prevents rendering errors when an image fails to load.
    """
    transparent_png = (
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8"
        "/w8AAwMCAOaQhhYAAAAASUVORK5CYII="
    )
    return f"data:image/png;base64,{transparent_png}"


def embed_image(image_name: str) -> str:
    """
    Return a Base64-encoded data URI for an image.
    Supports:
      - Remote URLs (http/https)
      - Local assets via get_asset_path()
    Raises LargeImageError if image exceeds SIZE_LIMIT_KB.
    Falls back to transparent PNG on failure.
    """
    # ✅ Remote image → use directly
    if image_name.startswith(("http://", "https://", "data:")):
        return image_name

    try:
        # ✅ Resolve local asset path
        image_path = get_asset_path(image_name)
        mime_type, _ = mimetypes.guess_type(image_path)
        if not mime_type:
            mime_type = "application/octet-stream"

        # ✅ Check size
        size_bytes = os.path.getsize(image_path)
        size_kb = size_bytes / 1024
        if size_kb > SIZE_LIMIT_KB:
            raise LargeImageError(image_name, size_kb, SIZE_LIMIT_KB)

        # ✅ Encode as base64
        with open(image_path, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode("utf-8")
        return f"data:{mime_type};base64,{b64}"

    except LargeImageError as e:
        logger.error(f"⚠️ {e}")
        return _get_fallback_base64()
    except Exception as e:
        logger.error(f"⚠️ Failed to embed image '{image_name}': {e}")
        return _get_fallback_base64()
