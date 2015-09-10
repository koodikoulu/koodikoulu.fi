$(function() {
  $('.startdate').datepicker({
      dateFormat: 'dd.mm.yy'
  });
  $('.enddate').datepicker({
      dateFormat: 'dd.mm.yy'
  });

  organizeForm($('form.organize-form'))

  function organizeForm($form) {
    var $submits = $form.find('[type=submit]')
    var $spinner = $form.find('.spinner')

    function formState($form) {
      return R.mergeAll(
        $form.serializeArray().map(function(o) {
          var obj = {}
          obj[o.name] = o.value
          return obj
        }))
    }

    var requiredKeys = $form.find('label.required')
        .map(function(i, el) {
          return $(el).attr('for').split('_')[1]
        }).get()

    $form.find('input').keyup(function() {
      var data = formState($form)
      var formValid = requiredKeys.map(function(key) {
        return !R.isEmpty(data[key])
      }).reduce(function(a, b) { return a && b })
      $submits.prop('disabled', !formValid)
    })

    // Set time to 00 or round it if value is not allowed
    $form.find('.time').focusout(function() {
      console.log($(this).val())
      var time = Math.round($(this).val()) ? Math.abs(Math.round($(this).val())) : '00';
      $(this).val(time)
    })

    $form.submit(function(e) {
      e.preventDefault()
      $form.find('.submit-message').hide()
      $spinner.show()
      $submits.prop('disabled', true)

      $.ajax({
        url: $form.attr('action'),
        type: $form.attr('method'),
        data: $form.serialize(),

        success: function(res) {
          $spinner.hide()
          $form.trigger('reset')
          $submits.prop('disabled', false)
          $form.find('.submit-message.success').fadeIn().delay(6000).fadeOut()
        },

        error: function(res) {
          $spinner.hide()
          $submits.prop('disabled', false)
          $form.find('.submit-message.error').fadeIn().delay(6000).fadeOut()
        }
      })
    })
  }
})