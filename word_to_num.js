let currentWord,
    currentNums;

function getNewWord() {
    let keys = Object.keys(wordToNumDict)
    let idx = Math.floor(Math.random() * keys.length);
    let nums = wordToNumDict[keys[idx]]

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