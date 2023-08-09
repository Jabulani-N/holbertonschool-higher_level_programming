let catFact = '';
const url = 'https://cat-fact.herokuapp.com/facts/random';
$(document).ready(function () {
    $.get(url, function (data) {
        catFact = data.text;
    })
  });
$('#get-fact').click(function () {
    $.get(url, function (data) {
        catFact = data.text;
    })
    $('UL.my_list').append('<li>' + catFact + '</li>');
});
