const fname = 'wordlist_processing/wordlist_major.json'

let currentWord,
    currentNums,
    globalWordList;


async function loadWordList() {
    const response = await fetch(fname);
    return await response.json();
}

loadWordList()
    .then(response => setup(response))
    .catch(error => console.error(error))

async function setup(wordList) {
    globalWordList = wordList
    getNewWord()
}
async function getNewWord() {
    let keys = Object.keys(globalWordList)
    let idx = Math.floor(Math.random() * keys.length);
    let nums = globalWordList[keys[idx]]

    currentWord = keys[idx]
    currentNums = nums
    document.getElementById('currentWord').innerText = keys[idx]
    document.getElementById('numInput').value = ""
}


function checkAnswer(value) {
    if (value === currentNums) {
        console.log("Correct!")
        getNewWord()

    }
}