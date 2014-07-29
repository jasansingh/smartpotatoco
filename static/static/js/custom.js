/**
 * Created by jasan_s on 7/27/2014.
 */

$(document).ready(function(){
    $('.upload-image').click(function(){
         $('.image-uploading').hide();
         $('.image-uploaded').toggleClass('hidden');

    });

});

var hacky = function(){
$("#temp1").hide();
    $("#temp2").show();
    $("#temp3").hide();
    $("#temp4").hide();
};

var hacky2 = function(){
$("#temp1").hide();
$("#temp2").hide();
$("#temp3").show();
$("#temp4").hide();
};

var hacky3 = function(){
$("#temp1").hide();
$("#temp2").hide();
$("#temp3").hide();
$("#temp4").show();
};
$(document).ready(function(){
    $('#first-addon').click(function(){
        console.log()
         $('#DIV-111').css("display","none");
         $('#DIV_112').show();




    });

});


