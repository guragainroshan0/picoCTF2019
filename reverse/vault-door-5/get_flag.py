from base64 import *
from urllib.parse import unquote
data="JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTMwJTY2JTMzJTMwJTM5JTY0JTM0JTMw"
print(unquote(b64decode(data).decode()))
