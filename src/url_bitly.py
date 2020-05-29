from bitlyshortener import Shortener # install bitlyshortener 

tokens_pool = ['4b933f79f3b8a6cef677c2a660488f0460fde8c5']  # SHIVAM ACCESS TOKEN 
shortener = Shortener(tokens=tokens_pool, max_cache_size=8192)
def link_shortner(urls): # urls -> list return -> list

    res = shortener.shorten_urls(urls)
    return res
