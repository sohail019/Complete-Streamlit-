from nicegui import ui, html, events, Tailwind
from random import random
import numpy as np
from matplotlib import pyplot as plt
import math
from datetime import datetime
import asyncio

#* TEXT ELEMENTS

#Label: display some text
ui.label('Hello, NICE GUI!')


# Link: Create a hyperlink, (text, target = url, new_tab = by default false)
ui.link('Click me for NICE GUI Website', 'https://nicegui.io', new_tab=True)

# Chat Message: Display a chat message, (text = message body, name = message author, label = header/section, stamp = time of msg, avatar = URL to profile picture, sent = as a sent message [so from current user], text_html)
ui.label('Chat Message:')
ui.chat_message("Hello, Nice GUI!", name="Sohail", label="Welcome", stamp="10.00 AM", avatar="https://avatars.githubusercontent.com/u/69633245?v=4", sent=True, text_html=False)

# Multiline chat
ui.chat_message(['Hi! 😀', 'How are you?'])

ui.separator()
# Generic Element: This class is the base class for all other UI elements. But we can use it to create elements with arbitrary HTML tags. (tag: HTML tag, _client: client for this element)

with ui.element('div').classes('p-2 bg-blue-500'):
    ui.label('This is a custom HTML element')


# Markdown Element: 
ui.markdown('This is **Markdown**.')

ui.label('This is a Mermaid diagram.')
# Mermaid element: render diagrams and chart written in markdown inspired Mermaid language
ui.mermaid('graph TD; A-->B; A-->C; B-->D; C-->D;')
ui.separator()

# Other HTML Elements:There is also an html module that allows you to insert other HTML elements like <span>, <div>, <p>, etc. It is equivalent to using the ui.element method with the tag argument.

with html.section().style('font-size: 120%'):
    html.strong('This is bold.') \
        .classes('cursor-pointer') \
        .on('click', lambda: ui.notify('Bold!'))
    html.hr()
    html.em('This is italic.').tooltip('Nice!')
    with ui.row():
        html.img().props('src=https://placehold.co/60')
        html.img(src='https://placehold.co/60')
ui.separator()

#* Controls
ui.markdown('## Controls')
ui.label('Button:')
# Buttons: (text, on_click = callback which is invoked when button is pressed, color, icon)
ui.button('Click me', on_click=lambda: ui.notify('Button clicked!'), color='primary', icon='check')
ui.separator()
# Expandable Floating Action Button
ui.label('Expandable Floating Action Button')
with ui.element('q-fab').props('icon=navigation color=green'):
    ui.element('q-fab-action').props('icon=train color=green-5') \
        .on('click', lambda: ui.notify('train'))
    ui.element('q-fab-action').props('icon=sailing color=green-5') \
        .on('click', lambda: ui.notify('boat'))
    ui.element('q-fab-action').props('icon=rocket color=green-5') \
        .on('click', lambda: ui.notify('rocket'))
ui.separator()

# Button Group:
ui.label('Button Group:')
with ui.button_group():
    ui.button('One', on_click=lambda: ui.notify('You clicked Button 1!'))
    ui.button('Two', on_click=lambda: ui.notify('You clicked Button 2!'))
    ui.button('Three', on_click=lambda: ui.notify('You clicked Button 3!'))
ui.separator()

# Dropdown Button:
ui.label('Dropdown Button:')
with ui.dropdown_button('Open me!', auto_close=True):
    ui.item('Item 1', on_click=lambda: ui.notify('You clicked item 1'))
    ui.item('Item 2', on_click=lambda: ui.notify('You clicked item 2'))

ui.separator()

# Badge: (text, color, text_color, outline)
ui.label('Badge:')
with ui.button('Click me!', on_click=lambda: badge.set_text(int(badge.text) + 1)):
    badge = ui.badge('0', color='red').props('floating')
ui.separator()

