window.Superlists = {};

window.Superlists.hideErrorsOnInput = function () {
  $('input[name="text"]').on('keypress', function () {
    $('.has-error').hide();
  });
};

var getListItems = function (url) {
  $.get(url).done(function (response) {
    var rows = '';
    for (var i=0; i<response.length; i++) {
      var row = response[i];
      rows += '<tr><td>' + (i+1) + ': ' + row.text + '</td></tr>\n';
    }
    $('#id_list_table').html(rows);
  });
};

window.Superlists.startAjax = function (url) {
  getListItems(url);
  var form = $('input[name="text"]').parent('form');
  form.on('submit', function (event) {
    event.preventDefault();
    $.post(url, {
      'text': form.find('input[name="text"]').val(),
      'csrfmiddlewaretoken': form.find('input[name="csrfmiddlewaretoken"]').val(),
    }).done(function () {
      getListItems(url);
    });
  });
};
