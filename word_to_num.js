const fname = 'wordlist_processing/wordlist_major.json'

async function loadWordlist() {
    const response = await fetch(fname);
    return await response.json();
}

loadWordlist()
    .then(response => testWord(response))
    .catch(error => console.error(error))


async function testWord(wordList) {
    console.log(wordList)
    let keys = Object.keys(wordList)
    let idx = Math.floor(Math.random() * keys.length);
    console.log(idx);
    let nums = wordList[keys[idx]]
    document.getElementById('currentWord').innerText = keys[idx]
    document.getElementById('correctNums').innerText = nums
}
