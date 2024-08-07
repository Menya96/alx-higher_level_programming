//Script that adds class red to the header element on click
 const $ = window.$;
 $('#red_header').bind('click', function (){
	 $('header').addClass('red');
 });

