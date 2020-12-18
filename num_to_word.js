/**
 * Script for highlighting numbers, and suggesting words
 */


function selectText(textarea) {
    const num = window.getSelection().toString()
    const start = textarea.selectionStart
    const end = textarea.selectionEnd
    console.log(start, end)
    console.log(num)
    $('.numInput').highlightWithinTextarea({
        highlight: [start, end]
    })
}