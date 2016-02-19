$(document).ready(function () {
    new Clipboard('#copy');

    $.ajaxSetup({
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-XSRFToken", $('input[name=_xsrf]').val());
        }
    });

    $('#generate').click(function () {
        $('.notification').addClass('hide');

        var longUrl = $('#longurl').val();

        $.post('/short', { url: longUrl }, function (shortUrl) {
            $('#orignalurl').attr('href', longUrl).text(longUrl);
            $('#shorturl').attr('href', shortUrl).text(shortUrl);
            $('#copy').attr('data-clipboard-text', shortUrl);
            $('.result-data').removeClass('hide');

            $.post('/clicks', { url: shortUrl }, function (clickCount) {
                $('#click-count').attr('title', clickCount + ' clicks').find('span').text(clickCount);
            });
        })
        .fail(function () {
            $('.notification').removeClass('hide');

            setTimeout(function () {
                $('.notification').addClass('hide');
            }, 10 * 1000);
        });
    });

    $('#copy').click(function () {
        $(".copied").fadeIn(700, function(){
            window.setTimeout(function(){
                $('.copied').fadeOut();
            }, 2 * 1000);
        });
    });
});