describe('my test runner', function () {

  beforeEach(function () {
    var htmlFixture = $('<div id="myfixture" class="has-error">Error!</div>');
    $('body').append(htmlFixture);
  });

  afterEach(function () {
    $('#myfixture').remove();
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

