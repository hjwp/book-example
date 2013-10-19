$(document).ready(function() {

    var urls;
    var csrfToken;

    var initialize = function (navigator, user, token, urls_){
        urls = urls_;
        csrfToken = token;
        $('#id_login').on('click', function () {
            navigator.id.request();
        });

        navigator.id.watch({
            loggedInUser: user,
            onlogin: submitAssertion,
            onlogout: logOut
        });
    };

    var submitAssertion = function (assertion) {
        $.post(urls.login, { assertion: assertion, csrfmiddlewaretoken: csrfToken });
    };

    var logOut = function () {};

    window.Superlists = {
        Accounts: {
            initialize: initialize,
            submitAssertion: submitAssertion,
            logOut: logOut
        }
    };


});
