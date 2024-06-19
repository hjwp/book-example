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
    console.log("in test 1");
    const errorMsg = document.querySelector(".invalid-feedback");
    expect(errorMsg.checkVisibility()).toBe(true);
  });

  it("error message should be hidden on input", () => {
    console.log("in test 2");
    const textInput = document.querySelector("#id_text");
    const errorMsg = document.querySelector(".invalid-feedback");

    textInput.dispatchEvent(new InputEvent("input"));

    expect(errorMsg.checkVisibility()).toBe(false);
  });
});
