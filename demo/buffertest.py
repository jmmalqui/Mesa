import sys
import os

root_dir = "/".join(os.path.abspath(__file__).replace("\\", "/").split("/")[:-2])
sys.path.insert(1, os.path.join(root_dir, "src"))
import mayaa


buffer = mayaa.TextBuffer()
buffer.add("c")
buffer.shift_right()
buffer.add("a")
buffer.shift_left()
buffer.add("t")
print(buffer.buffer)
buffer.pop()
print(buffer.buffer)
