$(document).ready(function() {
    var current = location.pathname;
    //console.log(current);

    $('nav a').each(function() {
        var $this = $(this); 

        //console.log($this.attr('href'));

        if ($this.attr('href') === current) {

            //console.log("got current")
            $this.addClass('active item');
        }
    });
})
