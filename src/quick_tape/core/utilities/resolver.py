import yt_dlp
from dataclasses import dataclass
from search import search # temporary testing import

def resolve_release(release: {tracklist, artist}) -> list:
    tracklist_paginated = release.get_tracks()
    tracklist = []

    artist = release.get_artist().name

    for track in tracklist_paginated: #extract paginated tracks
        print(track.title)
        tracklist.append(track)

    with yt_dlp.YoutubeDL() as ydl:
        for index, track in enumerate(tracklist):
            query = f"{artist}-{track.title}"
            try:
                results = ydl.extract_info(f"ytsearch1:{query}", download=False)
                entry = (next(entry for entry in results.get("entries", []) if entry), None)

                if video is None:
                    resolved = ResolvedTrack(
                        source_track=track,
                        download_url=None,
                        matched_title=None,
                        matched_duration=None,
                        actual_title=track.title,
                        actual_duration=track.duration,
                        status="track_not_found"
                    )
                else:
                    resolved = ResolvedTrack(
                        source_track=track,
                        download_url=video.get("webpage_url") or video.get("url"),
                        matched_title = video.get("title"),
                        matched_duration=video.get("duration"),
                        actual_title=track.title,
                        actual_duration=track.duration,
                        status="track_found"
                    )

            except Exception as e:
                resolved = ResolvedTrack(
                    source_track=track,
                    download_url=None,
                    matched_title=None,
                    matched_duration=None,
                    actual_title=track.title,
                    actual_duration=track.duration,
                    status="failed_to_resolve",
                    error=str(e)
                )

            yield (index+1), len(tracklist), resolved

@dataclass
class ResolvedTrack:
    source_track: object
    download_url: str | None
    matched_title: str | None
    matched_duration: str | None
    actual_title: str | None
    actual_duration: str | None
    status: str | None
    error: str | None = None




if __name__ == "__main__":

    release = search(query="Hayley Williams")[0]
    resolve_release(release)

    for index, total, result in resolve_release(release):
        print(f"[{index}/{total}] {result.source_track.title}")

        if result.status == "matched":
            print(f"YouTube: {result.matched_title}")
            print(f"URL: {result.url}")
        else:
            print(f"Resolution status: {result.status}")
