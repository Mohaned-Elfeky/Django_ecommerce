
(function ($) {
    "use strict";

    
    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }
        
        $('.validate-form').submit()
        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    

})(jQuery);

$("#register_btn").click(function(){
    
    if($("#confirm_input").hasClass("hidden")){
        
        
        $("#form_type").attr("name","register_form")
        $("#register_btn").html("Sign in")
        $("#register_btn").css({"position":"relative","bottom":"120px"});
        $("#signin_btn").html("Register")
        $("#confirm_input").removeClass("hidden")
        $("#username_field").removeClass("hidden")
        
        
    }
    else{
        
        $("#form_type").attr("name","login_form")
        $("#register_btn").html("Create your Account")
        $("#signin_btn").html("login")
        $("#confirm_input").addClass("hidden")
        $("#username_field").addClass("hidden")
        
    }
})