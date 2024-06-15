const initialize = (inputSelector) => {
  const textInput = document.querySelector(inputSelector);
  textInput.oninput = () => {
    textInput.classList.remove("is-invalid");
  }
};

export { initialize };
