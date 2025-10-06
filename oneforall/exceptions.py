class LargeImageError(Exception):
    """Raised when an image exceeds the allowed embed size limit."""

    def __init__(self, image_name: str, size_kb: float, limit_kb: int) -> None:
        super().__init__(
            f"Image '{image_name}' is too large ({size_kb:.2f} KB > {limit_kb} KB limit)"
        )
        self.image_name = image_name
        self.size_kb = size_kb
        self.limit_kb = limit_kb
