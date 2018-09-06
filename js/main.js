var modal = document.getElementById('add-modal');
var updatemodal=document.getElementById('editmodal')


var btn = document.getElementById("add-btn");
var editbtn=document.getElementById('editmodal-btn')


// display modal
btn.onclick = function() {
    modal.style.display = "block";
};

editbtn.onclick=function(){
updatemodal.style.display='block';
}

// Close Modal
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

window.onclick = function(event) {
    if (event.target == updatemodal) {
        updatemodal.style.display = "none";
    }
}