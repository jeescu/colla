 
//create new article
$('#createArticleForm').on('submit',(function(e) {
    e.preventDefault();
    
    var formData = new FormData(this);

    console.log('Submitting article')
    formArticle = false

    formData.userid = token;
    formData.title = get('article-title').value;
    formData.content = get('article-content').value.replace(/\n/g, "<br />");
    formData.image = postIMAGE || "None";

    $.ajax({
        type:'POST',
        url: 'new-article/',
        data:formData,
        cache:false,
        contentType: false,
        processData: false,
        success:function(data) {
            console.log(formData);
            console.log(data)
            console.log(getQuery('#article-dialog'));
            getQuery('#toastArticle').show();
            getQuery('#article-dialog').toggle()
            formArticle = true;
        },
        error: function(data){
            console.error("error");
        }
    });

}));


function articleImgThumb(input) {
    if (input.files && input.files[0])
    {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#article-thumb').attr('src', e.target.result).height(166);
        };
        reader.readAsDataURL(input.files[0]);
    }
    showArticleThumb();
}

function getArticles() {
     AJAXRequest("article/browse", "GET", null, prepareArticles, "application/json;charset=utf-8", "json")
}

var prepareArticles = function(articles) {
    $("#article-dynamic").empty()
    
    for (article in articles) {
        displayArticles(articles[article])
    }
}

function displayArticles(article) {
    console.log(article)
    var articleForm = '<div class="col-md-6">';
        articleForm+='<paper-shadow class="article-indx-fragment" z="0">';
         articleForm +='  <div class="article-thumb-cover">';
        articleForm +='       <img src="'+article.cover+'"/>';
        articleForm +='   </div>';
         articleForm +='  <div class="article-title"><span>'+article.title+'</span></div>';
        articleForm  +='  <div class="article-content-preview">';
         articleForm +='      <span>'+ (article.content.length > 44) ? article.content.substring(0, 44) + " . ." : article.content; +'</span>';
         articleForm   +='    <div class="article-more">';
        articleForm  +='         <paper-icon-button icon="open-in-new" onclick="" role="button" tabindex="0" aria-label="more-vert"></paper-icon-button>';
        articleForm  +='      </div>';
        articleForm  +='  </div>';
        articleForm  +='  <div class="article-separator"></div>';
         articleForm  +=' <div class="article-author">';
         articleForm +='     <span>';
         articleForm +='          <div class="col-xs-2 comm-av article-card-av"><img src="'+article.pic+'"/></div><b>' + article.display_name +'</b></br>'+ article.date;
         articleForm +='      </span>';
         articleForm  +='     <!-- like article -->';
         articleForm +='      <span>';
         articleForm +='          <paper-icon-button class="article-btn-like"  icon="grade" onclick="" role="button" tabindex="0" aria-label="more-vert"></paper-icon-button>';
         articleForm +='      </span>';
        articleForm+='    </div>';
       articleForm +='</paper-shadow>';
    articleForm+='</div>';
    
    $("#article-dynamic").append(articleForm);
}