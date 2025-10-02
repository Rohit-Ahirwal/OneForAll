from typing import List

def merge_classes(default: str, custom: str) -> str:
    """
    Merge default Tailwind classes with user-defined classes.
    User classes take precedence in case of conflicts (e.g., p-2 vs p-4).
    """
    def class_set(cls: str) -> List[str]:
        return cls.strip().split() if cls else []

    default_list = class_set(default)
    custom_list = class_set(custom)

    # Simple approach: if same prefix exists in custom, remove from default
    # e.g., "p-2" in default and "p-4" in custom => keep "p-4"
    result = []

    # Map for quick conflict resolution
    seen_prefixes = set()
    for cls in reversed(custom_list):
        prefix = cls.split("-")[0]  # e.g., "p-4" -> "p"
        seen_prefixes.add(prefix)
        result.insert(0, cls)

    for cls in default_list:
        prefix = cls.split("-")[0]
        if prefix not in seen_prefixes:
            result.insert(0, cls)

    return " ".join(result)
