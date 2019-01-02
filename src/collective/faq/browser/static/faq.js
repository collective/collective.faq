$(function() {
  $('.faq .glyphicon').on('click', function(e) {
    e.preventDefault();
    var $el = $(this);
    if ($el.hasClass('glyphicon-plus')) {
      $el.removeClass('glyphicon-plus');
      $el.addClass('glyphicon-minus');
    } else {
      $el.removeClass('glyphicon-minus');
      $el.addClass('glyphicon-plus');
    }
  });
  $('.faq-toggle-answers').on('click', function(e) {
    e.preventDefault();
    $('.faq .faq-li-question .glyphicon').trigger('click');
  });
  $('.faq-toggle-categories').on('click', function(e) {
    e.preventDefault();
    $('.faq .faq-li-nested .glyphicon').trigger('click');
  });
});
