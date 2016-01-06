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
$(document).ready(function () {
  $('.accordion-tabs').each(function(index) {
    $(this).children('li').first().children('a').addClass('is-active').next().addClass('is-open').show();
  });
  $('.accordion-tabs').on('click', 'li > a.tab-link', function(event) {
    if (!$(this).hasClass('is-active')) {
      event.preventDefault();
      var accordionTabs = $(this).closest('.accordion-tabs');
      accordionTabs.find('.is-open').removeClass('is-open').hide();

      $(this).next().toggleClass('is-open').toggle();
      accordionTabs.find('.is-active').removeClass('is-active');
      $(this).addClass('is-active');
    } else {
      event.preventDefault();
    }
  });
});
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
            error : function(request, error) {
                $('#people-form').empty().append(JSON.stringify(request));
            }
        });
    });
    $("#button-id-set").click(function(e) { 
        $.ajax({
           type: "POST",
           url: "",
           data: $('.form-inline').serialize(),
           success: function(data) {
               notif({
                   msg: "<b>Ok!:</b> Party data has been set.",
                   type: "success"
               });
           },
           error : function(request, error) {
               notif({
                   msg: "<b>Opps!</b> contact Mike for help :/" + error,
                   type: "error"
               });
           }
        });
        return false; 
    });
    $("#button-id-set-song").click(function(e) { 
        // default is "slug=", we want at least 2 chars for a song
        if ($("#id_slug").serialize() > 7) {
            $("#button-id-set").click()
        } else {
          $.ajax({
            type: "POST",
            url: "song/",
            data: $("#id_slug").serialize(),
            success: function(data) {
                notif({
                    msg: "<b>Thanks!:</b> Feel free to recommend more songs.",
                    type: "success"
                }),
                $("#id_slug").val("")
            },
            error : function(request, error) {
                notif({
                    msg: "<b>Opps!</b> contact Mike for help :/" + error,
                    type: "error"
                });
            }
          });
        }
        return false; 
    });
});