# Chip: It can be clickable, selectable and removable.
ui.label('Chip: It can be clickable, selectable and removable.')
with ui.row().classes('gap-1'):
    ui.chip('Click me', icon='ads_click', on_click=lambda: ui.notify('Clicked'))
    ui.chip('Selectable', selectable=True, icon='bookmark', color='orange')
    ui.chip('Removable', removable=True, icon='label', color='indigo-3')
    ui.chip('Styled', icon='star', color='green').props('outline square')
    ui.chip('Disabled', icon='block', color='red').set_enabled(False)
ui.separator()

# Toggle: The options can be specified as a list of values, or as a dictionary mapping values to labels. After manipulating the options, call update() to update the options in the UI.
ui.label('Toggle:')
toggle1 = ui.toggle([1, 2, 3], value=1)
toggle2 = ui.toggle({1: 'A', 2: 'B', 3: 'C'}).bind_value(toggle1, 'value')
ui.separator()

# Radio Button: The options can be specified as a list of values, or as a dictionary mapping values to labels. After manipulating the options, call update() to update the options in the UI.
ui.label('Radio Button:')
radio1 = ui.radio([1, 2, 3], value=1).props('inline')
radio2 = ui.radio({1: 'A', 2: 'B', 3: 'C'}).props('inline').bind_value(radio1, 'value')
ui.separator()

# Checkbox : 
ui.label('Checkbox:')
checkbox = ui.checkbox('check me')
ui.label('Check!').bind_visibility_from(checkbox, 'value')
ui.separator()

# Switch:
ui.label('Switch:')
switch = ui.switch('switch me')
ui.label('Switch!').bind_visibility_from(switch, 'value')
ui.separator()

# Slider: (min, max, value, step, label, color, icon, on_change)
ui.label('Slider:')
slider = ui.slider(min=0, max=100, value=50)
ui.label().bind_text_from(slider, 'value')
ui.separator()

# Range: (min, max, value, step, label, color, icon, on_change)
min_max_range = ui.range(min=0, max=100, value={'min': 20, 'max': 80})
ui.label().bind_text_from(min_max_range, 'value',
                          backward=lambda v: f'min: {v["min"]}, max: {v["max"]}')
ui.separator()

# Joystick: (on_start=callback for when user touches joystick, on_move, on_end, throttle,  )
ui.joystick(
    color='blue', size=50,
    on_move=lambda e: coordinates.set_text(f'{e.x:.3f}, {e.y:.3f}'),
    on_end=lambda _: coordinates.set_text('0, 0'),
).classes('bg-slate-300')
coordinates = ui.label('0, 0')

ui.separator()

# Form Control
ui.markdown('## Forms')

# Input
ui.label('Input:')
ui.input(label='Text', placeholder='start typing',
         on_change=lambda e: input_result.set_text('you typed: ' + e.value),
         validation={'Input too long': lambda value: len(value) < 20})
input_result = ui.label()
ui.separator()

# TextArea
ui.label('TextArea:')
ui.textarea(label='Text', placeholder='start typing',
            on_change=lambda e: textarea_result.set_text('you typed: ' + e.value))
textarea_result = ui.label()
ui.separator()

# Code Mirror
ui.label('Code Mirror:')
editor = ui.codemirror('print("Edit me!")', language='Python').classes('h-32')
ui.select(editor.supported_languages, label='Language', clearable=True) \
    .classes('w-32').bind_value(editor, 'language')
ui.select(editor.supported_themes, label='Theme') \
    .classes('w-32').bind_value(editor, 'theme')

ui.separator()

# Number input
ui.label('Number Input:')
ui.number(label='Number', value=3.1415927, format='%.2f',
          on_change=lambda e: number_result.set_text(f'you entered: {e.value}'))
number_result = ui.label()
ui.separator()

# Knob
ui.label('Knob:')
knob = ui.knob(0.3, show_value=True)

with ui.knob(color='orange', track_color='grey-2').bind_value(knob, 'value'):
    ui.icon('volume_up')
ui.separator()

# Color Input
label = ui.label('Color Input: Change my color!')
ui.color_input(label='Color', value='#000000',
               on_change=lambda e: label.style(f'color:{e.value}'))
ui.separator()

