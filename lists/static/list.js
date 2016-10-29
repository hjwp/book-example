window.Superlists = {};
window.Superlists.initialize = function (url) {
  $('input[name="text"]').on('keypress', function () {
    $('.has-error').hide();
  });

  if (url) {
    $.get(url).done(function (response) {
      var rows = '';
      for (var i=0; i<response.length; i++) {
        var item = response[i];
        rows += '\n<tr><td>' + (i+1) + ': ' + item.text + '</td></tr>';
      }
      $('#id_list_table').html(rows);
    });
  }

};

