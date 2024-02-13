#!/usr/bin/node

$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
    const starwarsCharacter = data.name;
    $('#character').text(starwarsCharacter);
});