$(document).ready(function() {

  function createSignUp(form, input, loader) {
    $.ajax({
      url: form.attr('action'),
      type: form.attr('method'),
      data: form.serialize(),
      success: function(data) {
        form[0].reset();
        var message = form.find('p.submit-message');
        message.text('Kiitos ilmoittautumisesta!');
        message.css('color', 'green');
        input.show();
        loader.remove();
      },
      error: function(data) {
        var message = form.find('p.submit-message');
        message.text('Jotakin meni pieleen. Yritä uudelleen.');
        message.css('color', 'red');
        input.show();
        loader.remove();
      }
    });
  }

  $('input[type="submit"]').on('click', function(event) {
    event.preventDefault();
    var form = $(this).closest('form');
    var input = $(this);
    var loader = $('<img src="/static/media/ajax-loader.gif" alt="loading" id="loader">');
    input.after(loader);
    input.hide();
    createSignUp(form, input, loader);
    return false;
  });
});
