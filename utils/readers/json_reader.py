import json
from typing import Any

from utils.readers.base_reader import BaseReader


class JSONReader(BaseReader):
    def read(self,filepath, **kwargs:Any)->list[dict]:
        self.validate(filepath,**kwargs)
        with open(filepath,mode="r",encoding="UTF-8") as Jsonfile:
            reader = json.load(Jsonfile)
            return list(reader)

    def validate(self, filepath, **kwargs:Any)->None:
        if not filepath.exists():
            raise FileNotFoundError(f"{filepath} does not exist")

        if filepath.suffix.lower() != ".json":
            raise ValueError(f"{filepath} is not a json file")


