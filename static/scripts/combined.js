fetch("/static/data.json")
.then(function(response){
    return response.json();
})
.then(function(dataset){
    console.log(dataset);
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for (const key in dataset){
        const data = dataset[key];
        
        out += `
            <tr>
                <td>${data.Investigators_Name}</td>
                <td>${data.CurrentSanity}</td>
                <td>${data.CurrentHP}</td>
                <td>${data.MOV}</td>
                <td class="tooltip-cell" data-tooltip="${data.DEX} / ${Math.floor(data.DEX / 2)} / ${Math.floor(data.DEX / 5)}">${data.DEX}</td>
                <td class="tooltip-cell" data-tooltip="${data.STR} / ${Math.floor(data.STR / 2)} / ${Math.floor(data.STR / 5)}">${data.STR}</td>
                <td class="tooltip-cell" data-tooltip="${data.CON} / ${Math.floor(data.CON / 2)} / ${Math.floor(data.CON / 5)}">${data.CON}</td>
                <td class="tooltip-cell" data-tooltip="${data.POW} / ${Math.floor(data.POW / 2)} / ${Math.floor(data.POW / 5)}">${data.POW}</td>
                <td class="tooltip-cell" data-tooltip="${data.INT} / ${Math.floor(data.INT / 2)} / ${Math.floor(data.INT / 5)}">${data.INT}</td>
                <td class="tooltip-cell" data-tooltip="${data.SIZ} / ${Math.floor(data.SIZ / 2)} / ${Math.floor(data.SIZ / 5)}">${data.SIZ}</td>
                <td class="tooltip-cell" data-tooltip="${data.APP} / ${Math.floor(data.APP / 2)} / ${Math.floor(data.APP / 5)}">${data.APP}</td>
                <td class="tooltip-cell" data-tooltip="${data.EDU} / ${Math.floor(data.EDU / 2)} / ${Math.floor(data.EDU / 5)}">${data.EDU}</td>
            </tr>
        `;
    }

    placeholder.innerHTML = out;

    // Adding event listeners to show the tooltip
    document.querySelectorAll('.tooltip-cell').forEach(cell => {
        const tooltip = document.createElement('div');
        tooltip.className = 'char_tooltip';
        document.body.appendChild(tooltip);

        cell.addEventListener('mouseover', function(e) {
            const text = e.target.getAttribute('data-tooltip');
            tooltip.innerHTML = text; // Set the tooltip text
            tooltip.style.left = `${e.pageX + 10}px`; // Position the tooltip next to the mouse
            tooltip.style.top = `${e.pageY + 10}px`;
            tooltip.style.display = 'block'; // Make it visible
        });

        cell.addEventListener('mouseout', function() {
            tooltip.style.display = 'none'; // Hide the tooltip when mouse leaves
        });
    });
});

// // Tooltip JavaScript
// const tooltip = document.getElementById('tooltip');

// document.addEventListener('mousemove', (e) => {
//   const tooltipText = e.target.getAttribute('data-tooltip');
//   if (tooltipText) {
//     tooltip.style.display = 'block';
//     tooltip.innerHTML = `
//       <div class="tooltip-title">Tooltip Title</div>
//       <table class="tooltip-table">
//         <tr>
//           <th>Attribute</th>
//           <th>Value</th>
//         </tr>
//         <tr>
//           <td>Example Data 1</td>
//           <td>100</td>
//         </tr>
//         <tr>
//           <td>Example Data 2</td>
//           <td>200</td>
//         </tr>
//       </table>
//     `;
//     tooltip.style.left = `${e.pageX + 10}px`;
//     tooltip.style.top = `${e.pageY + 10}px`;
//   } else {
//     tooltip.style.display = 'none';
//   }
// });

