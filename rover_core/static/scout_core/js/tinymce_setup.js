
// Map Django language codes to valid TinyMCE language codes.
// There's an entry for every TinyMCE language that exists,
// so if a Django language code isn't here, we can default to en.

var language_codes = {
    'ar': 'ar',
    'ca': 'ca',
    'cs': 'cs',
    'da': 'da',
    'de': 'de',
    'es': 'es',
    'et': 'et',
    'fa': 'fa',
    'fa_IR': 'fa_IR',
    'fi': 'fi',
    'fr': 'fr_FR',
    'hr_HR': 'hr',
    'hu': 'hu_HU',
    'id_ID': 'id',
    'is_IS': 'is_IS',
    'it': 'it',
    'ja': 'ja',
    'ko': 'ko_KR',
    'lv': 'lv',
    'nb': 'nb_NO',
    'nl': 'nl',
    'pl': 'pl',
    'pt_BR': 'pt_BR',
    'pt_PT': 'pt_PT',
    'ru': 'ru',
    'sk': 'sk',
    'sr': 'sr_Latn',
    'sv': 'sv_SE',
    'tr': 'tr',
    'uk': 'uk_UA',
    'vi': 'vi',
    'zh_CN': 'zh_CN',
    'zh_TW': 'zh_TW'
};

function custom_file_browser(field_name, url, type, win) {
    tinyMCE.activeEditor.windowManager.open({
        title: 'Select ' + type + ' to insert',
        file: window.__filebrowser_url + '?pop=5&type=' + type,
        width: 800,
        height: 500,
        resizable: 'yes',
        scrollbars: 'yes',
        inline: 'yes',
        close_previous: 'no'
    }, {
        window: win,
        input: field_name
    });
    return false;
}

jQuery(function($) {

    if (typeof tinyMCE != 'undefined') {

        tinyMCE.init({
            selector: "textarea.mceEditor",
            width: '800px',
            height: '200px',
            language: language_codes[window.__language_code] || 'pt_BR',
            plugins: [
                "advlist autolink lists link image charmap print preview hr anchor",
                "searchreplace wordcount visualblocks visualchars code fullscreen",
                "insertdatetime media nonbreaking table contextmenu paste imagetools",
                "directionality template textcolor colorpicker textpattern autoresize"

                // "advlist autolink lists link image charmap print preview hr anchor pagebreak",
                // "searchreplace wordcount visualblocks visualchars code fullscreen",
                // "insertdatetime media nonbreaking save table contextmenu directionality",
                // "emoticons template paste textcolor colorpicker textpattern imagetools"
            ],
            link_list: '/displayable_links.js',
            relative_urls: false,
            convert_urls: false,
            menubar: false,
            statusbar: true,
            toolbar: ("insertfile undo redo | styleselect | bold italic | " +
                      "alignleft aligncenter alignright alignjustify | " +
                      "bullist numlist outdent indent | link image table | " +
                      "code fullscreen"),
            file_browser_callback: custom_file_browser,
            content_css: window.__tinymce_css,

            // BUTTONS
            toolbar1: "undo redo | styleselect fontselect fontsizeselect formatselect | link image media | code fullscreen ",
            toolbar2: "bold italic underline | forecolor backcolor | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | table blockquote removeformat",
            forced_root_block : '',
            autoresize_on_init: true,
            autoresize_bottom_margin: 20,
            fontsize_formats: "8pt 10pt 12pt 14pt 16pt 18pt 20pt 22pt 24pt 26pt 28pt 30pt 23pt 34pt 36pt 38pt 40pt",

            // permite a tag style dentro do body do tiny_mce
            valid_elements : '*[*]',
            valid_children : "+body[style],p[strong|a|#text]",

            resize: "both"
        });


        // TEXTAREA.SIMPLE
        tinyMCE.init({
            selector: "textarea.simple",
            width: '800px',
            height: '80px',
            language: language_codes[window.__language_code] || 'pt_BR',
            plugins: [
                "advlist autolink lists link image charmap print preview hr anchor",
                "searchreplace wordcount visualblocks visualchars code fullscreen",
                "insertdatetime media nonbreaking table contextmenu paste imagetools",
                "directionality template textcolor colorpicker textpattern"

                // "advlist autolink lists link image charmap print preview hr anchor pagebreak",
                // "searchreplace wordcount visualblocks visualchars code fullscreen",
                // "insertdatetime media nonbreaking save table contextmenu directionality",
                // "emoticons template paste textcolor colorpicker textpattern imagetools"
            ],
            link_list: '/displayable_links.js',
            relative_urls: false,
            convert_urls: false,
            menubar: false,
            statusbar: true,
            toolbar: ("insertfile undo redo | styleselect | bold italic | " +
                      "alignleft aligncenter alignright alignjustify | " +
                      "bullist numlist outdent indent | link image table | " +
                      "code fullscreen"),
            file_browser_callback: custom_file_browser,
            content_css: window.__tinymce_css,

            // BUTTONS
            toolbar1: "undo redo | styleselect fontselect fontsizeselect formatselect | link image media | code fullscreen ",
            toolbar2: "bold italic underline | forecolor backcolor | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | table blockquote removeformat",
            forced_root_block : '',
            fontsize_formats: "8pt 10pt 12pt 14pt 16pt 18pt 20pt 22pt 24pt 26pt 28pt 30pt 23pt 34pt 36pt 38pt 40pt",

            // permite a tag style dentro do body do tiny_mce
            valid_elements : '*[*]',
            valid_children : "+body[style],p[strong|a|#text]",

            resize: "both"
        });
    }
});