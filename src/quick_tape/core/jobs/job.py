from dataclasses import dataclass, field
from enum import Enum
from uuid import uuid4

from quick_tape.core.jobs.base import BaseTask


class JobStatus(Enum):
    QUEUED = "Queued"
    RUNNING = "Running"
    COMPLETED = "Completed"
    FAILED = "Failed"
    CANCELLED = "Cancelled"

@dataclass
class Job:
    name: str
    task: BaseTask
    id: str = field(default_factory=lambda: str(uuid4()))
    status = JobStatus.QUEUED
    progress: int = 0
    total: int = 0
    message: str = "Queued"
    error: str | None = None
    results: list = field(default_factory=list)