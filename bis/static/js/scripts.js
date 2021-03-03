/**
 * Function for toggling the sidebar on click
 */
$(document).ready(function () {
    $("#sidebar-toggle").click(function(e) {
      e.preventDefault();
      $("#wrapper").toggleClass("toggled");
    });
});

/**
 * Copy email to clipboard
 */
$(document).ready(function() {
	var element = $('a.copy-email');
	var msgSuccess = 'Dirección copiada al portapapeles';

	// Disable default action
	$('a.copy-email').click(function() {
		return false;
	})

	// Store email in a variable.
	element.click(function() {
		var email = $(this).attr('href');
		copyToClipboard(email);
	});

});

// From StackOverflow
function copyToClipboard(text) {
    var dummy = document.createElement("input");
    document.body.appendChild(dummy);
    dummy.setAttribute('value', text);
    dummy.select();
    document.execCommand('copy');
    document.body.removeChild(dummy);
    console.log('copied to clipboard: ', text)
}

// From W3 school
function copyToClipboardMain() {
    /* Get the text field */
    var copyText = document.getElementById("copy-to-clipboard").getAttribute('data-copy');
    copyToClipboard(copyText)
}


/**
 * Functions for filtering
 */
jQuery.expr[':'].Contains = function (a, i, m) {
    return jQuery(a).text().toUpperCase().indexOf(m[3].toUpperCase()) >= 0;
};

$(function () {
    $('#searchbox').on('keyup', function () {
        var w = $(this).val();
        if (w) {
            $('#list .name').parent().hide();            
            $('#list .name:Contains(' + w + ')').parent().show();
        } else {
            $('#list .name').parent().show();
        }
    });
});

// Add parameter to url and refresh page
function insertParam(key, value) {
    key = encodeURIComponent(key);
    value = encodeURIComponent(value);

    // kvp looks like ['key1=value1', 'key2=value2', ...]
    var kvp = document.location.search.substr(1).split('&');
    let i=0;

    for(; i<kvp.length; i++){
        if (kvp[i].startsWith(key + '=')) {
            let pair = kvp[i].split('=');
            pair[1] = value;
            kvp[i] = pair.join('=');
            break;
        }
    }

    if(i >= kvp.length){
        kvp[kvp.length] = [key,value].join('=');
    }

    // can return this or...
    let params = kvp.join('&');

    // reload page with new params
    document.location.search = params;
}

function removeParam(parameter) {
    //prefer to use l.search if you have a location/link object
    var urlparts = window.location.search.split('?');
    if (urlparts.length >= 2) {

        var prefix = encodeURIComponent(parameter) + '=';
        var pars = urlparts[1].split(/[&;]/g);

        //reverse iteration as may be destructive
        for (var i = pars.length; i-- > 0;) {
            //idiom for string.startsWith
            if (pars[i].lastIndexOf(prefix, 0) !== -1) {
                pars.splice(i, 1);
            }
        }
        var url = urlparts[0] + (pars.length > 0 ? '?' + pars.join('&') : '');
        document.location = url;
    }
}

function removeAllParam() {
    document.location = String(document.location).split('?')[0];
}

// Filter table
$(document).ready(function(){
  $("#searchbox_text").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#searchtable tbody tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

// Datepicker
$(document).ready(function() {
    $('.datepicker').each(function(i){
        $(this).datepicker($.datepicker.regional[ "es" ]);
    });
});

// Loading progress bar

$(document).ready(function() {
    $('#sidebar-wrapper a:not(.dropdown-toggle)').bind('click', function() { 
            $('.progress-animation-wrapper').show();
    });
    $('#nav-dropdown a:not(.dropdown-toggle)').bind('click', function() { 
        $('.progress-animation-wrapper').show();
    });
});

//this will wait for the text assets to be loaded before calling this (the dom.. css.. js)
$(document).ready(function() {
    // do something...
    console.log('ready')
});

//this will wait for all the images and text assets to finish loading before executing
$(window).on("load", function () {
    $('.progress-animation-wrapper').hide()
    console.log('load')
});