describe("Superlists tests", () => {
  let testDiv;

  beforeEach(() => {
    testDiv = document.createElement("div");
    testDiv.innerHTML = `
      <form>
        <input
          id="id_text"
          name="text"
          class="form-control form-control-lg is-invalid"
          placeholder="Enter a to-do item"
          value="Value as submitted"
          aria-describedby="id_text_feedback"
          required
        />
        <div id="id_text_feedback" class="invalid-feedback">An error message</div>
      </form>
    `
    document.body.appendChild(testDiv)
  });

  afterEach(() => {
    testDiv.remove();
  });

  it("smoke test for checking visibility", () => {
    const errorDiv = document.querySelector("div.invalid-feedback");
    expect(errorDiv.checkVisibility()).toBe(true, "error div should be visible on load");
    errorDiv.style.display = "none";
    expect(errorDiv.checkVisibility()).toBe(false, "js hiding should work");
  });

});
