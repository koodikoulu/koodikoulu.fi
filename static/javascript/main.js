$(function() {
  var $panels = $('.panel')
  var activeClass = 'active'

  $panels.on('show.bs.collapse', function() {
    $(this).addClass(activeClass)
  })

  $panels.on('hide.bs.collapse', function() {
    $(this).removeClass(activeClass)
  })
})