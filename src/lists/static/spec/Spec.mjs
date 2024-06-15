import {initialize} from "../lists.mjs";

describe("Superlists tests", () => {
  let testDiv;
  const inputSelector = "input#id_text";
  const errorSelector = "div.invalid-feedback";

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

  it("sense-check default dom fixture from beforeEach", () => {
    const textInput = document.querySelector(inputSelector);
    const errorDiv = document.querySelector(errorSelector);
    expect(errorDiv.checkVisibility()).toBe(true);
    expect(textInput.classList).toContain("is-invalid");
  });

  it("error div should not just be hidden immediately by initialize()", () => {
    const errorDiv = document.querySelector(errorSelector);

    initialize(inputSelector);

    expect(errorDiv.checkVisibility()).toBe(true);
  });

  it("error message should be hidden on input", () => {
    const textInput = document.querySelector(inputSelector);
    const errorDiv = document.querySelector(errorSelector);

    initialize(inputSelector);
    textInput.dispatchEvent(new InputEvent("input"));

    expect(errorDiv.checkVisibility()).toBe(false);
    expect(textInput.classList).not.toContain("is-invalid");
  });

});
