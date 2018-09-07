var modal = document.getElementById('add-modal');
var updatemodal=document.getElementById('editmodal')


var btn = document.getElementById("add-btn");
var editbtn=document.getElementById('editmodal-btn')
var closebtn=document.getElementById('close')
var closebtn2=document.getElementById('close2')

// display modal
btn.onclick = function() {
    modal.style.display = "block";

};
editbtn.onclick=function(){
    updatemodal.style.display='block';
    }
    
// close modal
closebtn2.onclick= function(){
    updatemodal.style.display='none';
}
closebtn.onclick= function(){
    modal.style.display='none';
}


// Close Modal
window.onclick = function(event) {
    if (event.target == updatemodal) {
        updatemodal.style.display = "none";
    }
}