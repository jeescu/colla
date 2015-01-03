//var xmlhttp;
//
//function AJAXRequest(req, url, func) {
//    if (window.XMLHttpRequest)
//    {
//        xmlhttp = new XMLHttpRequest();
//    }
//    else
//    {
//        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
//    }
//    xmlhttp.onreadystatechange = func;
//    xmlhttp.open(req, url, true);
//    xmlhttp.send();
//}

//function sendNewPost() {
//    TODO: Use post
//    AJAXRequest("GET", "new-post/?"+"userid="+token+"&text="+postTEXT.value, function() {
//        if (xmlhttp.readyState==4 && xmlhttp.status==200)
//        {
//            document.getElementById("test-response").innerHTML=xmlhttp.responseText;
//        }
//    }); 
//}

function AJAXRequest(url, type, data, func) {
    console.log('ajax sending..')
    $.ajax({
        url: url,
        type: type,
        data: data, 
        contentType: "application/json;charset=utf-8",
        dataType: "json",
        success: function(data) { 
            func();
            console.log('Success');
        },
        error: function(ts) { 
            console.log('Error');
        }
    });
}

//refresh post with limit of 10
function autoloadPost() {
    console.log('autoloadpost');
    document.getElementById('new-post').classList.add('hidden');
    
    var postUpdate = function() {
//        for loop paper shadow
        alert(data);
    }
    
    setInterval(function() {
        AJAXRequest("update-post", "GET", {}, postUpdate)
    }, 10000);
}

function sendNewPost() {
    var post = {
        "userid" : token,
        "text" : postTEXT.value,
        "image" : postIMAGE || "None",
        "link" : postLINK || "None",
        "sharetype" : "Shared Publicly"
    }
    
    var newPost = function() {
        document.getElementById('new-post').classList.remove('hidden');
        document.getElementById('new-post-img').src = document.getElementById('user-post-img').src;
        document.getElementById('new-post-name').innerHTML = document.getElementById('user-post-name').value;
        document.getElementById('new-post-share-type').innerHTML = "Shared Publicly";
        document.getElementById('new-post-date').innerHTML = "Now";
        document.getElementById('new-post-text').innerHTML = postTEXT.value;
        document.getElementById('new-post-pic').src = "";
    }
    
    AJAXRequest("new-post","GET", post, newPost);
}

function loadMorePost() {
    postLimit+=10;
}

function postBtn() {
    var btn = document.getElementById('post-btn');
    var text = document.getElementById('post-text').value;
    if (text != '')
    {
        btn.classList.remove('btn-hide');
        btn.classList.add('btn-show')
    }
    else
    {
        btn.classList.remove('btn-show');
        btn.classList.add('btn-hide')
    }
}