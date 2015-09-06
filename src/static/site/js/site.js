(function(){
  $(window).scroll(function () {
      var top = $(document).scrollTop();
      $('.corporate-jumbo').css({
        'background-position': '0px -'+(top/3).toFixed(2)+'px'
      });
      if(top > 50)
        $('.navbar').removeClass('navbar-transparent');
      else
        $('.navbar').addClass('navbar-transparent');
  }).trigger('scroll');
})();
$(document).ready(function() {
    $('#id_name').yourlabsAutocomplete({
        choiceSelector: '[data-value]',
        url: '/autocomplete/PersonAutocomplete/',
    }).input.bind('selectChoice', function(e, choice, autocomplete) {
        $.ajax({
            url : 'person/' + choice.html(),
            type : 'GET',
            data : {
            },
            success : function(data) {              
                $('#people-form').empty().append( data );
            },
            error : function(request, error)
            {
                $('#people-form').empty().append(JSON.stringify(request));
            }
        });
    });
    $("#button-id-set").click(function(e) { 
        $.ajax({
           type: "POST",
           url: "",
           data: $('.form-inline').serialize(),
           success: function(data)
           {
               alert(data); 
           }
         });
        return false; 
    });
});
