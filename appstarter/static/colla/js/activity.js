function AJAXRequest(url, type, data, fn, contentType, dataType, processData) {
    $.ajax({
        url: url,
        type: type,
        data: data,
        contentType: contentType,
        dataType: dataType,
        success: function (data) {
            console.info('Success');
            fn(data);
        },
        error: function (ts) {
            console.error('Error');
            document.querySelector('#toastConnectionOut').show();
        }
    });
}

var postUpdate = function (post) {
    var newPost = document.getElementById('new-post'), post_number = Object.keys(post).length;
    var userDisName = document.getElementById('user-post-name').value;
    var userProfPic = document.getElementById('user-prof-pic').value;
    var csrftoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    if (post_number === 1 && newPost.className === 'new-post-show') {
        console.log('1 updated post , and you did it');
        document.getElementById('new-post').classList.remove('new-post-show');
        document.getElementById('new-post').classList.add('new-post-hide');

        console.log('append my post secretly');

        var userPost = post[Object.keys(post)[0]];
     
        var post_form = '<div id="post_activity"><input id="post" type="hidden" value="'+userPost['post_id']+'"><paper-shadow class="indx-fragment" z="0">';
            post_form += '<div class="row"><div class="col-xs-1 frm-av"><img src="'+userPost['pic']+'"/></div><div class="col-xs-8">';
            post_form +=     '<div class="col-xs-12 frm-name">'+userPost['display_name']+'</div>';
            post_form +=     '<div class="col-xs-12 frm-share sub-color">'+userPost['share']+'</div>';
            post_form +=         '</div><div class="frm-date">'+userPost['date']+'</div>';
            post_form +=         '<div class="col-xs-12 frm-txt"><p>'+userPost['text'].replace(/\n/g, "<br />")+'</p></div>';
            post_form +=         '<div class="col-xs-12 frm-pic"><img id="user-new-image-post" class="img-responsive" src="'+userPost['image']+'"/></div>';
            post_form +=         '<div class="col-xs-12 frm-dtl">';
            post_form +=            '<div class="frm-dtl-info">';
            post_form +=               '<form id="'+userPost['post_id']+'" method="post"><input type="hidden" name="csrfmiddlewaretoken" value="'+csrftoken+'">';
            post_form +=                '<input type="hidden" value="'+userPost['post_id']+'" name="post_id">';
            post_form +=                '<input type="hidden" value="'+userDisName+'" name="user_name">';
            post_form +=                '<input id="submit-agree'+userPost['post_id']+'" type="submit" class="hidden">';
            post_form +=                '<paper-button class="btn-frm-info agree-post"><core-icon icon="thumb-up"></core-icon>';
            post_form +=                    '<span>&emsp;'+userPost['agrees']+'</span></paper-button>';
            post_form +=                '<paper-button  class="btn-frm-info"><core-icon icon="question-answer"></core-icon>';
            post_form +=                '<span>&emsp;'+userPost['comments']+'</span></paper-button></form></div>';
            post_form +=        '<form id="'+userPost['post_id']+'" method="post"><input type="hidden" name="csrfmiddlewaretoken" value="'+csrftoken+'">'
            post_form +=            '<div class="txt-comm" >'
            post_form +=                '<input type="hidden" value="'+userPost['post_id']+'" name="post_id" />'
            post_form +=                '<input type="hidden" value="'+userProfPic+'" name="pic" />'
            post_form +=                '<input type="hidden" value="'+userDisName+'" name="user_name" />'
            post_form +=                '<paper-input-decorator label="Add new comment...">'
            post_form +=                    '<paper-autogrow-textarea id="a1"><textarea id="t1" name="comment"></textarea></paper-autogrow-textarea></paper-input-decorator></div>'
            post_form +=            '<div class="snd-comm hidden-xs"><input id="submit-comment'+userPost['post_id']+'" type="submit" class="hidden"/><paper-icon-button class="send-comment" icon="send"></paper-icon-button>'
            post_form +=            '</div></form></div></div>';

            post_form +=         '<div class="row con-comm"><div class="col-xs-12 frm-comm">';


//                                            Loop if ever there were already comments
//                                            <paper-shadow z="0" class="comment-board">
//                                                <div class="col-xs-2 comm-av"><img src="{{ comment.user_pic_url }}"/></div>
//                                                <div class="col-xs-10">
//                                                    <div class="col-xs-12 comm-name">{{ comment.user_name }}</div>
//                                                    <div class="col-xs-12 comm-time sub-color">{{ comment.comment_date }}</div>
//                                                </div>
//                                                <div class="col-xs-12 comm-text">
//                                                    <p>{{ comment.comment }}</p>
//                                                </div>
//                                            </paper-shadow>


            post_form +=      '</div></div></paper-shadow><br/></div>';
        
            console.log('Writing posts');
            $("#dynamic").prepend(post_form);
            userPost['image'] == "" ? document.getElementById('user-new-image-post').style.display="none":true;

    }
    else if (post.status)
    {
        console.info('no post updates');
    }
    else if(Object.keys(post).length == 0)
    {
        console.info('no available posts');
    }
    else
    {
        console.info('1 or more updated post'); 
        for (i=0;i < post_number; i++) {

            var userPost = post[Object.keys(post)[i]];
            console.debug(post[Object.keys(post)[i]]);

            var post_form = '<div id="post_activity"><input id="post" type="hidden" value="'+userPost['post_id']+'"><paper-shadow class="indx-fragment" z="0">';
                post_form += '<div class="row"><div class="col-xs-1 frm-av"><img src="'+userPost['pic']+'"/></div><div class="col-xs-8">';
                post_form +=     '<div class="col-xs-12 frm-name">'+userPost['display_name']+'</div>';
                post_form +=     '<div class="col-xs-12 frm-share sub-color">'+userPost['share']+'</div>';
                post_form +=         '</div><div class="frm-date">'+userPost['date']+'</div>';
                post_form +=         '<div class="col-xs-12 frm-txt"><p>'+userPost['text'].replace(/\n/g, "<br />")+'</p></div>';
                post_form +=         '<div class="col-xs-12 frm-pic"><img id="user-new-image-post" class="img-responsive" src="'+userPost['image']+'"/></div>';
                post_form +=         '<div class="col-xs-12 frm-dtl">';
                post_form +=            '<div class="frm-dtl-info">';
                post_form +=               '<form id="'+userPost['post_id']+'" method="post"><input type="hidden" name="csrfmiddlewaretoken" value="'+csrftoken+'">';
                post_form +=                '<input type="hidden" value="'+userPost['post_id']+'" name="post_id">';
                post_form +=                '<input type="hidden" value="'+userDisName+'" name="user_name">';
                post_form +=                '<input id="submit-agree'+userPost['post_id']+'" type="submit" class="hidden">';
                post_form +=                '<paper-button class="btn-frm-info agree-post"><core-icon icon="thumb-up"></core-icon>';
                post_form +=                    '<span>&emsp;'+userPost['agrees']+'</span></paper-button>';
                post_form +=                '<paper-button  class="btn-frm-info"><core-icon icon="question-answer"></core-icon>';
                post_form +=                '<span>&emsp;'+userPost['comments']+'</span></paper-button></form></div>';
                post_form +=        '<form id="'+userPost['post_id']+'" method="post"><input type="hidden" name="csrfmiddlewaretoken" value="'+csrftoken+'">'
                post_form +=            '<div class="txt-comm" >'
                post_form +=                '<input type="hidden" value="'+userPost['post_id']+'" name="post_id" />'
                post_form +=                '<input type="hidden" value="'+userProfPic+'" name="pic" />'
                post_form +=                '<input type="hidden" value="'+userDisName+'" name="user_name" />'
                post_form +=                '<paper-input-decorator label="Add new comment...">'
                post_form +=                    '<paper-autogrow-textarea id="a1"><textarea id="t1" name="comment"></textarea></paper-autogrow-textarea></paper-input-decorator></div>'
                post_form +=            '<div class="snd-comm hidden-xs"><input id="submit-comment'+userPost['post_id']+'" type="submit" class="hidden"/><paper-icon-button class="send-comment" icon="send"></paper-icon-button>'
                post_form +=            '</div></form></div></div>'
                                    
                post_form +=         '<div class="row con-comm"><div class="col-xs-12 frm-comm">'
                                        
                                    
//                                            Loop if ever there were already comments
//                                            <paper-shadow z="0" class="comment-board">
//                                                <div class="col-xs-2 comm-av"><img src="{{ comment.user_pic_url }}"/></div>
//                                                <div class="col-xs-10">
//                                                    <div class="col-xs-12 comm-name">{{ comment.user_name }}</div>
//                                                    <div class="col-xs-12 comm-time sub-color">{{ comment.comment_date }}</div>
//                                                </div>
//                                                <div class="col-xs-12 comm-text">
//                                                    <p>{{ comment.comment }}</p>
//                                                </div>
//                                            </paper-shadow>
                                        
                                      
                post_form +=      '</div></div></paper-shadow><br/></div>';
                                    
                console.log('Writing posts');
                document.getElementById('new-post-pic').src="";
                $("#dynamic").prepend(post_form);
                userPost['image'] == "" ? document.getElementById('user-new-image-post').style.display="none":true;
            
                document.querySelector('#toastNewPost').show();
                
        }
        console.info('Finish writing posts');
    }
}

