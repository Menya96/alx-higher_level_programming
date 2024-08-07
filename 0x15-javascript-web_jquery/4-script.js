//script that toggles the class of header element when the user clicks
//on the DiV tag

const $ = window.$;
$('#toggle_header').bind('click', function() {
	$('header').toggleClass('green red');
});


