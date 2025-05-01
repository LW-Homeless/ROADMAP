import asyncio

from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout, HSplit, FloatContainer
from prompt_toolkit.widgets import TextArea, Frame
from prompt_toolkit.styles import Style
from prompt_toolkit.key_binding import KeyBindings

from model.WeatherAPI import WeatherAPI
from Screen.dialog import show_error_dialog

# table data
headers = ['Datatime', 'Temperature Max.', 'Temperature Min.', 'Sunrise', 'Sunset', 'windspeed', 'Conditions', 'Name']
rows = []

# Column widths
col_widths = [12, 18, 18, 12, 12, 12, 30, 30]


# Format table with borders
def format_table(headers, rows):
    def row_line(cells, sep='│'):
        return sep + sep.join(f" {str(cell):<{w-2}} " for cell, w in zip(cells, col_widths)) + sep

    col_widths = [max(len(str(cell)) for cell in col) + 2
                  for col in zip(headers, *rows)]

    top = "┌" + "┬".join("─" * w for w in col_widths) + "┐"
    header = row_line(headers)
    sep = "├" + "┼".join("─" * w for w in col_widths) + "┤"
    data = "\n".join(row_line(r) for r in rows)
    bottom = "└" + "┴".join("─" * w for w in col_widths) + "┘"

    return f"{top}\n{header}\n{sep}\n{data}\n{bottom}"


# Table display (read-only)
table_display = TextArea(text=format_table(headers, rows), read_only=True)


# Input handler
def on_enter(buff):
    asyncio.create_task(handle_enter())


async def handle_enter():
    global table_display
    country = input_field.text.strip().capitalize()

    w = WeatherAPI(country)

    query = w.query_weather()

    if 'Error' in query:
        if query['Error_n'] > 200:
            await show_error_dialog(title="Error de Conexión", text="Weather API is not response.")
        elif query['Error_n'] == 11001:
            await show_error_dialog(title="Error de Conexión", text="Failed to connect to the weather API.")
    else:
        for data in query:
            rows.append([data['datetime'], data['tempmax'], data['tempmin'],
                         data['sunrise'], data['sunset'], data['windspeed'], data['conditions'], data['resolvedAddress']])

    table_display.text = format_table(headers, rows)
    rows.clear()

    input_field.text = ''
    layout.focus(input_field)

# Input field
input_field = TextArea(
    prompt='> ',
    height=1,
    multiline=False,
    accept_handler=lambda buff: asyncio.create_task(handle_enter())
)

# Header (top-left)
header = TextArea(
    text="Weather API\nv1.0.0",
    style="class:header",
    read_only=True,
    focusable=False,
    height=2
)

# Layout with header and borders
body = HSplit([
    header,
    Frame(table_display),
    Frame(input_field, title="Enter country or city")
])

root_container = FloatContainer(
    content=body,
    floats=[]
)

layout = Layout(root_container)
layout.focus(input_field)

# Key bindings
kb = KeyBindings()


@kb.add('c-c')
def exit_app(event):
    event.app.exit()


# Style
style = Style.from_dict({
    'frame.label': '#ffffff bold',
    'frame.border': '#0000FF',
    'text-area': '#ffffff',
    'header': '#FF0000 bold',
    'table': '#00FF00',
    "dialog": "bg:#1e1e1e",
    "dialog frame.label": "bg:#1e1e1e #ff0000 bold",
    "dialog.body": "bg:#1e1e1e #ffffff",
    "button": "bg:#444444 #ffffff",
    "button.focused": "bg:#ff0000 #000000",
})

# Application
app = Application(
    layout=layout,
    key_bindings=kb,
    style=style,
    full_screen=True
)

if __name__ == '__main__':
    app.run()
