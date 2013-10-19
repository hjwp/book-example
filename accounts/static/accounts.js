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
            onlogin: function (assertion) {
                $.post(
                    urls.login,
                    { assertion: assertion, csrfmiddlewaretoken: token }
                ).done( Superlists.Accounts.refreshPage );
            },
        });
    };

    window.Superlists = {
        Accounts: {
            initialize: initialize,
            refreshPage: function () { console.log('who called me?'); }//window.location.reload(); }
        }
    };


});
