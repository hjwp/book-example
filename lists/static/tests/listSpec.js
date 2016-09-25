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

  it("should hide errors on keypress", function() {
    $('#testform input').trigger('keypress');
    expect( $('.has-error').is(':visible') ).toBe(false);
  });

});

