# Mesa

Develop applications with ease, without the hassle of dealing with pre-defined styles. Total control down to the pixel.

## Get Started

```bash
pip install mesa
```

## Basic Window

```py
class MainScene(MesaScene):
    def __init__(self, core, scene_name, manager) -> None:
        super().__init__(core, scene_name, manager)
        self.set_background_color("black")
        self.container = MesaStackVertical(self)
        self.container.set_as_core()
        self.container.build()

class MyApplication(MayaaCore):
    def __init__(self) -> None:
        super().__init__()
        self.set_application_name("MyApp")
        self.set_rendering_flags(pg.SRCALPHA)
        self.set_display_size(360, 600)
        self.set_background_color("black")
        self.set_clock(60)
        self.main_scene = MainScene(self, "main", self.scene_manager)
        self.scene_manager.set_init_scene("main")

app = MyApplication()
app.run()

```
