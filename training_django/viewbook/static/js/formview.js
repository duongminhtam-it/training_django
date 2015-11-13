function getCookie(name){
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			if (cookie.substring(0, name.length + 1) == (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
$(document).ready(function() {
	$(".delete").click(function(event) {
		$.ajax({
			url: '/viewbook/',
			type: 'deletett',
			data: {'id': $(this).attr("id")},
            beforeSend: function(xhr, settings){
                console.log(xhr);
                console.log(settings);
                console.log((!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))));
				if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
					xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
				}
			},
		})
		.done(function() {
			console.log("success");
		})
		.fail(function() {
			console.log("error");
		})
		.always(function() {
			console.log("complete");
		});
		return false;
	});
});