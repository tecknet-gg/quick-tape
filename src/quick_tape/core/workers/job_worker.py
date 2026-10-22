from PySide6.QtCore import QObject, Signal, Slot

class JobWorker(QObject):
    progress = Signal(int, int, str)
    completed = Signal(str, object)
    failed = Signal(str, str)
    finished = Signal()

    def __init__(self, job):
        super().__init__()
        self.job = job

    @Slot
    def run(self):
        try:
            result = self.job.task.execute(
                report_progress=lambda current, total, message:
                    self.progress.emit(
                        self.job.id,
                        current,
                        total,
                        message,
                    )
            )
            self.completed.emit(self.job.id, result)
        except Exception as e:
            self.failed.emit(self.job.id, str(e))




