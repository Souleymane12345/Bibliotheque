
update()
function update  () {
    

    var updateButtom = document.querySelectorAll("#editEmployeeModalId");
    for (i = 0; i < updateButtom.length; i++) {
        alert(updateButtom.length)
        updateButtom[i].addEventListener("click", function() {
            alert("okkk")
            var personne = document.querySelectorAll("#id")[i];
            console.log(personne)
            document.querySelectorAll("#idUpdate")[i]  = personne;
        });
    }
}