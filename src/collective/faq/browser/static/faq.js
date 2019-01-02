$(function() {
  $('.faq li > .glyphicon').on('click', function(e) {
    e.preventDefault();
    var $el = $(this);
    $el.toggleClass(function() {
      if ($el.hasClass('glyphicon-plus')) {
        $el.removeClass('glyphicon-plus');
        return 'glyphicon-minus';
      } else {
        $el.removeClass('glyphicon-minus');
        return 'glyphicon-plus';
      }
    });
  });
});
