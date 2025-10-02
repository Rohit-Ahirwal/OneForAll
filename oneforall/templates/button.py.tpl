from oneforall.components import Button

variants = {
    "primary": "bg-indigo-500 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded cursor-pointer",
    "secondary": "bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded cursor-pointer",
    "danger": "bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded cursor-pointer",
    "link": "text-blue-500 hover:underline font-bold py-2 px-4 rounded cursor-pointer",
}

def {{name}}(label: str = "{{name}}", variant: str = "primary", on_click=None, className: str =""):
    return Button(
        f"{label}",
        on_click=on_click,
        className=className,
        default_class=variants.get(variant, "primary")
    )
