from nicegui import ui
from sections import footer

# using CSS
with ui.row().style("flex-wrap:nowrap; width:100vw"):
    ui.image("https://images.pexels.com/photos/30697854/pexels-photo-30697854.jpeg").style("width: 200px")
    ui.label("Hello Python!")
    ui.element("div").style('height:200px; width: 200px; background-color: red; border-radius:15px')

    
# using Tailwind
with ui.column():
    # ui.button("Click me").style("color: blue; font-size:2rem; font-style:italic")
    #why is the numbers not working for buttons
    ui.button("Click me",color="fuchsia-600",).props('push text-color=white').tooltip("Click me").tailwind("text-5xl hover:bg-pink-500")


    ui.select([1, 2, 3, 4])

# with ui.element('div').classes('p-8 bg-gray-100'):
#     ui.element('button', ).classes(
#         'bg-fuchsia-600 text-white px-4 py-2 rounded-lg hover:bg-pink-500 text-2xl'
#     ).props('id=my-btn').inner_html('Click Me')

# ui.element('h1', ).classes('text-4xl font-bold text-fuchsia-600').inner_html('This is H1')




footer.render()


# Always call ui.run(), but use this condition for multiprocessing
if __name__ in {"__main__", "__mp_main__"}:
    ui.run()
