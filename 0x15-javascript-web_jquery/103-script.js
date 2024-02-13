#!/usr/bin/node

$(document).ready(function() {
    $('#btn_translate').click(function() {
      translateHello();
    });
  
    $('#language_code').keypress(function(event) {
      if (event.keyCode === 13) {
        translateHello();
      }
    });
  
    function translateHello() {
      var languageCode = $('#language_code').val();
  
      $.ajax({
        url: 'https://www.fourtonfish.com/hellosalut/hello/',
        type: 'GET',
        dataType: 'json',
        data: {
          lang: languageCode
        },
        success: function(response) {
          $('#hello').text(response.hello);
        },
        error: function() {
          $('#hello').text('Error fetching translation');
        }
      });
    }
});  