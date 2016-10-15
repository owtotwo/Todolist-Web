function Done(user, id) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "/"+ user+ "/do/" + id, false);
    xmlHttp.send();
    location.reload(true);
}

function Undo(user, id) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "/"+ user+ "/undo/" + id, false);
    xmlHttp.send();
    location.reload(true);
}