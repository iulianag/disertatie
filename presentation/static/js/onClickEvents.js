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



function sendPut(event, url, input1, input2){
    event.preventDefault();
    var inputVal1 = document.getElementById(input1).value;
    var inputVal2 = document.getElementById(input2).value;
    var param1 = (input1.split("-"))[0]
    var param2 = (input2.split("-"))[0]
    var formData = new FormData();
    formData.append(param1, inputVal1);
    formData.append(param2, inputVal2);
    xhttp.open("PUT", url, true);
	xhttp.send(formData);
    location.reload();
}


function sendPutForm(event, formId, url){
    event.preventDefault();
    var formData = new FormData( document.getElementById(formId) );
    xhttp.open("PUT", url, true);
	xhttp.send(formData);
    location.reload();
}