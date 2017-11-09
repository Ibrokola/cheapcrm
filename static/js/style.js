
$(document).ready(function() {
    $('#gi-container').delegate('.edit-account', 'click', function(e) {
        e.preventDefault();
        $('#gi-container').load($(this).attr('href'));
    });


    // Contact - AJAX to get the Contact Add form
    $('#cd-container').delegate('#new-contact', 'click', function(e){
        e.preventDefault();
        $.get($(this).attr('href'), function(data) {
            $('#cd-body').append(data);
            $('#new-contact').hide();
        });
    });

    // Contact - Use AJAX to get the Contact Edit form
    $('#cd-container').delegate('.edit-contact', 'click', function(e) {
        e.preventDefault();
        var that = $(this);
        $.get($(this).attr('href'), function(data) {
            $('#new-contact').hide();
            that.parent().parent().remove();
            $('#cd-body'.append(data))
        });
    });

    // Contact - Use AJAX to save the Contact Add Form
    $('#cd-container').delegate('#contact-form', 'submit', function(e) {
        e.preventDefault();
        var form = $('#contact-form');
        var url = form.attr('action');
        $.post(url, form.serialize(), function(data) {
            if ($(data).find('.errorlist').html()) {
                // If the contact form is returned we know there are errors
                $('#new-contact').hide();
                $('#cd-body').append(data);
            }else{
                // Otherwise insert the row into the table
                $('#cd-table tr:last').after(data);
                $('#new-contact').show();
            }
        });
        $(this).remove(); // Remove the form
    });

    // Communications - Whne the Subject of the form is clicked, the whole form
    $('#co-container').delegate('#id_subject', 'focus', function() {
        $('#comm-form-internals').show()
    });


    // Communications - Use AJAX to get the Communications Add From
    $('#co-container').delegate('#new-comm', 'click', function(e) {
        e.preventDefault();
        $.get($(this).attr('href'), function(data){
            $('#co-list').prepend(data);
        })
    });

    // Communication - Use AJAX to get the Comm Edit Form
    $('#co-container').delegate('.comm-edit', 'click', function(e){
        e.preventDefault();
        var that = $(this)
        $.get($(this).attr('href'), function(data){
            $('#co-body').find('#comm-form').remove();
            $('#co-form-wrapper').append(data);
            $('#comm-form-internals').show();
            that.parent().parent().parent().remove();
        })
    });


    // Communications - Use AJAX to save the Comm Add Form
    $('#co-container').delegate('#comm-form', 'submit', function(e) {
        e.preventDefault();
        var form = $('#comm-form');
        var url = form.attr('action');
        $.post(url, form.serialize(), function(data) {
            if($(data).find('#comm-form-internals').html()){
                // If form comes back then display it properly
                form.remove()
                $('#co-form-wrapper').prepend(data); // Appends the newly created Communication
                $('#comm-form-internals').show(); // Make sure it shows
                $('#comm-form').attr('action','/comm/new/') //Make sure the action is set to new 
            }else {
                // When is this supposed to kick in?
                resetForm($('#comm-form')); //Reset the form values
                $('#comm-form').find('ul').remove(); // If there are any error
                $('#comm-form-internals').hide(); // Hides everything but the subject
                $('#co-list').prepend(data); // Appends the newly created Communication
                $('#comm-form').attr('action','/comm/new/'); // Make sure the action is set to new
            }
        })
    });


});



