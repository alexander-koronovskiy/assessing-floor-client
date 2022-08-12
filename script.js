$('#file-input').focus(function() {
     $('label').addClass('focus');
})
.focusout(function() {
     $('label').removeClass('focus');
});