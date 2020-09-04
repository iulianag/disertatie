var xhttp = new XMLHttpRequest();


function sendDelete(event, url){
    event.preventDefault();
	xhttp.open("DELETE", url, true);
	xhttp.send(null);
    location.reload();
}


function sendPostForm(event, formId, url){
    event.preventDefault();
    var formData = new FormData( document.getElementById(formId) );
    xhttp.open("POST", url, true);
	xhttp.send(formData);
    location.reload();
}
