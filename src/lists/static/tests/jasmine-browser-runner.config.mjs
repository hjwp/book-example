export default {
  srcDir: ".",
  srcFiles: [
    "*.js"
  ],
  specDir: "tests",
  specFiles: [
    "**/*[sS]pec.js"
  ],
  helpers: [
    "helpers/**/*.js"
  ],
  env: {
    stopSpecOnExpectationFailure: false,
    stopOnSpecFailure: false,
    random: true,
    forbidDuplicateNames: true
  },
  listenAddress: "localhost",
  hostname: "localhost",
  browser: {
    name: "headlessFirefox"
  }
};
