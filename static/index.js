function Done(user, id) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "/"+ user+ "/" + id, false);
    location.reload(true);
}

function Undo(user, id) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "/"+ user+ "/" + id, false);
    location.reload(true);
}