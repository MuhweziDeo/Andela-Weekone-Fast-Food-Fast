var modal = document.getElementById('add-modal');


var btn = document.getElementById("add-btn");


btn.onclick = function() {
    modal.style.display = "block";
}



window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}