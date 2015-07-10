var openedChatRooms = ['rooms']
var chatIdListener = []

// Open new chat
$('.open-chat-head').click(function(e) {
    var chatHead = e.currentTarget;
    
    prepareChatArea(chatHead)
    
    // Start updating messages
    // updateChatmessages()
});

function prepareChatArea(chatArea) {
    var chatUserName = chatArea.getElementsByClassName('detail-board')[0].innerHTML
    var chatUserId = chatArea.getElementsByTagName('input')[0].value
    var chatRoom = $('#chat-rooms')
    
    var chats = 1;
    
    // Write chat area
    if (openedChatRooms.indexOf(chatUserId) < 0)
    {
        openedChatRooms.push(chatUserId);
        writeChatArea(chatUserId, chatUserName, chatRoom);
        // Get messages
        getMessages(chatUserId, token)
    }
                 
}

var getElemByAtrrVal = function (e, attr, val) {
    return $(e+'['+attr+'='+val+']')
}

function writeChatArea(chatUserId, chatUserName, chatRoom) {    

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

    if (chatUserName.length > 22) {
        chatUserName = chatUserName.substring(0, 22) + " . .";
    }
    
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

//temp
function writeChatConversation(messageData, rcvr) {
    var chatId = 'contentMsgchat'+rcvr;
    var div = '<div></div>'
    
    var msgCnt = 1;
    for (message in messageData) {
        
        if (typeof(messageData[message]) == 'object')
        {
            
            if (messageData[message].user_id != token)
            {
                var reciever_msg='';
                var msgIdRcvr = 'chat-msg-'+messageData.chat_id+'-'+msgCnt;
                // Reciever
                reciever_msg += '<div id="text-field" class="col-xs-12 frm-txtfield chat-box-msg" chatType="reciever">';
                reciever_msg += '<div class="eg chat-box-arrow-top-reciever"><div class="yw oo chat-box-arrow-reciever">';
                reciever_msg += '</div><div class="yw VK chat-box-arrow-reciever"></div></div>';
                reciever_msg += '<div class="chat-msg text-justify"><p id="'+msgIdRcvr+'"></p></div></div>'                         
                $('#'+chatId).append(reciever_msg);
                $('#'+msgIdRcvr).text(messageData[message].message)
            }
            else
            {
                var msgIdSndr = 'chat-msg-'+messageData.chat_id+'-'+msgCnt;
                var sender_msg='';
                sender_msg += '<div id="text-field" class="col-xs-12 frm-txtfield chat-box-msg">';
                sender_msg += '<div class="chat-box-arrow-top-sender"><div class="yw oo chat-box-arrow-reciever">';
                sender_msg += '</div><div class="yw VK"></div></div>';
                sender_msg += '<div class="chat-msg text-justify"><p id="'+msgIdSndr+'"></p></div></div>';
                $('#'+chatId).append(sender_msg);
                $('#'+msgIdSndr).text(messageData[message].message)
            }
            msgCnt++;
        }
    }

    // Add chat id to Listener
    chatIdListener.push(messageData.chat_id);
        
    // Add id to chat contentMsgchat elem
    $('#'+chatId).attr('chat_id', messageData.chat_id);
     
    console.log('the listener: '+chatIdListener)
    
}

function getMessages(reciever, sender) {
    var users = {
        'sender' : sender,
        'reciever' : reciever
    }
    
    $.get( "get-messages", users )
    .done(function( data ) {
        writeChatConversation(data, reciever)
    });
}

// Update messages
function updateChatMessages() {
    
    setInterval( function() {
        
        if (chatIdListener.length != 0)
        {  
            // Send Multiple Opened Chat Id's
            var chatIds = {}
            chatIds.chats = chatIdListener
            
            $.get( "get-update-messages", chatIds )
            .done(function( data ) {
                
                // write updates
                for (chatConv in data) {
                    var reciever = $('div[chat_id='+chatConv.chat_id+']').attr('id');
                    $('div[chat_id='+chatConv.chat_id+']').empty();
                    writeChatConversation(data, reciever.split('t')[3])
                }
            });
        }
        else
        {
            // Do nothing
        }
        
    }, 1000 );
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
    var chatAreaId = chatArea.getAttribute('id')
    
    openedChatRooms.splice( openedChatRooms.indexOf(chatAreaId), 1 );
    
    var chatMessageId = document.getElementById('contentMsgchat'+chatAreaId).getAttribute('id');
    chatIdListener.splice( openedChatRooms.indexOf(chatMessageId), 1 );
    
    console.log('the listener: '+chatIdListener)
    
    chatArea.remove();
}