function clearTableBody(tableBody) {
   while (tableBody.firstChild) {
    tableBody.removeChild(tableBody.firstChild);
   }
}
const renderTable=(data)=>{
    const tableBody = document.getElementById("service-tb");
    clearTableBody(tableBody);
    const createRow =(params)=> {
        const row = document.createElement("tr");
        const cellPrice = document.createElement('td');
        const cellName = document.createElement('td');
        cellPrice.textContent = params.price;
        cellName.textContent = params.name;
        row.appendChild(cellName);
        row.appendChild(cellPrice);
        return row;
    }

    data.forEach((item)=>{
        const row = createRow(item);
        tableBody.appendChild(row);
    })

}

const fetchData=()=>{
    fetch('/api/services')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            renderTable(data.items);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

if (window.location.pathname === '/service') {
    window.onload = fetchData;
}