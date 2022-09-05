
update()
function update  () {
    
    
    let updateButtom = document.querySelectorAll("#editEmployeeModalId");
    let id_visiteur = document.querySelectorAll("#id_visiteur");
            //let len = document.querySelector("#main-wrapper > div > div > div > div.container > div > table > tbody > tr:nth-child(1) > td.id").textContent;

    console.log(id_visiteur.length)
    for ( let i = 0; i < updateButtom.length; i++) {
        updateButtom[i].addEventListener("click", function() {
            //alert(i)
            let personne = document.querySelectorAll("#id_visiteur")[i].textContent;
            //let len = document.querySelector("#main-wrapper > div > div > div > div.container > div > table > tbody > tr:nth-child(1) > td.id").textContent;

            console.log(personne)
            document.querySelector("#idUpdate").innerHTML  = personne;
        });
    }
}


//document.querySelector("#main-wrapper > div > div > div > div.container > div > table > tbody > tr:nth-child(1) > ")

