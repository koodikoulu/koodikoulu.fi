$(document).ready(function() {

  function createSignUp() {
    var form = $('#signup-form');
    $.ajax({
      url: form.attr('action'),
      type: form.attr('method'),
      data: form.serialize(),
      success: function(data) {
        if (data.status === 200) {
          $('#signup-form').replaceWith('<h3 style="color: green;">Kiitos ilmoittautumisesta!</h3>');
        } else {
          $('#signup-form p.submit-error').text('Jotakin meni pieleen. Yritä uudelleen.');
        }
      },
      error: function(data) {
        $('#signup-form p.submit-error').text('Jotakin meni pieleen. Yritä uudelleen.');
      }
    });
  }

  $('#signup-form').on('submit', function(event) {
    event.preventDefault();
    createSignUp();
    return false;
  });
});
