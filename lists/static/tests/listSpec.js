describe("list js", function() {
  it("should be able to use jquery to create and hide things", function() {
    expect( $('.has-error').is(':visible') ).toBe(true);
    $('.has-error').hide();
    expect( $('.has-error').is(':visible') ).toBe(false);
  });
});

