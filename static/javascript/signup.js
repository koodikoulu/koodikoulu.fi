$(document).ready(function() {

  function createSignUp(form, input) {
    $.ajax({
      url: form.attr('action'),
      type: form.attr('method'),
      data: form.serialize(),
      success: function(data) {
        if (data.status === 200) {
          form.replaceWith('<h3 style="color: green;">Kiitos ilmoittautumisesta!</h3>');
        } else {
          input.show();
          $('#loader').remove();
          form.find('p.submit-error').text('Jotakin meni pieleen. Yritä uudelleen.');
        }
      },
      error: function(data) {
        input.show();
        $('#loader').remove();
        form.find('p.submit-error').text('Jotakin meni pieleen. Yritä uudelleen.');
      }
    });
  }

  $('input[type="submit"]').on('click', function(event) {
    event.preventDefault();
    var form = $(this).closest('form');
    var input = $(this);
    input.after($('<img src="/static/media/ajax-loader.gif" alt="loading" id="loader">'));
    input.hide();
    createSignUp(form, input);
    return false;
  });
});
