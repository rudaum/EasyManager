$(function () {
    $('ul.tree').hide();
    $('label.tree-toggler').click(function () {
        $(this).parent().children('ul.tree').toggle(600);
        if ($(this).text().includes("+")) {
            $(this).text($(this).text().replace("+","-"));
        } else if ($(this).text().includes("-")) {
            $(this).text($(this).text().replace("-","+"));
        }
    });
    $('#tree-toggler').click(function () {
        if ($(this).text().includes("+")) {
            $('ul.tree').show(600);
            $(this).text($(this).text().replace("+","-"));
            $('label.tree-toggler').each(function() {
                $(this).text($(this).text().replace("+","-"))
            });
        } else if ($(this).text().includes("-")) {
            $('ul.tree').hide(600);
            $(this).text($(this).text().replace("-","+"));
            $('label.tree-toggler').each(function() {
                $(this).text($(this).text().replace("-","+"))
            });
        }
    });
});