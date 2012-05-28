
// usage: log('inside coolFunc', this, arguments);
// paulirish.com/2009/log-a-lightweight-wrapper-for-consolelog/
window.log = function(){
  log.history = log.history || [];   // store logs to an array for reference
  log.history.push(arguments);
  if(this.console) {
    arguments.callee = arguments.callee.caller;
    var newarr = [].slice.call(arguments);
    (typeof console.log === 'object' ? log.apply.call(console.log, console, newarr) : console.log.apply(console, newarr));
  }
};

// make it safe to use console.log always
(function(b){function c(){}for(var d="assert,count,debug,dir,dirxml,error,exception,group,groupCollapsed,groupEnd,info,log,timeStamp,profile,profileEnd,time,timeEnd,trace,warn".split(","),a;a=d.pop();){b[a]=b[a]||c}})((function(){try
{console.log();return window.console;}catch(err){return window.console={};}})());


// place any jQuery/helper plugins in here, instead of separate, slower script files.

(function($) {

    $.fn.extend({
                    filter_rows: function(role, value, condition){

                        var eval = function(x,y,o){

                            if (typeof(y) === 'Integer' ) var x = parseInt(x);

                            switch(o){
                                    case '%3C':
                                    case '<':
                                        return x < y;
                                        break;
                                    case '%3C%3D':
                                    case '<=':
                                        return x <= y;
                                        break;
                                    case '%3E':
                                    case '>':
                                        return x > y;
                                        break;
                                    case '%3E%3D':
                                    case '>=':
                                        return x >= y;
                                        break;
                                    case '=':
                                    case '%3D%3D':
                                    default:
                                        return x == y;
                                }
                        };

                        var collection = [];

                        this.find('td[role="'+role+'"]').each(function(){
                            if (eval($(this).html(), value, condition))
                                collection.push($(this).parents('tr')[0]);
                        });

                        return $(collection);

                    }

    });

})(jQuery);