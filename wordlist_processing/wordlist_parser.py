import json
from tqdm import tqdm
import parse
import os
import random
from eng_to_ipa import convert

TRANSLATE_FNAME = r'C:\Users\tobyb\OneDrive\Documents\JavaScript\JavaScriptProjects\major-system\data\major_translate.json'
with open(TRANSLATE_FNAME, 'r', encoding='utf-8') as infile:
	json_file = json.load(infile)
	TRANSLATE = {int(k): v for k, v in json_file.items()}
	TRANSLATE_REVERSED = {i: key for key, sub in json_file.items() for i in sub} # unpack all


def get_word_list():
	cwd = os.getcwd()
	fname = os.path.join(cwd, 'wordlist.txt')
	with open(fname, 'r') as infile:
		words = [line.rstrip() for line in infile.readlines()]

	return words


def word_to_nums(ipa):
	"""Convert ipa pronounciation of word to Major system numbers
	Special case for tʃ, dʒ as each are two characters long"""
	if ipa is None: return ''
	nums = ''
	ipa = ipa.replace('tʃ', 'ʃ').replace('dʒ', 'ʒ')
	for i, c in enumerate(ipa):
		if c in TRANSLATE_REVERSED:
			nums += TRANSLATE_REVERSED[c]
	return nums


def write_wordlist_ipa(overwrite=True):
	# min/max count of numbers
	min_length = 2
	max_length = 5

	words = get_word_list()
	words = random.sample(words, 100)
	major_dict = {}
	with tqdm(words) as tqdm_it:
		for n, word in enumerate(tqdm_it):
			ipa = convert(word)
			nums = word_to_nums(ipa)
			# don't save this value if too many/few numbers
			if '*' not in ipa and min_length <= len(nums) <= max_length:
				major_dict[word] = nums

	# save the dictionary to a json file
	out_fname = 'wordlist_major.json'
	with open(out_fname, 'r', encoding='utf-8') as outfile:
		old_dict = json.load(outfile)
		old_dict.update(major_dict)

	if overwrite:
		old_dict = major_dict

	with open(out_fname, 'w', encoding='utf-8') as outfile:
		json.dump(old_dict, outfile,
				  indent=4, sort_keys=True, ensure_ascii=False)


def gen_cmu_wordlist():
	in_fname = 'CMU_dict.json'
	out_fname = 'cmu_wordlist.txt'

	with open(in_fname, 'r') as infile:
		cmu_dict = json.load(infile)

	words = [word + '\n' for word in cmu_dict.keys() if word.isalpha()]
	with open(out_fname, 'w') as outfile:
		outfile.writelines(words, )


if __name__ == '__main__':
	gen_cmu_wordlist()