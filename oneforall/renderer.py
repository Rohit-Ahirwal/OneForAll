# flake8: noqa: W291
import html
import traceback

from .components import Component
from .tailwind_builder import load_tailwind_css


class Renderer:
    @staticmethod
    def show_error_modal(exc: Exception):
        tb_str = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
        tb_html = (
            "<pre style='white-space:pre-wrap; background:#1e1e1e; color:#ffbaba; padding:12px; border-radius:6px; overflow-x:auto;'>"
            + html.escape(tb_str)
            + "</pre>"
        )

        modal_html = f"""
        <div id="oneforall-error-overlay" style="
            position: fixed; top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0,0,0,0.7);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 99999;
            font-family: monospace;
        ">
            <div style="
                background: #111;
                color: #fff;
                border-radius: 12px;
                padding: 24px;
                max-width: 800px;
                width: 90%;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                animation: fadeIn 0.25s ease-in-out;
            ">
                <h2 style="color: #ff4d4f; margin: 0 0 16px 0; font-size: 18px;">
                    ⚠ OneForAll Render Error
                </h2>
                {tb_html}
                <button onclick="document.getElementById('oneforall-error-overlay').remove()" 
                    style="
                        margin-top: 16px;
                        padding: 8px 16px;
                        background: #ff4d4f;
                        color: #fff;
                        border: none;
                        border-radius: 6px;
                        cursor: pointer;
                        font-weight: bold;
                    ">
                    Dismiss
                </button>
            </div>
        </div>
        <style>
            @keyframes fadeIn {{
                from {{ opacity: 0; transform: translateY(-10px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
            body.modal-open {{
                overflow: hidden;
            }}
        </style>
        <script>
            document.body.classList.add('modal-open');
            document.getElementById('oneforall-error-overlay')
                .addEventListener('click', (e) => {{
                    if (e.target.id === 'oneforall-error-overlay') {{
                        e.target.remove();
                        document.body.classList.remove('modal-open');
                    }}
                }});
        </script>
        """
        return modal_html

    @staticmethod
    def render_app(
        title: str, components: list[Component], dev_mode: bool = False
    ) -> str:
        """Render full HTML document from components"""

        try:
            body_html = "".join([comp.render().to_html() for comp in components])

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

            content_html = f"""
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
            return content_html
        except Exception as e:
            return Renderer.show_error_modal(e)
