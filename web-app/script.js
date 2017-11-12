var i=0;
var num_stud=8;
var newdiv;
var divIdName;

$("#card").flip({
  trigger: 'manual'
});

$('.fab').on('click', function() {

$("#card").flip(true);


});

$('.cancel').on('click', function() {

$("#card").flip(false);


});

$('.save').on('click', function() {
newdiv = document.createElement('div');
            divIdName = '50'+i;
            newdiv.setAttribute('id',divIdName);
            newdiv.innerHTML ='<div id="box'+i+'">document.getElementById("c-number");</div>';
            document.body.appendChild(newdiv);



});

