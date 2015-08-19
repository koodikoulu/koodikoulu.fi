$(document).ready(function() {

  function createSignUp(form) {
    $.ajax({
      url: form.attr('action'),
      type: form.attr('method'),
      data: form.serialize(),
      success: function(data) {
        if (data.status === 200) {
          form.replaceWith('<h3 style="color: green;">Kiitos ilmoittautumisesta!</h3>');
        } else {
          form.find('p.submit-error').text('Jotakin meni pieleen. Yritä uudelleen.');
        }
      },
      error: function(data) {
        $('#signup-form p.submit-error').text('Jotakin meni pieleen. Yritä uudelleen.');
      }
    });
  }

  $('input[type="submit"]').on('click', function(event) {
    event.preventDefault();
    var form = $(this).closest('form');
    createSignUp(form);
    return false;
  });
});
