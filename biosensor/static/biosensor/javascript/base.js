// Handle click on mtp items

$('[class^=circle-]').on( 'click', function() {
  var thisClass = $(this).attr('class');
  thisClass = thisClass.replace('circle-','');
  window.location.href = "/biobrick/" + thisClass;
});

$('.edit-mode').on( 'click', function() {
  $('body').addClass('edit-mode');
  $(this).fadeOut();
});

$('.upload-mode').on( 'click', function(e) {
  e.preventDefault();
  $('body').addClass('upload-mode');
  $(this).fadeOut();
  $(this).parent().next().fadeIn();
});

// Initiate svg4everybody https://github.com/jonathantneal/svg4everybody
svg4everybody();
