function onSubmit() {
  $.ajax({
    url: "/ai_request/",
    type: "post",
    data: {'input': $("#input_box").val()}
  }).done(function(data) {
    $("#ai_output").html(data.output)
  });
}
