let catFact = '';
const url = 'https://cat-fact.herokuapp.com/facts/random';
$(document).ready(function () {
    $.get(url, function (data) {
        catFact = data.text;
    })
  });

$('#get-fact').click(function () {
  // #ID of item.click
    $.get(url, function (data) {
        catFact = data.text;
    })
    // $.get will get from the "url" as declared earlier,
    // and then whatever it replies with is "data"
    // data is used in the function which runs on a promise
    // so it doesn't egt waited on for the reset of the page to run
    $('UL.my_list').append('<li>' + catFact + '</li>');
});
