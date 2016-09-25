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
    $('body').trigger('keypress');
    expect( $('.has-error').is(':visible') ).toBe(false);
  });

  it("should not hide errors unnecessarily", function() {
    expect( $('.has-error').is(':visible') ).toBe(true);
  });

  it("should attach an event handler to the body", function() {
    $('body').on('foo', function baz() {});
    expect( $._data(document.body, 'events') ).toEqual([]);
  });

  it("shouldnt mess with the body element", function() {
    expect(window.oldBody).toBe(document.body);
  });
});

