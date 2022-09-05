
search()
function search  () {
    
    
    let recherche =  document.getElementById("recherche");
    recherche.addEventListener("click", function() {
            let value = document.getElementById("value").value;
            console.log(value)
            let base_url = 
            "http://127.0.0.1:8080/bib/api-view/operation-search?search=";
            let api_url = base_url.concat(value)
            console.log(api_url)
            getapi(api_url);
     });

}

// api url

  
// Defining async function
async function getapi(url) {
    
    // Storing response
    const response = await fetch(url);
    
    // Storing data in form of JSON
    var data = await response.json();
    
    for (let i = 0; i < data.length; i++) {
        console.log(data[i].exRef)
      }
    show(data);
}
// Calling that async function


// Function to define innerHTML for HTML table
function show(data) {
    let tab = 
        `<thead>
            <tr>
                <th class="border-top-0">Id</th>
                <th class="border-top-0">Réferencee</th>
                <th class="border-top-0">Réf Livre</th>
                <th class="border-top-0">Réf Edition</th>
                <th class="border-top-0">Réf Visiteur</th>
                <th class="border-top-0">Operation</th>
                <th class="border-top-0">D debut</th>
                <th class="border-top-0">D fin</th>
                <th class="border-top-0">Statut</th>
            </tr>
        </thead>`;
    
    // Loop to access all rows 
    for (let i = 0; i < data.length; i++) {
        tab += `<tr> 
    <td>${data[i].id} </td>
    <td>${data[i].exRef}</td>
    <td>${data[i].exEc}</td> 
    <td>${data[i].exEd}</td>  
    <td>${data[i].exVi}</td>         
    <td>${data[i].exOp}</td> 
    <td>${data[i].exDb}</td>
    <td>${data[i].exDb}</td>  
    <td>${data[i].exSt}</td> 
</tr>`;
    }
    // Setting innerHTML as tab variable
    document.getElementById("filtre").innerHTML = tab;
}