# Color Picker
ui.label('Color Picker:')
with ui.button(icon='colorize') as button:
    ui.color_picker(on_pick=lambda e: button.classes(f'!bg-[{e.color}]'))
ui.separator()

# Date Picker
ui.label('Date Picker:')
ui.date(value='2025-02-01', on_change=lambda e: result.set_text(e.value))
result = ui.label()

date_input = ui.input('Date range').classes('w-40')
ui.date().props('range').bind_value(
    date_input,
    forward=lambda x: f'{x["from"]} - {x["to"]}' if x else None,
    backward=lambda x: {
        'from': x.split(' - ')[0],
        'to': x.split(' - ')[1],
    } if ' - ' in (x or '') else None,
)
ui.separator()

# Time Input
ui.label('Time Input:')
ui.time(value='12:00', on_change=lambda e: result.set_text(e.value))
result = ui.label()
ui.separator()

# File Upload
ui.label('File Upload:')
ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}')).classes('max-w-full')


with ui.dialog().props('full-width') as dialog:
    with ui.card():
        content = ui.markdown()

def handle_upload(e: events.UploadEventArguments):
    text = e.content.read().decode('utf-8')
    content.set_content(text)
    dialog.open()

ui.upload(on_upload=handle_upload).props('accept=.md').classes('max-w-full')

ui.separator()

#* Audio Visual Elements
ui.markdown('## Audio Visual Elements')

# Image
ui.label('Image:')
ui.image('https://picsum.photos/id/377/640/360')

# Captions and Overlays:By nesting elements inside a ui.image you can create augmentations
ui.label('Captions and Overlays:')
with ui.image('https://picsum.photos/id/29/640/360'):
    ui.label('Nice!').classes('absolute-bottom text-subtitle2 text-center')

with ui.image('https://cdn.stocksnap.io/img-thumbs/960w/airplane-sky_DYPWDEEILG.jpg'):
    ui.html('''
        <svg viewBox="0 0 960 638" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
        <circle cx="445" cy="300" r="100" fill="none" stroke="red" stroke-width="10" />
        </svg>
    ''').classes('w-full bg-transparent')

# Interactive Images
ui.label('Interactive Images:')
def mouse_handler(e: events.MouseEventArguments):
    color = 'SkyBlue' if e.type == 'mousedown' else 'SteelBlue'
    ii.content += f'<circle cx="{e.image_x}" cy="{e.image_y}" r="15" fill="none" stroke="{color}" stroke-width="4" />'
    ui.notify(f'{e.type} at ({e.image_x:.1f}, {e.image_y:.1f})')

src = 'https://picsum.photos/id/565/640/360'
ii = ui.interactive_image(src, on_mouse=mouse_handler, events=['mousedown', 'mouseup'], cross=True)

ui.separator()

# Audio Player
ui.label('Audio Player:')
a = ui.audio('https://cdn.pixabay.com/download/audio/2022/02/22/audio_d1718ab41b.mp3')
a.on('play', lambda _: ui.notify('Started'))
a.on('pause', lambda _: ui.notify('Paused'))
a.on('ended', lambda _: ui.notify('Completed'))

ui.button(on_click=lambda: a.props('muted'), icon='volume_off').props('outline')
ui.button(on_click=lambda: a.props(remove='muted'), icon='volume_up').props('outline')
ui.button('Jump to 0:02', on_click=lambda: a.seek(2))
ui.separator()

# Video Player
ui.label('Video Player:')
v = ui.video('https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4')
ui.button('Play', on_click=v.play)
ui.button('Pause', on_click=v.pause)
ui.button('Jump to 0:05', on_click=lambda: v.seek(5))
ui.separator()

# Icon
ui.label('Icon:')
ui.icon('thumb_up', color='primary').classes('text-5xl')
ui.separator()

# Material icons and symbols
ui.label('Material icons and symbols:')
with ui.row().classes('text-4xl'):
    ui.icon('home')
    ui.icon('o_home')
    ui.icon('r_home')
    ui.icon('sym_o_home')
    ui.icon('sym_r_home')
ui.separator()

# Lottie Files
ui.label('Lottie Files:')
ui.add_body_html('<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>')

