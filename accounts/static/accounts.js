/*global $ */

var initialize = function (navigator, user, token, urls) {
    $('#id_login').on('click', function () {
        navigator.id.request();
    });

    navigator.id.watch({
        loggedInUser: user
    });
};

window.Superlists = {
    Accounts: {
        initialize: initialize
    }
};
