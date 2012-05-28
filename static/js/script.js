/* Author: Temiyemi Agbetunsin @temiyemi */

if (!Array.prototype.every)
{
    Array.prototype.every = function(fun /*, thisp*/)
    {
        var len = this.length;
        if (typeof fun != "function")
            throw new TypeError();

        var thisp = arguments[1];
        for (var i = 0; i < len; i++)
        {
            if (i in this &&
                !fun.call(thisp, this[i], i, this))
                return false;
        }

        return true;
    };
}

if (!Array.prototype.filter) {
    Array.prototype.filter = function(fun /*, thisp*/) {
        var len = this.length >>> 0;
        if (typeof fun != "function") {
            throw new TypeError();
        }

        var res = [];
        var thisp = arguments[1];
        for (var i = 0; i < len; i++) {
            if (i in this) {
                var val = this[i]; // in case fun mutates this
                if (fun.call(thisp, val, i, this)) {
                    res.push(val);
                }
            }
        }

        return res;
    };
}

$(document).ready(function(){
	
	// temporary redirection function to forms
	$('button.forms').click(function(){
		$form = $(this).html(),
		location.href = 'forms_' + $form.slice(4).toLowerCase() + 's.html'; 
	});
	
	// temporary redirection function to profiles
	$('table.projects tbody, table.partners tbody, table.recipients tbody')
		.on('click','td:first-child', function(){
			var $this = $(this),
			    $parent = $this.parents('table');
			location.href = 'profile_' + $parent.attr('class').slice(0,-1) + '.html';
		})
	;

    var show_all = function(collection){
        $(collection).show('fast');
    };

    var projects = $('table.projects tbody tr:not(.empty)');

    $('form.filters').on({
        'submit': function(e){
            e.preventDefault();
            var filters = new Object,
                fields  = $(this).serialize().split('&');
            $.each(fields, function(){
                var field = this.split('=');
                filters[field[0]] = field[1];
            });

            //= Filters: status | year | cost | duration | industry | sector
            var set_filters = ['status','year','cost','duration','sector','industry'].filter(
                function(element){
                    return filter_has_value(filters[element]);
                }
            );

            // if no filter is set
            if (set_filters.length == 0) return;
            else {
                var $projects = projects;
                $projects.hide('fast');
                $.each(set_filters, function(index,filter){
                    switch (filter){
                        case 'year':
                        case 'cost':
                        case 'duration':
                            $projects = $projects.filter_rows(filter,parseInt(filters[filter]),filters['eval_'+filter]);
                            break;
                        default:
                            $projects = $projects.filter_rows(filter,filters[filter]);
                    }
                });
                if ($projects.length > 0) {
                    $('table.projects tbody tr.empty').remove();
                    $projects.show('fast');
                }
                else {
                    if ($('table.projects tbody tr.empty').length < 1)
                        $('<tr class="empty">')
                            .html('Search returned no result set')
                            .appendTo($(projects).parents('tbody')[0]);
                }
            };
        },
        'reset': function(){
            projects.show('fast');
        }
    });

    var filter_has_value = function(value){
        if (/^Any/.test(value) || 'any'==value || ''==value || !value) return false;
        else return true;
    };

});