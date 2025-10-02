from cProfile import label
from components import button
from oneforall.app import App, Window
from oneforall.components import Container, Text, Button

# Create main app
app = App()
window = Window()

container = Container(className="p-4")
container2 = Container(className="flex gap-2")

msg = app.use_state('msg', )

# Add a simple text
text = Text("Welcome to OneForAll!", className="text-xl font-bold")
container.add(text)
container.add(container2)

# Add a button
def greet(name, time):
    text.text = "Button clicked"
    print(f"Button clicked! Hello, {name} at {time}")

button1 = button.my_button(label="Click me", on_click=lambda: greet("User", "10:00AM"))
container2.add(button1)
button2 = button.my_button(label="Click me too", className="bg-black", on_click=lambda: print("New button clicked"))
container2.add(button2)



window.add_child(container)
app.windows.append(window)

# Run the app in dev mode to see Tailwind CDN effects
if __name__ == "__main__":
    app.run(dev_mode=True)
