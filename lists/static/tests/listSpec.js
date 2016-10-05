describe('javascript for lists', function () {

  beforeEach(function () {
    var myFixture = $(
        '<form id="testform">' + 
          '<input name="text" />' +
          '<div class="has-error">Error!</div>' + 
        '</form>'
    );
    $('body').append(myFixture);
  });

  afterEach(function () {
    $('#testform').remove();
  });

  it('hide errors on input', function () {
    console.log('input test');
    $('input[name="text"]').trigger('keypress');
    expect( $('.has-error').is(':visible') ).toBe(false);
  });

  it('should not hide errors unnecessarily', function () {
    expect( $('.has-error').is(':visible') ).toBe(true);
  });

});

