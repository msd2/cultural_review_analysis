import requests
from requests import api
from settings import api_key
import pandas as pd


def search_articles(search_term, api_key, page=1, tag=0):
    '''
    Searches the OP and returns json results.

    inputs
        search_term: string, what to search for
        page: int, which page of results to return
        api_key: string
    outputs
        results: dictionary of results
    '''
    if tag==0:
        r = requests.get(f'https://content.guardianapis.com/search?page={page}&q={search_term}&show-fields=body&api-key={api_key}')
    else:
        r = requests.get(f'https://content.guardianapis.com/search?page={page}&q={search_term}&tag={tag}&show-fields=body&api-key={api_key}')
    results = r.json()['response']['results']
    return results


results = search_articles(search_term='review', tag='film/film', page=2, api_key=api_key)

# print(results[0].keys())

print(results)