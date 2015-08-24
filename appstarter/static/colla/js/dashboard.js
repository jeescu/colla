var token;

var get = function(id) {
    return document.getElementById(id);
}

var getQuery = function(id) {
    return document.querySelector(id);
}

var getName = function(id) {
    return document.getElementsByName(id);
}

function addEvt(id, fn, act) {
    for (e in id) {
        get(id[e]).addEventListener(act, fn[e]);
    }
}

function toggle(tbs, act, cls) {
    if (act == 'show')
    {
        for (tab in tbs) { get(tbs[tab]).classList.remove(cls); }
    }
    else if (act == 'hide')
    {
        for (tab in tbs) { get(tbs[tab]).classList.add(cls); }
    }
    else if (act == 'custom') {
        for (tab in tbs) { get(tbs[tab]).classList.add(cls[tab]); }
    }
}

function showActivity() {
    toggle(['fragment-activity'], 'show', 'hidden');
    toggle(['fragment-article', 'fragment-resource', 'fragment-forum', 'fragment-issue'], 'hide', 'hidden');
}

function showArticle() {
    toggle(['fragment-article'], 'show', 'hidden');
    toggle(['fragment-activity', 'fragment-resource', 'fragment-forum', 'fragment-issue'], 'hide', 'hidden');
    getArticles();
}

function showResource() {
    toggle(['fragment-resource'], 'show', 'hidden');
    toggle(['fragment-article', 'fragment-activity', 'fragment-forum', 'fragment-issue'], 'hide', 'hidden');
}

function showForum() {
    toggle(['fragment-forum'], 'show', 'hidden');
    toggle(['fragment-article', 'fragment-resource', 'fragment-activity', 'fragment-issue'], 'hide', 'hidden');
}

function showIssue() {
    toggle(['fragment-issue'], 'show', 'hidden');
    toggle(['fragment-article', 'fragment-resource', 'fragment-forum', 'fragment-activity'], 'hide', 'hidden');
}

function textToolSelected() {
    toggle(['new-text'], 'hide', 'tool-selected');
    toggle(['new-link', 'new-image'], 'show', 'tool-selected');
    toggle(['text-field'], 'show', 'hidden');
    toggle(['image-field'], 'hide', 'hidden');
}

function imageToolSelected () {
    toggle(['new-image'], 'hide', 'tool-selected');
    toggle(['new-link', 'new-text'], 'show', 'tool-selected');
    toggle(['text-field'], 'hide', 'hidden');
    toggle(['image-field'], 'show', 'hidden');
}

function linkToolSelected () {
    toggle(['new-link'], 'hide', 'tool-selected');
    toggle(['new-image', 'new-text'], 'show', 'tool-selected');
}

function articleDialog() {
    get('article-dialog').toggle();
}

function askDialog() {
    get('ask-dialog').toggle();
}

function bugReportDialog() {
    get('bug-report-dialog').toggle();
}

function showPostThumb() {
    toggle(['post-label-img'], 'show', 'add-image');
    toggle(['post-thumb', 'image-input', 'post-label-img'], 'custom', ['img-thumb', 'hidden', 'full-width']);
}

function showArticleThumb() {
    toggle(['article-label-img'], 'show', 'add-image');
    toggle(['article-thumb', 'article-image-input', 'article-label-img'], 'custom', ['img-thumb', 'hidden', 'full-width']);
}

function init() {
    token = get('_token').value;
    
    // tabs
    addEvt(['tab-activity', 'tab-article', 'tab-forum', 'tab-issue', 'tab-resource'], 
          [showActivity, showArticle, showForum, showIssue, showResource],
          'click');
    
    // New Post Tool
    addEvt(['reset-text', 'new-text', 'new-image', 'new-link'],
          [clearText, textToolSelected, imageToolSelected, linkToolSelected],
          'click');

    // action new button
    addEvt(['new-article', 'new-question', 'new-bug-report'],
           [articleDialog, askDialog, bugReportDialog],
           'click');
    
    // activity
    addEvt(['more'], [loadMorePost], 'click');
    
    autoloadPost();
}

$(document).ready(function(){
    $('[state=in]').html('Online');
    $('[state=out]').html('Offline');
});

window.addEventListener("load", init);
