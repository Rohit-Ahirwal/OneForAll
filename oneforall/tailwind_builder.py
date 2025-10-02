import os

def load_tailwind_css():
    """
    Locate and load the Tailwind CSS file for production.
    Priority:
      1. User project root (./tailwind.css)
      2. Installed package assets (oneforall/assets/tailwind.css)
    """
    # 1. User project root
    user_css = os.path.join(os.getcwd(), "tailwind.css")
    if os.path.exists(user_css):
        with open(user_css, "r", encoding="utf-8") as f:
            return f.read()

    # 2. Package assets
    pkg_dir = os.path.dirname(__file__)
    asset_css = os.path.join(pkg_dir, "assets", "tailwind.css")
    if os.path.exists(asset_css):
        with open(asset_css, "r", encoding="utf-8") as f:
            return f.read()

    # If nothing found
    raise FileNotFoundError(
        "Tailwind CSS file not found. Please run Tailwind build in your project root."
    )
