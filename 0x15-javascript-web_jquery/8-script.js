#!/usr/bin/node

$(document).ready(function() {
    $.ajax({
      url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
      type: 'GET',
      success: function(response) {
        var starwarsMovies = response.results;
        var $list = $('#list_movies');
  
        $.each(starwarsMovies, function(index, movie) {
          var $li = $('<li>').text(movie.title);
          $list.append($li);
        });
      },
      error: function(error) {
        console.log('Error:', error);
      }
    });
});  