function readImage(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#thumb')
                    .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}


$('#update_profile_form').on('submit', (function(e) {
    e.preventDefault();
    
    var formData = new FormData(this);
    
        $.ajax({
            type:'POST',
            url: 'update-profile/',
            data:formData,
            cache:false,
            contentType: false,
            processData: false,
            success:function(data) {
                document.querySelector('#success_update').show();
                console.log(data);
            },
            error: function(data){
                document.querySelector('#error_update').show();
            }
    });
}));


// EXERCISE
function writeReturn(obj) {
    for ( i=0; i<10; i++ ) {
        var newDiv = '<div></div>'
        var ls = '<h2></h2>';
        var parent = $('#json_text');
        
        $(newDiv).attr({
            style : 'border: 2px solid #546E7A',
            class : 'col-md-6 text-center'
        }).appendTo(parent);
        
        for ( n in obj ) {
            $(ls).html(n +' : '+obj[n]).appendTo(parent.find('div').last().prepend())
        }
    }
}

// js ajax
function loadJSON() {
	var xmlhttp;
	if ( window.XMLHttpRequest ) {
	  xmlhttp=new XMLHttpRequest();
	}

	xmlhttp.onreadystatechange=function() {
        if ( xmlhttp.readyState==4 && xmlhttp.status==200 ) {
            writeReturn(xmlhttp.response);
        }
    }

	xmlhttp.open("GET",'/static/colla/data.json',true);
    xmlhttp.responseType = 'json';
	xmlhttp.send();
}

//jquery ajax
function loadJSONJquery() {
    $.ajax({
        type:'GET',
        url: '/static/colla/data.json',
        success: function(data) {
            writeReturn(data);
        },
        error: function(data){
            console.log('Error');
        }
    });
    
//    $.getJSON('/static/colla/data.json', function(data) {
//         writeReturn(data);
//    });
}
