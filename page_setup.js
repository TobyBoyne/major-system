const fname = 'wordlist_processing/wordlist_major.json'

let wordToNumDict,
    numToWordDict

//TODO: create and read num to word dictionary

async function loadWordList() {
    const response = await fetch(fname);
    return await response.json();
}

loadWordList()
    .then(response => setup(response))
    .catch(error => console.error(error))

async function setup(wordList) {
    wordToNumDict = wordList
    getNewWord()
}