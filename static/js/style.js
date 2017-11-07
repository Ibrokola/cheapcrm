
$(document).ready(function() {

    $('#gi-container').delegate('.edit-account', 'click', function(e) {
        e.preventDefault();
        $('#gi-container').load($(this).attr('href'));
    });
});