// script that fetches and lists title of all movies by using a URL

const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data){
	console.log(data);
	data.results.forEach(film => {
        $('UL#list_movies').append($('<li>').text(film.title));
   });
});
