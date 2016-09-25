console.log('list.js loads');
window.oldBody = $('body')[0];
console.log(window.oldBody);
$('body').on('keypress', function () {
  console.log('handler');
  $('.has-error').hide();
});
