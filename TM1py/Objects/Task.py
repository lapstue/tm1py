import json
from typing import List, Dict
from enum import Enum
from TM1py.Objects.TM1Object import TM1Object

class ExecutableType(Enum):
     PROCESS = 'Process'
     CHORE = 'Chore'

class Task(TM1Object):
    def _init_(self, task_name: str, executable_type: ExecutableType, executable: str, parameters: str, dependencies: str ):
        self.task_name = task_name
        self.executable_type = executable_type
        self.executable = executable
        if ExecutableType == 'Process':
            self.parameters = parameters
        else:
             self.parameters = None

        self.dependencies = dependencies

    def task_name(self) -> str:
        return self.task_name

    def executable_type(self) -> ExecutableType:
        return self.executable_type

    def exexutable(self) -> str:
        return self.executable

    def parameters(self) -> str:
        return self.parameters

    def dependencies(self) -> List[str]:
        return self.dependencies