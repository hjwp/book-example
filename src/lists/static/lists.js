const initialize = (inputSelector, errorSelector) => {
  const textInput = document.querySelector(inputSelector);
  textInput.oninput = () => {
    textInput.classList.remove("is-invalid");
  };
};
