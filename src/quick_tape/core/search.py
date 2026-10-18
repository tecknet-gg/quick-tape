import deezer as dz
from quick_tape.ui.components.release_card import ReleaseCard


def search(query: str) -> deezer.pagination.PaginatedList:
    client = dz.Client()
    query = f"{query}"
    results = client.search_albums(query)
    results = [result for result in results]
    return results[0:25]


if __name__ == "__main__":
    print(search(query="Hayley Williams")[0].title)

