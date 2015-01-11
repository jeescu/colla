var activity = document.getElementById('tab-activity');
var project = document.getElementById('tab-project');
var monitor = document.getElementById('tab-monitor');
var graph = document.getElementById('tab-graph');
var issue = document.getElementById('tab-issue');

var newIssue = document.getElementById('new-issue');
var newIssueDialog = document.getElementById('issue-dialog');
var newMessage = document.getElementById('new-message');
var newMsgDialog = document.getElementById('message-dialog');

var newText = document.getElementById('new-text');
var newImage = document.getElementById('new-image');
var newLink = document.getElementById('new-link');
var sendPost = document.getElementById('send-post');
var postTEXT = document.getElementById('post-text');
var postIMAGE = "";
var postLINK = "";
var resetText = document.getElementById('reset-text');
var postLimit = 10;
var loadMore = document.getElementById('more');

var imgInput = document.getElementById('image-input');

var sndComm = document.getElementById('send-comment');

var token;

function actShow() {
    document.getElementById('fragment-activity').classList.remove('hidden');
    document.getElementById('fragment-project').classList.add('hidden');
    document.getElementById('fragment-monitor').classList.add('hidden');
    document.getElementById('fragment-graph').classList.add('hidden');
    document.getElementById('fragment-issue').classList.add('hidden');
}

function proShow() {
    document.getElementById('fragment-project').classList.remove('hidden');
    document.getElementById('fragment-activity').classList.add('hidden');
    document.getElementById('fragment-monitor').classList.add('hidden');
    document.getElementById('fragment-graph').classList.add('hidden');
    document.getElementById('fragment-issue').classList.add('hidden');
}

function monShow() {
    document.getElementById('fragment-monitor').classList.remove('hidden');
    document.getElementById('fragment-project').classList.add('hidden');
    document.getElementById('fragment-activity').classList.add('hidden');
    document.getElementById('fragment-graph').classList.add('hidden');
    document.getElementById('fragment-issue').classList.add('hidden');
}

function graphShow() {
    document.getElementById('fragment-graph').classList.remove('hidden');
    document.getElementById('fragment-project').classList.add('hidden');
    document.getElementById('fragment-monitor').classList.add('hidden');
    document.getElementById('fragment-activity').classList.add('hidden');
    document.getElementById('fragment-issue').classList.add('hidden');
}

function issueShow() {
    document.getElementById('fragment-issue').classList.remove('hidden');
    document.getElementById('fragment-project').classList.add('hidden');
    document.getElementById('fragment-monitor').classList.add('hidden');
    document.getElementById('fragment-graph').classList.add('hidden');
    document.getElementById('fragment-activity').classList.add('hidden');
}

function textToolSelected() {
    document.getElementById('new-text').classList.add('tool-selected');
    document.getElementById('new-image').classList.remove('tool-selected');
    document.getElementById('new-link').classList.remove('tool-selected');
    document.getElementById('text-field').classList.remove('hidden');
    document.getElementById('image-field').classList.add('hidden');
}

function imageToolSelected () {
    document.getElementById('new-image').classList.add('tool-selected');
    document.getElementById('new-text').classList.remove('tool-selected');
    document.getElementById('new-link').classList.remove('tool-selected');
    document.getElementById('text-field').classList.add('hidden');
    document.getElementById('image-field').classList.remove('hidden');
}

function linkToolSelected () {
    document.getElementById('new-link').classList.add('tool-selected');
    document.getElementById('new-image').classList.remove('tool-selected');
    document.getElementById('new-text').classList.remove('tool-selected');
}

function issueDialog() {
    newIssueDialog.toggle();
}

function messageDialog() {
    newMsgDialog.toggle();
}

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#thumb')
                    .attr('src', e.target.result)
                    .height(166);
        };

        reader.readAsDataURL(input.files[0]);
    }

    document.getElementById('thumb').classList.add('img-thumb');
    imgInput.classList.add('hidden');
    document.getElementById('label-img').classList.remove('add-image');
    document.getElementById('label-img').classList.add('full-width');
}

function init() {
    token = document.getElementById('_token').value;
    
    //    tabs
	activity.addEventListener("click", actShow);
    project.addEventListener("click", proShow);
    monitor.addEventListener("click", monShow);
    graph.addEventListener("click", graphShow);
    issue.addEventListener("click", issueShow);
    
//  New Post Tool
    resetText.addEventListener("click", clearText);
    
    newText.addEventListener("click", textToolSelected);
    newImage.addEventListener("click", imageToolSelected);
    newLink.addEventListener("click", linkToolSelected);

//    action new button
    newIssue.addEventListener("click", issueDialog);
    newMessage.addEventListener("click", messageDialog);

//   post action
    // if (sndComm) {
    //     sndComm.addEventListener("click", sendNewComment);
    // }
    
//    activity
    loadMore.addEventListener("click", loadMorePost);    
    
//    issue
    
//    graph
    
//    monitor
    
    autoloadPost();
}

window.addEventListener("load", init);