src = 'https://assets5.lottiefiles.com/packages/lf20_MKCnqtNQvg.json'
ui.html(f'<lottie-player src="{src}" loop autoplay />').classes('w-24')

ui.separator()

#* Data Elements
ui.markdown('## Data Elements')

# Table
ui.label('Table:') 
columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
    {'name': 'age', 'label': 'Age', 'field': 'age', 'sortable': True},
]
rows = [
    {'name': 'Sohail', 'age': 22},
    {'name': 'Aniket', 'age': 21},
    {'name': 'Sohrab'},
]
ui.table(columns=columns, rows=rows, column_defaults={
    'align': 'left',
    'headerClasses': 'uppercase text-primary',
}, row_key='name')

ui.separator()

# AG Grid
ui.label('AG Grid:')
grid = ui.aggrid({
    'defaultColDef': {'flex': 1},
    'columnDefs': [
        {'headerName': 'Name', 'field': 'name'},
        {'headerName': 'Age', 'field': 'age'},
        {'headerName': 'Job Title', 'field': 'job'},
    ],
    'rowData': [
        {'name': 'Sohail', 'age': 22, 'job': 'Frontend Developer'},
        {'name': 'Aniket', 'age': 21, 'job': 'Backend Developer'},
        {'name': 'Sohrab', 'age': 24, 'job': 'Strapi Developer'},
    ],
    'rowSelection': 'multiple',
}).classes('max-h-40, w-50')

def update():
    grid.options['rowData'][0]['age'] += 1
    grid.update()

ui.button('Update', on_click=update)
ui.button('Select all', on_click=lambda: grid.run_grid_method('selectAll'))
ui.separator()

# Highlights Chart
ui.label('Highlights Chart:')
chart = ui.highchart({
    'title': False,
    'chart': {'type': 'bar'},
    'xAxis': {'categories': ['A', 'B']},
    'series': [
        {'name': 'Alpha', 'data': [0.1, 0.2]},
        {'name': 'Beta', 'data': [0.3, 0.4]},
    ],
}).classes('w-full h-64')

def update():
    chart.options['series'][0]['data'][0] = random()
    chart.update()

ui.button('Update', on_click=update)

ui.separator()

# Apache ECharts
ui.label('Apache ECharts:')
echart = ui.echart({
    'xAxis': {'type': 'value'},
    'yAxis': {'type': 'category', 'data': ['A', 'B'], 'inverse': True},
    'legend': {'textStyle': {'color': 'gray'}},
    'series': [
        {'type': 'bar', 'name': 'Alpha', 'data': [0.1, 0.2]},
        {'type': 'bar', 'name': 'Beta', 'data': [0.3, 0.4]},
    ],
})
def update():
    echart.options['series'][0]['data'][0] = random()
    echart.update()

ui.button('Update', on_click=update)
ui.separator()

# Pyplot Context : Create a context to configure a Matplotlib plot.
ui.label('Pyplot Context:')
with ui.pyplot(figsize=(3, 2)):
    x = np.linspace(0.0, 5.0)
    y = np.cos(2 * np.pi * x) * np.exp(-x)
    plt.plot(x, y, '-')
ui.separator()

# Line Plot
ui.label('Line Plot:')
line_plot = ui.line_plot(n=2, limit=20, figsize=(3, 2), update_every=5) \
    .with_legend(['sin', 'cos'], loc='upper center', ncol=2)
    
def update_line_plot() -> None:
    now = datetime.now()
    x = now.timestamp()
    y1 = math.sin(x)
    y2 = math.cos(x)
    line_plot.push([now], [[y1], [y2]], y_limits=(-1.5, 1.5))

line_updates = ui.timer(0.1, update_line_plot, active=False)
line_checkbox = ui.checkbox('active').bind_value(line_updates, 'active')
ui.separator()

# Linear and Circular Progress
ui.label('Linear and Circular Progress:')
slider = ui.slider(min=0, max=1, step=0.01, value=0.5)
ui.linear_progress().bind_value_from(slider, 'value')
ui.circular_progress().bind_value_from(slider, 'value')
ui.separator()

