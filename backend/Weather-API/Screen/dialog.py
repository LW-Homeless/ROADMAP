import asyncio

from prompt_toolkit.widgets import Dialog, Label, Button
from prompt_toolkit.styles import Style
from prompt_toolkit.layout import Float, HSplit
from prompt_toolkit.layout.dimension import Dimension
from prompt_toolkit.application.current import get_app


async def show_error_dialog(title, text):
    """
    Show a small, centered error dialog as a floating window.
    """
    done = asyncio.Event()

    def on_ok():
        done.set()
        floats.pop()  # Quitamos el Float (el diálogo)

    app = get_app()
    layout = app.layout
    floats = layout.container.floats

    ok_button = Button(text="OK", handler=on_ok)

    dialog = Dialog(
        title=title,
        body=HSplit([
            Label(text=text, dont_extend_height=True),
        ], padding=1),
        buttons=[ok_button],
        width=Dimension(preferred=40),
        modal=True,
    )

    floats.append(Float(content=dialog))

    layout.focus(ok_button)

    await done.wait()
