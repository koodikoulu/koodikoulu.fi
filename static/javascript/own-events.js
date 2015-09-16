$(document).ready(function() {

  function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method))
  }

  function removeParticipant(id) {
    $.ajaxSetup({
      beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader('X-CSRFToken', Cookies.get('csrftoken'))
        }
      }
    })
    
    $.ajax({
      url: '/participant/' + id + '/',
      type: 'POST',
      success: function(data) {
        $('.participant-' + id).remove()
      },
      error: function(data) {
        alert('Jotakin meni pieleen: ' + data.statusText)
      }
    })

  }

  $('input[type="submit"]').on('click', function(event) {
    var answer = confirm('Haluatko varmasti poistaa osallistujan?')
    if (answer) {
      removeParticipant($(this).attr('name'))
    }
  })

})
