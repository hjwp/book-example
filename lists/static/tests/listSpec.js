describe('my test runner', function () {

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

  it('should be able to check element visibility', function () {
    expect( $('.has-error').length ).toEqual(1);
    expect( $('.has-error').is(':visible') ).toBe(true);
    $('.has-error').hide();
    expect( $('.has-error').is(':visible') ).toBe(false);
  });

  it('should be able to check element visibility twice', function () {
    expect( $('.has-error').length ).toEqual(1);
    expect( $('.has-error').is(':visible') ).toBe(true);
    $('.has-error').hide();
    expect( $('.has-error').is(':visible') ).toBe(false);

  });

});

