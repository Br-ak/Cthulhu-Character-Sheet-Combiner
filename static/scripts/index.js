function update_table(files){
    console.log(files);
    const fileList = document.getElementById("file_list");
    const title = document.getElementById("title");

    if (Object.keys(files).length > 0){
        fileList.hidden = false
        title.hidden = false
        for (const key in files){
            console.log(files[key]);
            const listItem = document.createElement("li"); // Create a new <li>
            listItem.textContent = files[key]; // Set its text content
            fileList.appendChild(listItem); // Append it to the <ol>
        }
    }
}