//refresh post with limit of 10
function autoloadPost() {

    console.log('autoloadpost');
    
    setInterval(function() {
        AJAXRequest("update-post", "GET", getlatest(), postUpdate, "application/json;charset=utf-8", "json")
    }, 5000);
}

function getlatest() {
    var latestPost = {}
    try
    {
        var postId = document.getElementById('post_activity');
        latestPost.latest = postId.getElementsByTagName('input')[0].value;

        console.log('latest post is: '+latestPost.latest);
    }
    catch(err)
    {
        latestPost.latest = "None"
        console.log('latest post is: '+latestPost.latest);
    }
    return latestPost;
}

var formPostId = 0;
$('#imageUploadForm').on('submit',(function(e) {
    e.preventDefault();
    var formData = new FormData(this);

    console.log('Pressed upload ajax POST')
    formPostId = 1;

    formData.userid = token;
    formData.title = "None";
    formData.text = postTEXT.value.replace(/\n/g, "<br />");      
    formData.image =  postIMAGE || "None";
    formData.link = postLINK || "None";
    formData.sharetype = "Shared Publicly";

    var newUserPost = function() {
        document.getElementById('new-post').classList.remove('new-post-hide');
        document.getElementById('new-post').classList.add('new-post-show');
        document.getElementById('new-post-img').src = document.getElementById('user-post-img').src;
        document.getElementById('new-post-name').innerHTML = document.getElementById('user-post-name').value;
        document.getElementById('new-post-share-type').innerHTML = "Shared Publicly";
        document.getElementById('new-post-date').innerHTML = "Now";
        document.getElementById('new-post-text').innerHTML = postTEXT.value.replace(/\n/g, "<br />");
        // Need To fix for production
        
        var thumb = document.getElementById('thumb').src;
        var img = document.getElementById('new-post-pic');
        
        console.log(thumb);
        if ((thumb == "http://localhost:8080/colla/") || (thumb == "http://localhost:8000/colla/"))
        {
            img.style.display = "none";
        }
        else
        {
            img.removeAttribute("style"); 
            img.src = thumb;
        }
    }

    $.ajax({
        type:'POST',
        url: 'new-post/',
        data:formData,
        cache:false,
        contentType: false,
        processData: false,
        success:function(data){
            newUserPost();
            clearText();
            formPostId = 0;
            document.querySelector('#toastPost').show();
        },
        error: function(data){
            console.error("error");
        }
    });

}));

