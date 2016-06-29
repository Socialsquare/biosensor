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

// Hide image and show input on report edit pages
$('.upload-mode').on( 'click', function(e) {
  e.preventDefault();
  $(this).parent().next().show().trigger('click');
  $(this).parent().hide();
});

// Initiate svg4everybody https://github.com/jonathantneal/svg4everybody
svg4everybody();

// Upload file text update
var inputs = document.querySelectorAll( '.inputfile' );
Array.prototype.forEach.call( inputs, function( input )
{
	var label	 = input.parentElement;
	var labelVal = label.innerHTML;

	input.addEventListener( 'change', function( e )
	{
		// var fileName = '';
		// if( this.files && this.files.length > 1 )
		// 	fileName = ( this.getAttribute( 'data-multiple-caption' ) || '' ).replace( '{count}', this.files.length );
		// else
		fileName = e.target.value.split( '\\' ).pop();

		if( fileName )
			label.querySelector( 'span' ).innerHTML = fileName;
		else
			label.innerHTML = labelVal;
	});
});
