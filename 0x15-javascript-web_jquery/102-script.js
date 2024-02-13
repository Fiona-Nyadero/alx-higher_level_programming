#!/usr/bin/node

$(document).ready(function() {
    $('#btn_translate').click(function() {
      let languageCode = $('#language_code').val();
      
      $.ajax({
        url: 'https://www.fourtonfish.com/hellosalut/hello/',
        type: 'GET',
        data: { lang: languageCode },
        success: function(response) {
          let translation = response.hello;
          $('#hello').text(translation);
        },
        error: function() {
          $('#hello').text('Error fetching translation');
        }
      });
    });
});  