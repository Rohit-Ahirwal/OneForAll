from .components import Component
from .tailwind_builder import load_tailwind_css


class Renderer:
    @staticmethod
    def render_app(
        title: str, components: list[Component], dev_mode: bool = False
    ) -> str:
        """Render full HTML document from components"""

        body_html = "".join([comp.render() for comp in components])

        # Load CSS
        if dev_mode:
            # Use Tailwind CDN in dev mode
            css_link = '<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>'
            css = css_link
        else:
            # Use prebuilt local CSS in prod
            css_content = load_tailwind_css()
            css = f"<style>\n{css_content}\n</style>"

        # JS for event handling
        js = """
            <script>
            function sendEvent(id) {
                if(window.pywebview && window.pywebview.api && window.pywebview.api.call){
                    window.pywebview.api.call(id, {});
                }
            }
            </script>
        """

        html = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width,initial-scale=1">
            <title>{title}</title>
            {css}
            </head>
            <body>
            {body_html}
            {js}
            </body>
            </html>
        """
        return html
