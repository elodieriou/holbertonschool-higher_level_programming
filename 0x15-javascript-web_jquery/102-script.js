$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const languageCode = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + languageCode, function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
