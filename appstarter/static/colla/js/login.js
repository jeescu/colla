document.addEventListener('polymer-ready', function() {
    var navicon = document.getElementById('navicon');
    var drawerPanel = document.getElementById('drawerPanel');
    navicon.addEventListener('click', function() {
    drawerPanel.togglePanel();
    });
});

window.fbAsyncInit = function() {
    FB.init({
        appId      : '334517380088294',
        xfbml      : true,
        version    : 'v2.2'
    });
};

(function(d, s, id){
    var js, fjs = d.getElementsByTagName(s)[0];
    
    if (d.getElementById(id))
    {
        return;
    }
    
    js = d.createElement(s);
    js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
    
}(document, 'script', 'facebook-jssdk'));

var getCookies = function(){
    var pairs = document.cookie.replace(/\s+/g, '').split(";");
    var cookies = {};
    for (var i=0; i<pairs.length; i++){
        var pair = pairs[i].split("=");
        cookies[pair[0]] = unescape(pair[1]);
    }
    return cookies;
}

function fbLogin() {
    FB.login(function(response) {
        if (response.authResponse)
        {
            FB.api('/me', function(response) {
                var ck = getCookies();
                response.provider = 'facebook';
                response.accessToken =  FB.getAuthResponse()['accessToken'];
                response.session = ck.session_id || ck.csrftoken;
                verifyAuth(response, 'login/facebook/');
            });
        }
        else
        {
        console.info('User cancelled login or not authorize.');
        }
    });
}

//send
function verifyAuth(data, url) {
     $.ajax({
        type:'GET',
        url: url,
        data: data,
        success:function(data) {
            console.debug(data);
            window.location.href = '';
        },
        error: function(data) {
            console.error("error");
        }
    });
}
