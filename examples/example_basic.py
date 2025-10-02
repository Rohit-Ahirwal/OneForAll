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



window.add_child(container)
app.windows.append(window)

# Run the app in dev mode to see Tailwind CDN effects
if __name__ == "__main__":
    app.run(dev_mode=True)
