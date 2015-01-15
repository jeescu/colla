var successDialog = document.getElementById('success-dialog');

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
            console.info('Registered');
            successDialog.toggle();
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