
// close modal

closebtn2.onclick = function () {
    updatemodal.style.display = 'none';
}
closebtn.onclick = function () {
    modal.style.display = 'none';
}

function showmodal() {
    document.getElementById("editmodal").style.display = "block";
}
function closemodal() {
    document.getElementById("editmodal").style.display = "none";
}

function addfastfood() {
    document.getElementById("add-modal").style.display = "block";
}
function close_addmodal() {
    document.getElementById("add-modal").style.display = "none";
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