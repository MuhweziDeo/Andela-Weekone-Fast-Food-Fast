var modal = document.getElementById('add-modal');
var updatemodal = document.getElementById('editmodal')
var ordermodal=document.getElementById('order-modal')


var btn = document.getElementById("add-btn");
var orderbtn=document.getElementById('place-order')

var editbtn = document.getElementById('editmodal-btn')
var editbtn2 = document.getElementById('editmodal-btn2')
var editbtn3 = document.getElementById('editmodal-btn3')
var editbtn4 = document.getElementById('editmodal-btn4')
var editbtn5 = document.getElementById('editmodal-btn5')
var closebtn = document.getElementById('close')
var closebtn2 = document.getElementById('close2')


// display modal
orderbtn.onclick=function(){
    ordermodal.style.display="block";
}
btn.onclick = function () {
    modal.style.display = "block";

};

editbtn.onclick = function () {
    updatemodal.style.display = 'block';
}
editbtn2.onclick = function () {
    updatemodal.style.display = 'block';
}
editbtn3.onclick = function () {
    updatemodal.style.display = 'block';
}
editbtn4.onclick = function () {
    updatemodal.style.display = 'block';
}
editbtn5.onclick = function () {
    updatemodal.style.display = 'block';
}

// close modal

closebtn2.onclick = function () {
    updatemodal.style.display = 'none';
}
closebtn.onclick = function () {
    modal.style.display = 'none';
}

function displaymenu() {
    document.getElementById("menu-modal").style.display = "block";
}

function closemenu() {
    document.getElementById("menu-modal").style.display = "none";
}
function cancelorder() {
    document.getElementById("order-modal").style.display = "none";
}