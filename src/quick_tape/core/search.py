import deezer as dz

def search(release: str, artist: str | None=None):
    with dz.Client() as client:
        query = f"{release} {artist}"
        results = client.search_albums(query)
        return [result for result in results]

if __name__ == "__main__":
    print(search("Oh Inverted World", "The Shins"))