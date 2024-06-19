const initialize = (errorSelector, inputSelector) => {
  const textInput = document.querySelector(inputSelector);
  textInput.oninput = () => {
    const errorMsg = document.querySelector(errorSelector);
    errorMsg.style.display = "none";
  };
};
