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
    `;
    document.body.appendChild(testDiv);
  });

  afterEach(() => {
    testDiv.remove();
  });

  it("sense-check our html fixture", () => {
    const errorMsg = document.querySelector(".invalid-feedback");
    expect(errorMsg.checkVisibility()).toBe(true);
  });

  it("check we know how to hide things", () => {
    const errorMsg = document.querySelector(".invalid-feedback");
    errorMsg.style.display = "none";
    expect(errorMsg.checkVisibility()).toBe(false);
  });

});
