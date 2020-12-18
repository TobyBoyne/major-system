const fname = 'wordlist_processing/wordlist_major.json'

let wordToNumDict,
    numToWordDict

function $(x) {return document.getElementById(x);}

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

//    setup num_to_word
    const textarea = $('numberTextarea');
    textarea.oninput = handleInput
    textarea.onscroll = handleScroll
}