# Spinner
ui.label('Spinner:')
with ui.row():
    ui.spinner(size='lg')
    ui.spinner('audio', size='lg', color='green')
    ui.spinner('dots', size='lg', color='red')
ui.separator()

# Leaflet Map
ui.label('Leaflet Map:')
m = ui.leaflet(center=(19.0760, 72.8777))
ui.label().bind_text_from(m, 'center', lambda center: f'Center: {center[0]:.3f}, {center[1]:.3f}')
ui.label().bind_text_from(m, 'zoom', lambda zoom: f'Zoom: {zoom}')

with ui.grid(columns=2):
    ui.button('Mumbai', on_click=lambda: m.set_center((19.0760, 72.8777)))
    ui.button('Mumbra', on_click=lambda: m.set_center((19.1900, 73.0229)))
    ui.button('Pune', on_click=lambda: m.set_center((18.5204, 73.8567)))
    ui.button('Delhi', on_click=lambda: m.set_center((28.7041, 77.1025)))
    ui.button('Chennai', on_click=lambda: m.set_center((13.0827, 80.2707)))
    ui.button('Kolkata', on_click=lambda: m.set_center((22.5726, 88.3639)))
    ui.button(icon='zoom_in', on_click=lambda: m.set_zoom(m.zoom + 1))
    ui.button(icon='zoom_out', on_click=lambda: m.set_zoom(m.zoom - 1))

# Tree
ui.label('Tree:')
ui.tree([
    {'id': 'numbers', 'children': [{'id': '1'}, {'id': '2'}]},
    {'id': 'letters', 'children': [{'id': 'A'}, {'id': 'B'}]},
], label_key='id', on_select=lambda e: ui.notify(e.value))
ui.separator()

# Log View
ui.label('Log View:')
log = ui.log(max_lines=10).classes('w-full h-20')
ui.button('Log time', on_click=lambda: log.push(datetime.now().strftime('%X.%f')[:-5]))
ui.separator()

# Editor
ui.label('Editor:')
editor = ui.editor(placeholder='Type something here')
ui.markdown().bind_content_from(editor, 'value',
                                backward=lambda v: f'HTML code:\n```\n{v}\n```')

ui.separator()

# Code
ui.label('Code:')
ui.code('''
    from nicegui import ui

    ui.label('Hello Sohail!')

    ui.run()
''').classes('w-full')
ui.separator()

# JSONEditor
ui.label('JSONEditor:')
json = {
    'array': [1, 2, 3],
    'boolean': True,
    'color': '#82b92c',
    None: None,
    'number': 123,
    'object': {
        'a': 'b',
        'c': 'd',
    },
    'time': 1575599819000,
    'string': 'Hello Sohail',
}
ui.json_editor({'content': {'json': json}},
               on_select=lambda e: ui.notify(f'Select: {e}'),
               on_change=lambda e: ui.notify(f'Change: {e}'))
ui.separator()


#* Page Layout
ui.markdown('## Page Layout')

# Card
ui.label('Card:')
with ui.card().tight():
    ui.image('https://picsum.photos/id/684/640/360')
    with ui.card_section():
        ui.label('Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...')
ui.separator()

# Column
ui.label('Column:')
with ui.column():
    ui.label('label 1')
    ui.label('label 2')
    ui.label('label 3')
ui.separator()

# Row 
ui.label('Row:')
with ui.row():
    ui.label('label 1')
    ui.label('label 2')
    ui.label('label 3')
ui.separator()

# Grid Element
ui.label('Grid Element:')
with ui.grid(columns=2):
    ui.label('Name:')
    ui.label('Tom')

    ui.label('Age:')
    ui.label('42')

    ui.label('Height:')
    ui.label('1.80m')
ui.separator()

# List
ui.label('List:')
with ui.list().props('dense separator'):
    ui.item('3 Apples')
    ui.item('5 Bananas')
    ui.item('8 Strawberries')
    ui.item('13 Walnuts')
ui.separator()

