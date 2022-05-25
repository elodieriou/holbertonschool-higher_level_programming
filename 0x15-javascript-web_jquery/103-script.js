$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const languageCode = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + languageCode, function (data) {
      $('DIV#hello').html(data.hello);
    });
  });

  $('INPUT#language_code').keypress(function (event) {
    if (event.key === 'Enter') {
      $('INPUT#btn_translate').click();
    }
  });
});
