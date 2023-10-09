import sys
import os

root_dir = "/".join(os.path.abspath(__file__).replace("\\", "/").split("/")[:-2])
sys.path.insert(1, os.path.join(root_dir, "src"))

import mayaa


class ImageApp(mayaa.MayaaCore):
    def __init__(self) -> None:
        super().__init__()
        self.set_application_name("Image in Mayaa")
        self.set_background_color(mayaa.MayaaColors.ALICEWHITE)


app = ImageApp()
app.run()
