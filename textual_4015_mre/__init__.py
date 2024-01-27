from typing import cast

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, ListItem, Label


class DemoApp(App):
    def compose(self) -> ComposeResult:
        list_item = ListItem(
            Label("Hello")
        )
        cast(Label, list_item.children[0]).update("Hello World!")
        yield list_item


if __name__ == "__main__":
    app = DemoApp()
    app.run()
