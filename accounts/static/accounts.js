$(document).ready(function() {
    var loginUrl;

    var initialize = function (navigator, loggedInUser, urls){
        $('#id_login').on('click', function () {
            navigator.id.request();
        });
        loginUrl = urls.login;

        navigator.id.watch({
            loggedInUser: loggedInUser,
            onlogin: onLogin,
            onlogout: onLogout
        });
    };

    var onLogin = function (assertion) {
        $.post(
            loginUrl, 
            {assertion: assertion, csrfmiddlewaretoken: 'csrf token'}
        ).done(
            Superlists.Accounts.onLoginDone
        );
    };
    var onLoginDone = function () {};
    var onLogout = function () {};

    window.Superlists = {
        Accounts: {
            initialize: initialize,
            onLogin: onLogin,
            onLoginDone: onLoginDone,
            onLogout: onLogout
        }
    };


});
