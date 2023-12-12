function onPageLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/location"; // Adjust the URL as per your Flask route
    $.get(url, function(data, status) {
        console.log("got response for get_location_names request");
        if (data && data.locations) {
            var locations = data.locations;
            for (var i = 0; i < locations.length; i++) {
                var opt = '<option>' + locations[i] + '</option>'; // Corrected line
                $('#uiLocations').append(opt);
            }
        }
    });
     
}
window.onload = onPageLoad;



$(document).ready(function() {
    $('#pricePredictionForm').submit(function(event) {
        // Prevent the default form submission
        event.preventDefault();

        // Get form data
        var formData = $(this).serialize();

        // Send an AJAX POST request
        $.ajax({
            type: 'POST',
            url: '/',
            data: formData,
            success: function(response) {
                // Store form data before resetting the form
                var formInputs = $('#pricePredictionForm').serializeArray();

                // Display the response
                $('.output').removeClass('hidden');
                $('.output h1').text(response); // Assuming the response contains 'prediction' data

                // Reset the form
                $('#pricePredictionForm')[0].reset();

                // Repopulate form fields with stored data
                $.each(formInputs, function(index, input) {
                    $('[name="' + input.name + '"]').val(input.value);
                });
            },
            error: function(error) {
                console.log('Error:', error);
            }
        });
    });
});
