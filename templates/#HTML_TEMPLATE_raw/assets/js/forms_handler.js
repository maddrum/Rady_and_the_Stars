var $form = $('form#message_form'),
    url = 'https://script.google.com/macros/s/AKfycbxi1ET1_UAltZoUYCLRaZTLTikgSSkdreqk6qHG-wS4r_FDps0r/exec';

$('#submit-form').on('click', function(e) {
  e.preventDefault();
  var jqxhr = $.ajax({
    url: url,
    method: "GET",
    dataType: "json",
    data: $form.serializeObject()
  }).success(
    // do something
  );
});