# Clear Containers
ui.label('Clear Containers:')
container = ui.row()

def add_face():
    with container:
        ui.icon('face')
add_face()

ui.button('Add', on_click=add_face)
ui.button('Remove', on_click=lambda: container.remove(0) if list(container) else None)
ui.button('Clear', on_click=container.clear)
ui.separator()

# Teleport
ui.label('Teleport:')
markdown = ui.markdown('Enter your **name**!')

def inject_input():
    with ui.teleport(f'#c{markdown.id} strong'):
        ui.input('name').classes('inline-flex').props('dense outlined')

ui.button('inject input', on_click=inject_input)
ui.separator()

# Scroll Area
ui.label('Scroll Area:')
with ui.row():
    with ui.scroll_area().classes('w-32 h-32 border'):
        ui.label('I scroll. ' * 20)
    with ui.column().classes('p-4 w-32 h-32 border'):
        ui.label('I will not scroll. ' * 10)
ui.separator()

# Space
ui.label('Space:')
with ui.row().classes('w-full border'):
    ui.label('Left')
    ui.space()
    ui.label('Right')

ui.separator()

# Skeleton
ui.label('Skeleton:')
ui.skeleton().classes('w-full')
ui.skeleton().classes('w-32 h-32')
ui.separator()

# Splitter
ui.label('Splitter:')
with ui.splitter() as splitter:
    with splitter.before:
        ui.label('This is some content on the left hand side.').classes('mr-2')
    with splitter.after:
        ui.label('This is some content on the right hand side.').classes('ml-2')

ui.separator()

# Tabs
ui.label('Tabs:')
with ui.tabs().classes('w-full') as tabs:
    one = ui.tab('One')
    two = ui.tab('Two')
with ui.tab_panels(tabs, value=two).classes('w-full'):
    with ui.tab_panel(one):
        ui.label('First tab')
    with ui.tab_panel(two):
        ui.label('Second tab')

ui.separator()

# Stepper
ui.label('Stepper:')
with ui.stepper().props('vertical').classes('w-full') as stepper:
    with ui.step('Preheat'):
        ui.label('Preheat the oven to 350 degrees')
        with ui.stepper_navigation():
            ui.button('Next', on_click=stepper.next)
    with ui.step('Ingredients'):
        ui.label('Mix the ingredients')
        with ui.stepper_navigation():
            ui.button('Next', on_click=stepper.next)
            ui.button('Back', on_click=stepper.previous).props('flat')
    with ui.step('Bake'):
        ui.label('Bake for 20 minutes')
        with ui.stepper_navigation():
            ui.button('Done', on_click=lambda: ui.notify('Yay!', type='positive'))
            ui.button('Back', on_click=stepper.previous).props('flat')

ui.separator()

# Timeline
ui.label('Timeline:')
with ui.timeline(side='right'):
    ui.timeline_entry('Rodja and Falko start working on NiceGUI.',
                      title='Initial commit',
                      subtitle='May 07, 2021')
    ui.timeline_entry('The first PyPI package is released.',
                      title='Release of 0.1',
                      subtitle='May 14, 2021')
    ui.timeline_entry('Large parts are rewritten to remove JustPy '
                      'and to upgrade to Vue 3 and Quasar 2.',
                      title='Release of 1.0',
                      subtitle='December 15, 2022',
                      icon='rocket')

ui.separator()

# Carousel
ui.label('Carousel:')

with ui.carousel(animated=True, arrows=True, navigation=True).props('height=180px'):
    with ui.carousel_slide().classes('p-0'):
        ui.image('https://picsum.photos/id/30/270/180').classes('w-[270px]')
    with ui.carousel_slide().classes('p-0'):
        ui.image('https://picsum.photos/id/31/270/180').classes('w-[270px]')
    with ui.carousel_slide().classes('p-0'):
        ui.image('https://picsum.photos/id/32/270/180').classes('w-[270px]')

ui.separator()
# Pagination

ui.label('Pagination:')
p = ui.pagination(1, 5, direction_links=True)
ui.label().bind_text_from(p, 'value', lambda v: f'Page {v}')
ui.separator()

