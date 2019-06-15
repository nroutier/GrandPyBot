// Script that generates the dialogs beetween the user and GandPy using Ajax
// let dialogForm = document.querySelector("form");
let dialogForm = document.getElementById("queryForm");
dialogForm.addEventListener("submit", e => {
    e.preventDefault();
    document.getElementById("progress").classList.remove("d-none");
    let divReq = document.createElement("div");
    divReq.classList.add("user-dialog");
    divReq.appendChild(document.createTextNode(dialogForm.elements.place.value));
    let dialogSection = document.getElementById("dialog");
    dialogSection.appendChild(divReq);
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
            let dialSection = document.getElementById("dialog");
            let addressText = data.address_dialog;
            let divAddress = document.createElement("div");
            divAddress.classList.add("grandpy-dialog");
            divAddress.appendChild(document.createTextNode(addressText + data.address));
            dialSection.appendChild(divAddress);
            if (data.coord !== "") {
                let divMap = document.createElement("div");
                divMap.classList.add("map");
                dialSection.appendChild(divMap);
                let map = new google.maps.Map(divMap, {
                    center: data.coord,
                    zoom: 15
                });
                let marker = new google.maps.Marker({
                    position: data.coord,
                    map: map
                });
                let aboutUrl = document.createElement("a");
                if (data.info_place_url == "") {
                    aboutUrl.textContent = "";
                } else {
                    aboutUrl.textContent = "[En savoir plus sur Wikipedia]";
                }
                aboutUrl.href = data.info_place_url;
                let aboutGpyText =  data.place_dialog;
                let aboutText = document.createTextNode(aboutGpyText + data.info_place + " ");
                let divAbout = document.createElement("div");
                divAbout.classList.add("grandpy-dialog");
                divAbout.appendChild(aboutText);
                divAbout.appendChild(aboutUrl);
                dialogSection.appendChild(divAbout);
            }
            document.getElementById("progress").classList.add("d-none");
            document.getElementById("queryForm").reset();
        }); 
    })
    .catch(function(error) {
        console.log("Fetch error: " + error);
    });
});