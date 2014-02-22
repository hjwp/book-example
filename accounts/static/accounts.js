var initialize = function (navigator) {
    navigator.id.request();
    navigator.id.doSomethingElse();
};

window.Superlists = {
    Accounts: {
        initialize: initialize
    }
};
