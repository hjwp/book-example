window.Superlists = {};

window.Superlists.updateItems = function (url) {
  $.get(url).done(function (response) {
    var rows = '';
    for (var i=0; i<response.length; i++) {
      var item = response[i];
      rows += '\n<tr><td>' + (i+1) + ': ' + item.text + '</td></tr>';
    }
    $('#id_list_table').html(rows);
  });
};

window.Superlists.initialize = function (url) {
  $('input[name="text"]').on('keypress', function () {
    $('.has-error').hide();
  });

  if (url) {
    window.Superlists.updateItems(url);

    var form = $('#id_item_form');
    form.on('submit', function(event) {
      event.preventDefault();
      $.post(url, {
        'text': form.find('input[name="text"]').val(),
        'csrfmiddlewaretoken': form.find('input[name="csrfmiddlewaretoken"]').val(),
      }).done(function () {
        $('.has-error').hide();
        window.Superlists.updateItems(url);
      }).fail(function (xhr) {
        $('.has-error').show();
        if (xhr.responseJSON && xhr.responseJSON.error) {
          $('.has-error .help-block').text(xhr.responseJSON.error);
        } else {
          $('.has-error .help-block').text('Error talking to server. Please try again.');
        }
      });
    });
  }
};