# Menu
ui.label('Menu:')
with ui.row().classes('w-full items-center'):
    result = ui.label().classes('mr-auto')
    with ui.button(icon='menu'):
        with ui.menu() as menu:
            ui.menu_item('Menu item 1', lambda: result.set_text('Selected item 1'))
            ui.menu_item('Menu item 2', lambda: result.set_text('Selected item 2'))
            ui.menu_item('Menu item 3 (keep open)',
                         lambda: result.set_text('Selected item 3'), auto_close=False)
            ui.separator()
            ui.menu_item('Close', menu.close)
ui.separator()

# Tooltip
ui.label('Tooltip:')
ui.button('Hover me').tooltip('This is a tooltip')

with ui.button(icon='thumb_up'):
    ui.tooltip('I like this').classes('bg-green')
ui.separator()

# Notification
ui.label('Notification:')
ui.button('Say hi!', on_click=lambda: ui.notify('Hi!', close_button='OK'))
ui.separator()

# Notification with Actions
ui.label('Notification with Actions:')
async def compute():
    n = ui.notification(timeout=None)
    for i in range(10):
        n.message = f'Computing {i/10:.0%}'
        n.spinner = True
        await asyncio.sleep(0.2)
    n.message = 'Done!'
    n.spinner = False
    await asyncio.sleep(1)
    n.dismiss()

ui.button('Compute', on_click=compute)
ui.separator()

# Dialog
ui.label('Dialog:')
with ui.dialog() as dialog, ui.card():
    ui.label('Hello Sohail!')
    ui.button('Close', on_click=dialog.close)

ui.button('Open a dialog', on_click=dialog.open)
ui.separator()

#* Styling and Apperance
ui.markdown('## Styling and Apperance')

# Styling
ui.label('Styling:')
ui.radio(['x', 'y', 'z'], value='x').props('inline color=green')
ui.button(icon='touch_app').props('outline round').classes('shadow-lg')
ui.label('Stylish!').style('color: #6E93D6; font-size: 200%; font-weight: 300')
ui.separator()

# TailwindCSS
ui.label('TailwindCSS:')
ui.label('Label A').tailwind.font_weight('extrabold').text_color('blue-600').background_color('orange-200')
ui.label('Label B').tailwind('drop-shadow', 'font-bold', 'text-green-600')

red_style = Tailwind().text_color('red-600').font_weight('bold')
label_c = ui.label('Label C')
red_style.apply(label_c)
ui.label('Label D').tailwind(red_style)

ui.separator()

# Color Theming
ui.label('Color Theming:')
ui.button('Default', on_click=lambda: ui.colors())
ui.button('Gray', on_click=lambda: ui.colors(primary='#555'))

ui.separator()

# Dark or Light Mode
ui.label('Dark or Light Mode:')
dark = ui.dark_mode()
ui.label('Switch mode:')
ui.button('Dark', on_click=dark.enable)
ui.button('Light', on_click=dark.disable)
ui.separator()


#* Action and Events
ui.markdown('## Action and Events')

# Timer
ui.label('Timer:')
label = ui.label()
ui.timer(1.0, lambda: label.set_text(f'{datetime.now():%X}'))

ui.separator()

# UI Updates
ui.label('UI Updates:')
chart = ui.echart({
    'xAxis': {'type': 'value'},
    'yAxis': {'type': 'value'},
    'series': [{'type': 'line', 'data': [[0, 0], [1, 1]]}],
})

def add():
    chart.options['series'][0]['data'].append([random(), random()])
    chart.update()

def clear():
    chart.options['series'][0]['data'].clear()
    ui.update(chart)

with ui.row():
    ui.button('Add', on_click=add)
    ui.button('Clear', on_click=clear)

ui.separator()

# Async Event Handlers
ui.label('Async Event Handlers:')
async def async_task():
    ui.notify('Asynchronous task started')
    await asyncio.sleep(5)
    ui.notify('Asynchronous task finished')

ui.button('start async task', on_click=async_task)

ui.separator()


ui.run(title="Digital Salt")



