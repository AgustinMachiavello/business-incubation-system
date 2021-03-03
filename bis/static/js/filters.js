var urlParams = new URLSearchParams(window.location.search);

function onFilterChange(obj) {
    if ($(obj).is(':checked')) {
        insertParam(obj.dataset.paramname, obj.value);
    }
    else {
        removeParam(obj.dataset.paramname);
    }
}

function onActiveFilterClick(obj) {
    console.log(obj.dataset.paramname)
    removeParam(obj.dataset.paramname);
}

$(document).ready(function(){
    document.getElementById('remove_filters').addEventListener('click', function(){
        removeAllParam();
    })
});


// Set checkbox as checked if parameter is in URL
window.addEventListener('load', function () {
    $('.form-check-input').each(function(i, obj) {
        param = urlParams.get(obj.dataset.paramname);
        if (param) {
            if (obj.value == param) {
                obj.setAttribute("checked", "checked");
            }
        }
        else {
        }
    });
})

// Filter dates report page
$(document).ready(function(){

    $('#reportDateRangeFrom').change(function() {
        dateFrom = $(this).val();
        dateFrom = dateFrom.split('/');
        dateFrom = dateFrom.join('-');
        insertParam('date_from', dateFrom);
    });

    $('#reportDateRangeTo').change(function() {
        dateTo = $(this).val();
        dateTo = dateTo.split('/');
        dateTo = dateTo.join('-')
        insertParam('date_to', dateTo)
    });
});