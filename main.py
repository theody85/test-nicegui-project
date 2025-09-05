from nicegui import ui
from sections import footer

# using CSS
with ui.row().style("flex-wrap:nowrap; width:100vw"):
    ui.image("https://images.pexels.com/photos/30697854/pexels-photo-30697854.jpeg").style("width: 200px")
    ui.label("Hello Python!")
    ui.element("div").style('height:200px; width: 200px; background-color: red; border-radius:15px')

    
# using Tailwind
with ui.column():
    ui.button("Click me",color="fuchsia-600",).props('push text-color=white').tooltip("Click me").tailwind("text-5xl hover:bg-pink-500")


    ui.select([1, 2, 3, 4])




footer.render()




ui.run()
