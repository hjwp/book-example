const initialize = (inputSelector, errorSelector) => {
  const errorDiv = document.querySelector(errorSelector);
  const textInput = document.querySelector(inputSelector);
  textInput.oninput = () => {
    errorDiv.style.display = "none";
  }
};

