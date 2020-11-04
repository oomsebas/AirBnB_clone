#!/usr/bin/python3
""" init file to create a unique instance of filestorage """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
