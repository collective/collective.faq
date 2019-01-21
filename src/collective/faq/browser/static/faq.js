$(function() {
  $('.faq .glyphicon, .faq-question').on('click', function(e) {
    e.preventDefault();
    var $el = $(this);
    if ($el.hasClass('faq-question')) {
      $el = $el.prev('.glyphicon');
    }
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
    var state = $('.faq .faq-li-question .glyphicon').first().hasClass('glyphicon-plus');
    if (state) {
      $('.faq .faq-li-question .glyphicon-plus').trigger('click');
    } else {
      $('.faq .faq-li-question .glyphicon-minus').trigger('click');
    }
  });
});
