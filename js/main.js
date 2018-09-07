var modal = document.getElementById('add-modal');
var updatemodal=document.getElementById('editmodal')


var btn = document.getElementById("add-btn");
var editbtn=document.getElementById('editmodal-btn')
var closebtn=document.getElementById('close')


// display modal
btn.onclick = function() {
    modal.style.display = "block";
};
// close modal
closebtn.onclick= function(){
    updatemodal.style.display='none';
}
closebtn.onclick= function(){
    modal.style.display='none';
}

editbtn.onclick=function(){
updatemodal.style.display='block';
}

// Close Modal


window.onclick = function(event) {
    if (event.target == updatemodal) {
        updatemodal.style.display = "none";
    }
}