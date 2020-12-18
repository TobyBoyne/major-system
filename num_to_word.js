/**
 * Script for highlighting numbers, and suggesting words
 * https://codersblock.com/blog/highlight-text-inside-a-textarea/#:~:text=You%20can%27t%20actually%20highlight,JavaScript%2C%20you%20can%20fake%20it.
 */

function selectText(textarea) {
    const fullText = textarea.value
    const num = window.getSelection().toString()
    const start = textarea.selectionStart
    const end = textarea.selectionEnd
    console.log(start, end)
    console.log(num)

    var highlightedText = applyHighlights(fullText, start, end);
    $('highlights').innerHTML = highlightedText;
    console.log($('highlights').innerHTML)
}




function handleInput() {
    var text = $('numberTextarea').value;

}

function applyHighlights(text, start, end) {
    text = text
        .replace(/\n$/g, '\n\n')
    text = text.slice(0, start)
        + '<mark>'
        + text.slice(start, end)
        + '</mark>'
        + text.slice(end, text.length)
    return text.replace(/ /g, ' <br>')
}

function handleScroll() {
  var scrollTop = $('numberTextarea').scrollTop;
  $('backdrop').scrollTop = scrollTop;
}