$(function() {
  var $panels = $('.panel')
  var activeClass = 'active'
  var display = false;

  // Active class for togglable panels.

  $panels.on('show.bs.collapse', function() {
    $(this).addClass(activeClass)
  })
  $panels.on('hide.bs.collapse', function() {
    $(this).removeClass(activeClass)
  })

  $('.more').click(function() {
    $('.more-container').show();
    $('.more').hide();
  })

  $('.less').click(function() {
    $('.more-container').hide();
    $('.more').show();
  })

  // Scroll window to content when toggling accordion panels.

  $('#accordion').on('shown.bs.collapse', function (e) {
    $('html,body').animate({
      scrollTop: $($(e.target).find('.panel-body')).offset().top - 115
    }, 100)
  })

  $('.flash .close').click(function() { $('.flash').slideUp() })

})