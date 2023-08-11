#!usr/bin/python3
"""this instance of theFileStorage class
initializes tyhe package.
"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
