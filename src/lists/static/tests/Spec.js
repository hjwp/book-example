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

  it("error message should be hidden on input", () => {
    const inputSelector = "input#id_text";
    const errorSelector = "div.invalid-feedback";
    const textInput = document.querySelector(inputSelector);
    const errorDiv = document.querySelector(errorSelector);
    expect(errorDiv.checkVisibility()).toBe(true, "error div should be visible on load");

    initialize(inputSelector, errorSelector);

    expect(errorDiv.checkVisibility()).toBe(true, "error div should not be hidden by initialize()");

    textInput.dispatchEvent(new InputEvent("input"));
    expect(errorDiv.checkVisibility()).toBe(false, "error div should be hidden on input");
  });

});
