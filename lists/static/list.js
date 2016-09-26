window.Superlists = {};

window.Superlists.hideErrorsOnInput = function () {
  $('input[name="text"]').on('keypress', function () {
    $('.has-error').hide();
  });
};
