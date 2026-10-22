from quick_tape.core.jobs.base import BaseTask, ProgressCallback
from quick_tape.core.utilities.resolver import resolve_release

class ResolveTask(BaseTask):
    def __init__(self, release):
        self.release = release

    def execute(self, report_progress: ProgressCallback):
        resolved_tracks = []
        for index, total, resolved_track in resolve_release(self.release):
            resolved_tracks.append(resolved_track)
            report_progress(index, total, f"Resolving track: {resolved_track.source_track.title}")
        return resolved_tracks