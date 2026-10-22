from abc import ABC, abstractmethod
from typing import Callable, Any

ProgressCallback = Callable[[int, int, str], None] #current, total, message

class BaseTask(ABC):
    @abstractmethod
    def execute(self, report_progress: ProgressCallback) -> Any:
        raise NotImplementedError #base execute method that all tasks must implement

