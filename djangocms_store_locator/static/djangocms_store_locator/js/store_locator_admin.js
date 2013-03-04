$j = django.jQuery
try {
	get_lat_long_url = get_lat_long_url + '?q=';
}
catch(err) {
	get_lat_long_url = window.location.href + '../get_lat_long/?q=';
	get_lat_long_url = get_lat_long_url.replace(/#/g, '');
}

$j(document).ready(function() {

	var button = $j('<div style="margin:10px 0 0 105px"><a href="" class="button">Get lat/long from Google Maps</a></div>');
	$j('.form-row.field-address div').append(button);

	button.bind('click', function(e) {
		e.preventDefault();
		var address = $j("textarea#id_address").val().replace(/\n/g, ', ').replace('\n', ', ');
		$j.get(get_lat_long_url + address, function(data, code) {
			$j("input#id_latitude").val(data.split(",")[0]);
			$j("input#id_longitude").val(data.split(",")[1]);
		});
	});
});
