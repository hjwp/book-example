window.Superlists = {};

window.Superlists.hideErrorsOnInput = function () {
  $('input[name="text"]').on('keypress', function () {
    $('.has-error').hide();
  });
};

window.Superlists.startAjax = function (url) {
  $.get(url).done(function (response) {
    var rows = '';
    for (var i=0; i<response.length; i++) {
      var row = response[i];
      rows += '<tr><td>' + (i+1) + ': ' + row.text + '</td></tr>\n';
    }
    $('#id_list_table').html(rows);
  });
};
