/*global $ */

var initialize = function (navigator, user, token, urls) {
    $('#id_login').on('click', function () {
        navigator.id.request();
    });

    navigator.id.watch({
        loggedInUser: user,
        onlogin: function (assertion) {
            $.post(
                urls.login,
                { assertion: assertion, csrfmiddlewaretoken: token }
            );
        },
        onlogout: function () {}
    });
};

window.Superlists = {
    Accounts: {
        initialize: initialize
    }
};
