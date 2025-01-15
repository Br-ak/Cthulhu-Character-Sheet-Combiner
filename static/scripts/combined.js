fetch("/static/data.json")
.then(function(response){
    return response.json();
})
.then(function(dataset){
    console.log(dataset);
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for (const key in dataset){
        data = dataset[key];
        out += `
            <tr>
                <td>${data.Investigators_Name}</td>
                <td>${data.CurrentSanity}</td>
                <td>${data.CurrentHP}</td>
                <td>${data.MOV}</td>
                <td>${data.DEX}</td>
                <td>${data.STR}</td>
                <td>${data.CON}</td>
                <td>${data.POW}</td>
                <td>${data.INT}</td>
                <td>${data.SIZ}</td>
                <td>${data.APP}</td>
                <td>${data.EDU}</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;
});