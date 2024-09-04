console.log("Spec.js loading");

describe("Superlists tests", () => {
  let testDiv;

  beforeEach(() => {
    console.log("beforeEach");
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

  it("sense-check our html fixture", () => {
    const errorMsg = document.querySelector(".invalid-feedback");
    expect(errorMsg.checkVisibility()).toBe(true);
  });

  it("error message should be hidden on input", () => {
    const textInput = document.querySelector("#id_text");
    const errorMsg = document.querySelector(".invalid-feedback");

    initialize();
    textInput.dispatchEvent(new InputEvent("input"));

    expect(errorMsg.checkVisibility()).toBe(false);
  });

  it("error message should not be hidden before input is fired", () => {
    const errorMsg = document.querySelector(".invalid-feedback");
    initialize();
    expect(errorMsg.checkVisibility()).toBe(true);
  });
});
