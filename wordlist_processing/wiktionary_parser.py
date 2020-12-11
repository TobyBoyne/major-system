from urllib import request
import json
import re
import parse

import os

url = 'https://en.wikipedia.org/w/api.php?action=query&format=json&prop=categories%7Cpageviews&generator=allpages&formatversion=2&gapfrom=Ba&gaplimit=10'
url = 'https://en.wiktionary.org/w/api.php?action=query&format=json&prop=categories%7Cpageviews&generator=allpages&formatversion=2&gapfrom=Team&gaplimit=10'
BASE_URL = 'https://en.wiktionary.org/w/api.php?action=parse&format=json'

PATTERN = parse.compile(r'{}<span class="IPA">{pronounciation}</span>{}')

TRANSLATE_FNAME = r'C:\Users\tobyb\OneDrive\Documents\JavaScript\JavaScriptProjects\major-system\data\major_translate.json'
with open(TRANSLATE_FNAME, 'r') as infile:
	json_file = json.load(infile)
	TRANSLATE = {int(k): v for k, v in json_file.items()}
	ALL_CONSTS = {i: key for key, sub in json_file.items() for i in sub} # unpack all

print(TRANSLATE)
print(ALL_CONSTS)

def get_request(url):
	raw_data = request.urlopen(url).read()
	data = json.loads(raw_data)

	# print response
	# print(json.dumps(data, indent=4))

	return data

def get_word_list():
	cwd = os.getcwd()
	fname = os.path.join(cwd, 'wordlist.txt')
	with open(fname, 'r') as infile:
		words = [line.rstrip() for line in infile.readlines()]

	return words


def get_pronunciation(json_response):
	if 'error' in json_response:
		return None
	text = json_response['parse']['text']['*']
	pronounce = PATTERN.parse(text)
	if pronounce is None:
		return None
	return pronounce['pronounciation']


if __name__ == '__main__':
	words = get_word_list()[:10]
	words = ['xstsxx', 'ability']
	for word in words:
		url = f'{BASE_URL}&sectiontitle=Pronounciation&page={word}'
		response = get_request(url)
		print(get_pronunciation(response))

		# TODO: Count number of constanants