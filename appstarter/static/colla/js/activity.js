function AJAXRequest(url, type, data, func) {
    console.log('ajax sending..')
    $.ajax({
        url: url,
        type: type,
        data: data, 
        contentType: "application/json;charset=utf-8",
        dataType: "json",
        success: function(data) { 
            func(data);
            console.log('Success');
        },
        error: function(ts) { 
            console.log('Error');
        }
    });
}

var postUpdate = function(post) {
    var newPost = document.getElementById('new-post');
    var post_number = Object.keys(post).length;
    console.log(post);

    if (post_number == 1 && newPost.className == 'new-post-show') {
        console.log('1 updated post , and you did it');
        document.getElementById('new-post').classList.remove('new-post-show');
        document.getElementById('new-post').classList.add('new-post-hide');

        console.log('append my post secretly');

        var userPost = post[Object.keys(post)[0]];

        var post = '<div id="post_activity"><input id="post" type="hidden" value="'+userPost['post_id']+'"><paper-shadow class="indx-fragment" z="0">';
            post += '<div class="row"><div class="col-xs-1 frm-av"><img src="'+userPost['pic']+'"/></div><div class="col-xs-8">';
            post +=     '<div class="col-xs-12 frm-name">'+userPost['display_name']+'</div>';
            post +=     '<div class="col-xs-12 frm-share">'+userPost['share']+'</div>';
            post +=         '</div><div class="frm-date">'+userPost['date']+'</div>';
            post +=         '<div class="col-xs-12 frm-txt"><p>'+userPost['text']+'</p></div>';
            post +=         '<div class="col-xs-12 frm-pic"><img class="img-responsive" src="'+userPost['image']+'"/></div>';
            post +=         '<div class="col-xs-12 frm-dtl"><div class="frm-dtl-info"><paper-button class="btn-frm-info"><core-icon icon="thumb-up"></core-icon>';
            post +=                     '<span>&emsp;'+userPost['agrees']+'</span>'
            post +=                 '</paper-button><paper-button  class="btn-frm-info"><core-icon icon="question-answer"></core-icon>';
            post +=                     '<span>&emsp;'+userPost['comments']+'</span>';
            post +=                 '</paper-button></div><div class="txt-comm" ><paper-input-decorator label="Add new comment..."><paper-autogrow-textarea id="a1"><textarea id="t1"></textarea></paper-autogrow-textarea></paper-input-decorator></div>';
            post +=             '<div class="snd-comm hidden-xs"><paper-icon-button id="snd-comment" icon="send"></paper-icon-button></div></div></div>';

            post +=     '<div class="row con-comm"><div class="col-xs-12 frm-comm">';

            // for loop comments
            //                    <paper-shadow z="0" class="comment-board">
            //                         <div class="col-xs-2 comm-av"><img src="{% static 'colla/images/qlt.png' %}"/></div>
            //                         <div class="col-xs-10">
            //                             <div class="col-xs-12 comm-name">John Edward Escuyos</div>
            //                             <div class="col-xs-12 comm-time">10:00 AM</div>
            //                         </div>
            //                         <div class="col-xs-12 comm-text">
            //                             <p>Nothing beats my imagination!</p>
            //                         </div>
            //                  </paper-shadow>

            post +=      '</div></div></paper-shadow><br/></div>';
            console.log('Writing posts');
            $("#dynamic").prepend(post);

    }
    else if (post.status)
    {
        console.log('no post updates')
    }
    else
    {
        console.log('1 updated post');
        for (i=0;i < post_number; i++) {

            var userPost = post[Object.keys(post)[i]];

            var post = '<div id="post_activity"><input id="post" type="hidden" value="'+userPost['post_id']+'"><paper-shadow class="indx-fragment" z="0">';
                post += '<div class="row"><div class="col-xs-1 frm-av"><img src="'+userPost['pic']+'"/></div><div class="col-xs-8">';
                post +=     '<div class="col-xs-12 frm-name">'+userPost['display_name']+'</div>';
                post +=     '<div class="col-xs-12 frm-share">'+userPost['share']+'</div>';
                post +=         '</div><div class="frm-date">'+userPost['date']+'</div>';
                post +=         '<div class="col-xs-12 frm-txt"><p>'+userPost['text']+'</p></div>';
                post +=         '<div class="col-xs-12 frm-pic"><img class="img-responsive" src="'+userPost['image']+'"/></div>';
                post +=         '<div class="col-xs-12 frm-dtl"><div class="frm-dtl-info"><paper-button class="btn-frm-info"><core-icon icon="thumb-up"></core-icon>';
                post +=                     '<span>&emsp;'+userPost['agrees']+'</span>'
                post +=                 '</paper-button><paper-button  class="btn-frm-info"><core-icon icon="question-answer"></core-icon>';
                post +=                     '<span>&emsp;'+userPost['comments']+'</span>';
                post +=                 '</paper-button></div><div class="txt-comm" ><paper-input-decorator label="Add new comment..."><paper-autogrow-textarea id="a1"><textarea id="t1"></textarea></paper-autogrow-textarea></paper-input-decorator></div>';
                post +=             '<div class="snd-comm hidden-xs"><paper-icon-button id="snd-comment" icon="send"></paper-icon-button></div></div></div>';

                post +=     '<div class="row con-comm"><div class="col-xs-12 frm-comm">';

                // for loop comments
                //                    <paper-shadow z="0" class="comment-board">
                //                         <div class="col-xs-2 comm-av"><img src="{% static 'colla/images/qlt.png' %}"/></div>
                //                         <div class="col-xs-10">
                //                             <div class="col-xs-12 comm-name">John Edward Escuyos</div>
                //                             <div class="col-xs-12 comm-time">10:00 AM</div>
                //                         </div>
                //                         <div class="col-xs-12 comm-text">
                //                             <p>Nothing beats my imagination!</p>
                //                         </div>
                //                  </paper-shadow>

                post +=      '</div></div></paper-shadow><br/></div>';
                console.log('Writing posts');
                $("#dynamic").prepend(post);
        }

        console.log('Finish writing posts');
    }
}

//refresh post with limit of 10
function autoloadPost() {

    console.log('autoloadpost');
    
    setInterval(function() {
        AJAXRequest("update-post", "GET", getlatest(), postUpdate)
    }, 5000);
}

function getlatest() {
    var latestPost = {}
    try
    {
        latestPost.latest = document.getElementById('post_activity').getElementsByTagName('input')[0].value;
    }
    catch(err)
    {
        latestPost.latest = "None"
    }
    return latestPost;
}

function sendNewPost() {
    var post = {
        "userid" : token,
        "title" : "None",
        "text" : postTEXT.value,
        "image" : postIMAGE || "None",
        "link" : postLINK || "None",
        "sharetype" : "Shared Publicly"
    }
    
    var newPost = function(post) {
        document.getElementById('new-post').classList.remove('new-post-hide');
        document.getElementById('new-post').classList.add('new-post-show');
        document.getElementById('new-post-img').src = document.getElementById('user-post-img').src;
        document.getElementById('new-post-name').innerHTML = document.getElementById('user-post-name').value;
        document.getElementById('new-post-share-type').innerHTML = "Shared Publicly";
        document.getElementById('new-post-date').innerHTML = "Now";
        document.getElementById('new-post-text').innerHTML = postTEXT.value;
        document.getElementById('new-post-pic').src = "";
    }
    
    AJAXRequest("new-post","GET", post, newPost);
}

function sendNewComment() {
    
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