window.Superlists = {};

window.Superlists.updateItems = function (url) {
  $.get(url).done(function (response) {
    if (!response.items) {return;}
    var rows = '';
    for (var i=0; i<response.items.length; i++) {
      var item = response.items[i];
      rows += '\n<tr><td>' + (i+1) + ': ' + item.text + '</td></tr>';
    }
    $('#id_list_table').html(rows);
  });
};

window.Superlists.initialize = function (params) {
  $('input[name="text"]').on('keypress', function () {
    $('.has-error').hide();
  });

  if (params) {
    window.Superlists.updateItems(params.listApiUrl);

    var form = $('#id_item_form');
    form.on('submit', function(event) {
      event.preventDefault();
      $.post(params.itemsApiUrl, {
        'list': params.listId,
        'text': form.find('input[name="text"]').val(),
        'csrfmiddlewaretoken': form.find('input[name="csrfmiddlewaretoken"]').val(),
      }).done(function () {
        $('.has-error').hide();
        window.Superlists.updateItems(params.listApiUrl);
      }).fail(function (xhr) {
        $('.has-error').show();
        if (xhr.responseJSON) {
          $('.has-error .help-block').text(xhr.responseJSON.text || xhr.responseJSON.non_field_errors);
        } else {
          $('.has-error .help-block').text('Error talking to server. Please try again.');
        }
      });
    });
  }
};