// comment and agree post
var commentFormId;
var agreeFormId;
var agreeOrCommentUrl;

var toast;
// agrees
$('body').on('click', '.agree-post', function (){
    agreeFormId = $(this).closest('form').attr("id");
    agreeOrCommentUrl = 'new-agree/';
    toast = document.querySelector('#toastAgree');
    $('#submit-agree'+agreeFormId).trigger('click');
});

// comments
$('body').on('click', '.send-comment', function() {
    commentFormId = $(this).closest('form').attr("id");
    agreeOrCommentUrl = 'new-comment/';
    toast = document.querySelector('#toastComment');
    $('#submit-comment'+commentFormId).trigger('click');
});

$('body').on('submit', 'form', (function(e) {
    e.preventDefault();
    var formData = new FormData(this);

    if (formPostId == 0) {
        console.debug(agreeOrCommentUrl);
        postAgreeComment(agreeOrCommentUrl, formData, toast);
    }

}));

function postAgreeComment(url, data, msg) {
    $.ajax({
        type:'POST',
        url: url,
        data: data,
        cache:false,
        contentType: false,
        processData: false,
        success:function(data){
            console.info("success");
            msg.show();
            console.debug(data);
        },
        error: function(data){
            console.error("error");
        }
    });
}

$('#chat').on('click', (function (e) {
    console.log('click');
    document.getElementById('chat-board').style.display = 'block';
    document.getElementById('notification-board').style.display = 'none';
}));

$('#notification').on('click', (function (e) {
    console.log('click');
    document.getElementById('chat-board').style.display = 'none';
    document.getElementById('notification-board').style.display = 'block';
}));

// load more post vert pagination
function loadMorePost() {
    postLimit+=10;
}

function clearText() {
    $("#id_image").closest('form').trigger('reset');
    document.getElementById('thumb').src="";
    document.getElementById('thumb').classList.remove('img-thumb');
    document.getElementById("thumb").removeAttribute("style"); 
    document.getElementById('label-img').classList.remove('full-width');
    document.getElementById('label-img').classList.add('add-image');
    document.getElementById('image-input').classList.remove('hidden');
    document.getElementById('post-text').value = "";
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