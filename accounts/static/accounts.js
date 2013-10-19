$(document).ready(function() {

    var initialize = function (navigator, loggedInUser, urls){
        $('#id_login').on('click', function () {
            navigator.id.request();
        });

        navigator.id.watch({
            loggedInUser: loggedInUser,
            onlogin: onLogin,
            onlogout: onLogout
        });
    };

    var onLogin = function () {};
    var onLogout = function () {};

    window.Superlists = {
        Accounts: {
            initialize: initialize,
            onLogin: onLogin,
            onLogout: onLogout
        }
    };


});
