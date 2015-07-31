var successDialog = document.getElementById('success-dialog');
var errorDialog = document.getElementById('error-dialog');

$('#registerForm').on('submit', (function(e) {
    e.preventDefault();

    var formData = new FormData(this);

    $.ajax({
        url: '/colla/register/',
        type: 'POST',
        data: formData,
        contentType: false,
        processData: false,
        success: function (data) {
            if (!data.error) {
                successDialog.toggle();
            } else {
                errorDialog.toggle();
            }
        },
        error: function (ts) {
            console.log(ts);
            console.error('Registration Error');
        }
    });
}));

function tog() {
    successDialog.toggle();
}