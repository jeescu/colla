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
        }
    });
}

var postUpdate = function (post) {
    var newPost = document.getElementById('new-post'), post_number = Object.keys(post).length;
    console.log(post);

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
            post_form +=         '<div class="col-xs-12 frm-dtl"><div class="frm-dtl-info"><paper-button class="btn-frm-info"><core-icon icon="thumb-up"></core-icon>';
            post_form +=                     '<span>&emsp;'+userPost['agrees']+'</span>'
            post_form +=                 '</paper-button><paper-button  class="btn-frm-info"><core-icon icon="question-answer"></core-icon>';
            post_form +=                     '<span>&emsp;'+userPost['comments']+'</span>';
            post_form +=                 '</paper-button></div><div class="txt-comm" ><paper-input-decorator label="Add new comment..."><paper-autogrow-textarea id="a1"><textarea id="t1"></textarea></paper-autogrow-textarea></paper-input-decorator></div>';
            post_form +=             '<div class="snd-comm hidden-xs"><paper-icon-button id="snd-comment" icon="send"></paper-icon-button></div></div></div>';

            post_form +=     '<div class="row con-comm"><div class="col-xs-12 frm-comm">';

            // for loop comments
            //                    <paper-shadow z="0" class="comment-board">
            //                         <div class="col-xs-2 comm-av"><img src="{% static 'colla/images/qlt.png' %}"/></div>
            //                         <div class="col-xs-10">
            //                             <div class="col-xs-12 comm-name">John Edward Escuyos</div>
            //                             <div class="col-xs-12 comm-time sub-color">10:00 AM</div>
            //                         </div>
            //                         <div class="col-xs-12 comm-text">
            //                             <p>Nothing beats my imagination!</p>
            //                         </div>
            //                  </paper-shadow>

            post_form +=      '</div></div></paper-shadow><br/></div>';
            // document.getElementById('new-post-pic').src="";
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
        console.info('1 updated post');
        for (i=0;i < post_number; i++) {

            var userPost = post[Object.keys(post)[i]];
            console.error(post[Object.keys(post)[i]]);

            var post_form = '<div id="post_activity"><input id="post" type="hidden" value="'+userPost['post_id']+'"><paper-shadow class="indx-fragment" z="0">';
                post_form += '<div class="row"><div class="col-xs-1 frm-av"><img src="'+userPost['pic']+'"/></div><div class="col-xs-8">';
                post_form +=     '<div class="col-xs-12 frm-name">'+userPost['display_name']+'</div>';
                post_form +=     '<div class="col-xs-12 frm-share sub-color">'+userPost['share']+'</div>';
                post_form +=         '</div><div class="frm-date">'+userPost['date']+'</div>';
                post_form +=         '<div class="col-xs-12 frm-txt"><p>'+userPost['text'].replace(/\n/g, "<br />")+'</p></div>';
                post_form +=         '<div class="col-xs-12 frm-pic"><img id="user-new-image-post" class="img-responsive" src="'+userPost['image']+'"/></div>';
                post_form +=         '<div class="col-xs-12 frm-dtl"><div class="frm-dtl-info"><paper-button class="btn-frm-info"><core-icon icon="thumb-up"></core-icon>';
                post_form +=                     '<span>&emsp;'+userPost['agrees']+'</span>'
                post_form +=                 '</paper-button><paper-button  class="btn-frm-info"><core-icon icon="question-answer"></core-icon>';
                post_form +=                     '<span>&emsp;'+userPost['comments']+'</span>';
                post_form +=                 '</paper-button></div><div class="txt-comm" ><paper-input-decorator label="Add new comment..."><paper-autogrow-textarea id="a1"><textarea id="t1"></textarea></paper-autogrow-textarea></paper-input-decorator></div>';
                post_form +=             '<div class="snd-comm hidden-xs"><paper-icon-button id="snd-comment" icon="send"></paper-icon-button></div></div></div>';

                post_form +=     '<div class="row con-comm"><div class="col-xs-12 frm-comm">';

                // for loop comments
                //                    <paper-shadow z="0" class="comment-board">
                //                         <div class="col-xs-2 comm-av"><img src="{% static 'colla/images/qlt.png' %}"/></div>
                //                         <div class="col-xs-10">
                //                             <div class="col-xs-12 comm-name">John Edward Escuyos</div>
                //                             <div class="col-xs-12 comm-time sub-color">10:00 AM</div>
                //                         </div>
                //                         <div class="col-xs-12 comm-text">
                //                             <p>Nothing beats my imagination!</p>
                //                         </div>
                //                  </paper-shadow>

                post_form +=      '</div></div></paper-shadow><br/></div>';
                console.log('Writing posts');
                document.getElementById('new-post-pic').src="";
                $("#dynamic").prepend(post_form);
                userPost['image'] == "" ? document.getElementById('user-new-image-post').style.display="none":true;
        }

        console.error('Finish writing posts');
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
        if (document.getElementById('thumb').src != "http://localhost:8080/colla/")
        {
            document.getElementById('new-post-pic').removeAttribute("style"); 
            document.getElementById('new-post-pic').src = document.getElementById('thumb').src;
        }
        else
        {
            document.getElementById('new-post-pic').style.display = "none";
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

$('.agree-comment').on('click', function() {
    agreeFormId = $(this).closest('form').attr("id");
    agreeOrCommentUrl = 'new-agree/';
    $('#submit-agree'+agreeFormId).trigger('click');
    console.info('submitting agree');
});

$('.send-comment').on('click', function() {
    commentFormId = $(this).closest('form').attr("id");
    agreeOrCommentUrl = 'new-comment/';
    $('#submit-comment'+commentFormId).trigger('click');
    console.info('submitting comment');
});

$('form').on('submit', (function(e) {
    e.preventDefault();
    var formData = new FormData(this);

    if (formPostId == 0) {
        console.debug(agreeOrCommentUrl);
        postAgreeComment(agreeOrCommentUrl, formData);
    }

}));

function postAgreeComment(url, data) {
    $.ajax({
        type:'POST',
        url: url,
        data: data,
        cache:false,
        contentType: false,
        processData: false,
        success:function(data){
            console.info("success");
            console.debug(data);
        },
        error: function(data){
            console.error("error");
        }
    });
}

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