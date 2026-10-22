import deezer as dz
from itertools import islice

def search(query: str, limit: int = 25) -> deezer.pagination.PaginatedList:
    client = dz.Client()
    results = client.search_albums(query)
    return list(islice(results, limit))

if __name__ == "__main__":
    print(search(query="Hayley Williams")[0].title)

