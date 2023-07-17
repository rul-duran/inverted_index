from services.openalex import getRandomWork
from utils.inverted_index import inverted_index_to_text

# get a random job from the openalex api
work = getRandomWork()

# if the api returns a job with no inverse index, we get a new one
while (not work['abstract_inverted_index']):
    print('Inveted index is None, getting another work...')
    work = getRandomWork()

# the inverted index is converted to its original text form
print(inverted_index_to_text(work['abstract_inverted_index']))
