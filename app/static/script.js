function createDialDiv(content, cssClass) {
    let divElt = document.createElement("div");
    divElt.classList.add(cssClass);
    divElt.appendChild(document.createTextNode(content));
    let dialogSection = document.getElementById("dialog");
    dialogSection.appendChild(divElt);
}

var dialogForm = document.querySelector("form");
dialogForm.addEventListener("submit", e => {
    e.preventDefault();
    createDialDiv(dialogForm.elements.place.value, "user-dialog");
    let query = new FormData(dialogForm);
        
    fetch(`${window.origin}/query/`, {
        method: 'post',
        body: query,
        cache: "no-cache"
    })
    
    .then(function(response) {
        if (response.status !== 200){
            console.log(`A problem occured. Status code: ${response.status}`);
            return;
        }
        response.json().then(function(data) {
            console.log(data);
            createDialDiv(data.req, "grandpy-dialog")
        }); 
    })
    .catch(function(error) {
        console.log("Fetch error: " + error);
    });    
});