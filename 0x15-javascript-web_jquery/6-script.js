// Script that updates the text of the header element to New header on click

const $ = window.$;
$('#update_header').bind('click', function() {
	$('header').replaceWith('New Header!!!');
});

