$(document).ready(function() {

    var initialize = function (navigator, user, token, urls_){
        $('#id_login').on('click', function () {
            navigator.id.request();
        });

        navigator.id.watch({
            loggedInUser: user,
        });
    };

    window.Superlists = {
        Accounts: {
            initialize: initialize
        }
    };


});
