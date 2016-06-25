// Handle click on mtp items

$('[class^=circle-]').on( 'click', function() {
  var thisClass = $(this).attr('class');
  thisClass = thisClass.replace('circle-','');
  window.location.href = "/biobrick/" + thisClass;
});

// Initiate svg4everybody https://github.com/jonathantneal/svg4everybody
svg4everybody();
