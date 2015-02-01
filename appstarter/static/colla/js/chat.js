
// Open new chat
$('.open-chat-head').click(function(e) {
    var chatHead = e.currentTarget;
    
    prepareChatArea(chatHead)
    
    //send ajax 
    //check whether conversation exist
    
    //if not - nothing displays
    
    //if yes - display their conversations
    
});

var openedChatRooms = ['rooms']

function prepareChatArea(chatArea) {
    var chatUserName = chatArea.getElementsByClassName('detail-board')[0].innerHTML
    var chatUserId = chatArea.getElementsByTagName('input')[0].value
    var chatRoom = $('#chat-rooms')
    
    var chats = 1;
    
    if (openedChatRooms.indexOf(chatUserId) < 0)
    {
        openedChatRooms.push(chatUserId);
        writeChatArea(chatUserId, chatUserName, chatRoom);
    }
                 
}

function writeChatArea(chatUserId, chatUserName, chatRoom) {
    var getElemByAtrrVal = function (e, attr, val) {
        return $(e+'['+attr+'='+val+']')
    }    

    var formId = 'chat'+chatUserId;

    // panel
    var chat = '<paper-shadow></paper-shadow>';
    $(chat).attr({
        z : '1',
        id : chatUserId,
        class : 'chat-area'
    }).appendTo(chatRoom);

    // form
    var form = '<form></form>';
    var chatMain = getElemByAtrrVal('paper-shadow', 'id', chatUserId);
    $(form).attr({
        id : formId,
        name : 'chatMessage',
        method : 'post'
    }).appendTo(chatMain);

    // token
    var inputTkn = '<input></input>'
    var tknName = 'csrfmiddlewaretoken';
    var tkn = getName(tknName)[0].value;
    var chatForm = getElemByAtrrVal('form', 'id', formId);
    $(inputTkn).attr({
        type : 'hidden',
        name : tknName,
        value : tkn
    }).appendTo(chatForm);
    
    $(inputTkn).attr({
        type : 'hidden',
        name : 'sender',
        value : token
    }).appendTo(chatForm);
    
    $(inputTkn).attr({
        type : 'hidden',
        name : 'reciever',
        value : chatUserId
    }).appendTo(chatForm);

    // head bar
    var chatHeadBar = '<div></div>';
    var chatHeadBarId = 'head'+formId;
    $(chatHeadBar).attr({
        id : chatHeadBarId,
        class : 'chat-head-bar'
    }).appendTo(chatForm);

    // head bar content
    var chatHeadBarForm = getElemByAtrrVal('div', 'id', chatHeadBarId);
    var chatHeadIcon = '<core-icon></core-icon>';
    $(chatHeadIcon).attr({
        icon : 'question-answer',
        class : 'chat-icon'
    }).appendTo(chatHeadBarForm);

    var chatHeadName = '<span></span>';
    $(chatHeadName).attr({
        class : 'chat-reciever'
    }).html(chatUserName).appendTo(chatHeadBarForm);

    var chatHeadMinMaxIcon = '<paper-icon-button></paper-icon-button>';
    $(chatHeadMinMaxIcon).attr({
        icon : 'remove',
        onclick : 'minMaxChatRoom(this)'
    }).appendTo(chatHeadBarForm);

    var chatHeadCloseIcon = '<paper-icon-button></paper-icon-button>';
    $(chatHeadCloseIcon).attr({
        icon : 'close',
        onclick : 'exitChatRoom(this)'
    }).appendTo(chatHeadBarForm);

    var chatHeadShadow = '<div></div>';
    $(chatHeadShadow).attr({
        class : 'chat-shadow'
    }).appendTo(chatHeadBarForm);

    // content
    var chatContent = '<div></div>';
    var chatContentId = 'content'+formId;
    $(chatContent).attr({
        id : chatContentId,
        class : 'chat-content'
    }).appendTo(chatForm);

    // content content
    var chatContentMessages = '<div></div>';
    var chatContentForm = getElemByAtrrVal('div', 'id', chatContentId);
    var chatContentMsgId = 'contentMsg'+formId;
    $(chatContentMessages).attr({
        id : chatContentMsgId,
        class : 'col-xs-12'
    }).appendTo(chatContentForm); 

    // write text
    var chatText = '<div></div>';
    var chatTextId = 'write'+formId;
    $(chatText).attr({
        id : chatTextId,
        class : 'chat-write'
    }).appendTo(chatForm);

    //write content
    var chatWriteForm = getElemByAtrrVal('div', 'id', chatTextId);
    var chatInput = '<input></input>';
    $(chatInput).attr({
        name : 'message',
        class : 'chat-text',
        type : 'text',
        placeholder : 'Send a Message'
    }).appendTo(chatWriteForm);

    var chatSendIcon = '<paper-icon-button></paper-icon-button>'
    $(chatSendIcon).attr({
        class : 'chat-send',
        icon : 'send'
    }).appendTo(chatWriteForm);

    var chatEmoIcon = '<div></div>'
    $(chatEmoIcon).attr({
        class : 'g-emoticon'
    }).appendTo(chatWriteForm);
    
    var chatSubmit = '<input></input>'
    $(chatSubmit).attr({
        id : 'submit'+formId,
        type : 'submit',
        style : 'height: 0px'
    }).appendTo(chatWriteForm);
}

function writeChatConversation(chatArea, chatMessage) {
//            <!-- reciever -->
//            <div id="text-field" class="col-xs-12 frm-txtfield chat-box-msg" chatType="reciever">
//                <div class="eg chat-box-arrow-top-reciever">
//                    <div class="yw oo chat-box-arrow-reciever"></div>
//                    <div class="yw VK chat-box-arrow-reciever"></div>
//                </div>
//                <div class="chat-msg text-justify">
//                    Hello There
//                </div>
//            </div>
//
//            <!-- sender -->
//            <div id="text-field" class="col-xs-12 frm-txtfield chat-box-msg">
//                <div class="chat-box-arrow-top-sender">
//                    <div class="yw oo chat-box-arrow-reciever"></div>
//                    <div class="yw VK"></div>
//                </div>
//                <div class="chat-msg text-justify">
//                    Hi There Too    
//                </div>
//            </div> 
}

function getMessages(chatHead) {
    // send id : from and to 
}

// Send A Message
var chatUrl = 'new-message/'
var chatFormId;

$('body').on('click', '.chat-send', function() {
    chatFormId = $(this).closest('form').attr("id");
    $('#submit'+chatFormId).trigger('click');
});

$('#chat-rooms').on('submit', 'form', (function(e) {
    e.preventDefault();
    var formData = new FormData(this);
    post(chatUrl, formData);
    e.target.getElementsByClassName('chat-text')[0].value = '';
}));

function minMaxChatRoom(e) {
    var chatArea = e.parentNode.parentElement.parentElement;
    if (chatArea.style.position=='relative')
    {
        chatArea.removeAttribute("style");
    }
    else
    {
        chatArea.style.position='relative';
        chatArea.style.bottom='46px';
    }
}

function exitChatRoom(e) {
    var chatArea = e.parentNode.parentElement.parentElement;
    openedChatRooms.splice( openedChatRooms.indexOf(chatArea.getAttribute('id')), 1 );
    chatArea.remove();
}