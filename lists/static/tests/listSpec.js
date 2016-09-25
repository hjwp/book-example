describe("list js", function() {
  beforeEach(function () {
    var form = $(
      '<form id="testform">' +
        '<input name="text" />' +
        '<div class="has-error"></div>' +
      '</form>'
    );
    $('body').append(form);

  });
  afterEach(function () {
    $('#testform').remove();
  });

  it("should be able to use jquery to create and hide things", function() {
    expect( $('.has-error').is(':visible') ).toBe(true);
    $('.has-error').hide();
    expect( $('.has-error').is(':visible') ).toBe(false);
  });

  it("should be able to run the same test twice", function() {
    expect( $('.has-error').is(':visible') ).toBe(true);
    $('.has-error').hide();
    expect( $('.has-error').is(':visible') ).toBe(false);
  });

});

