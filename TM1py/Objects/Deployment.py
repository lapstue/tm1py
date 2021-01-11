import json
from typing import List, Dict

from TM1py.Objects.TM1Object import TM1Object
from Tm1py.Objects.Task import Task

class Deployment(TM1Object):
    def _init_(self, files: List[str], ignore: List[str], tasks: List[Task], prepull: List[Task], postpull: List[Task], prepush: List[Task], postpush: List[Task] ):
        self.files = files
        self.ignore = ignore
        self.tasks = tasks
        self.prepull = prepull
        self.postpull = postpull
        self.prepush = prepush
        self.postpush = postpush


    def files(self) -> List[str]:
        return self.files

    def ignore(self) -> List[str]:
        return self.ignore

    def tasks(self) -> List[Task]:
        return self.tasks

    def prepull(self) -> List[Task]:
        return self.prepull

    def postpull(self) -> List[Task]:
        return self.postpull

    def prepush(self) -> List[Task]:
        return self.prepush

    def postpush(self) -> List[Task]:
        return self.postpush

    def to_dict(self) -> Dict:
        output = {}
        if self.files != None:
            output['Files'] = self.files
        if self.ignore != None:
            output['Ignore'] = self.ignore
        if self.prepull != None:
            output['PrePull'] = self.prepull
        if self.postpull != None:
            output['PostPull'] = self.postpull
        if self.prepush != None:
            output['PrePush'] = self.prepush
        if self.postpush != None:
            output['PostPush'] = self.postpush
        if self.tasks != None:
            #TODO: loop through tasks and add their dictionary representation to the output
            pass
        return output