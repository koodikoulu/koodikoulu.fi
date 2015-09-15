$(function() {
  var $panels = $('.panel')
  var activeClass = 'active'

  // Active class for togglable panels.

  $panels.on('show.bs.collapse', function() {
    $(this).addClass(activeClass)
  })
  $panels.on('hide.bs.collapse', function() {
    $(this).removeClass(activeClass)
  })

  // Scroll window to content when toggling accordion panels.

  $('#accordion').on('shown.bs.collapse', function (e) {
    $('html,body').animate({
      scrollTop: $($(e.target).find('.panel-body')).offset().top - 115
    }, 100)
  })

  $('.flash .close').click(function() { $('.flash').slideUp() })

})