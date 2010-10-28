function initialize() {
    initMap();
    //Eventhandlers
    
    $('#new_t_button').click(function() {
				 window.location.href='/detail/budapest/'+$('#new_t_name').val();
			     });

			    
}
