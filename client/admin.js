const addFarmButton = document.querySelector("#addFarmBtn");
const addCoffeeButton = document.querySelector("#addCoffeeBtn");

const farmName = document.querySelector("#farmNameId");
const farmLocation = document.querySelector("#farmLocationId");
const farmDescription = document.querySelector("#farmDescriptionId");
const farmImage = document.querySelector("#farmImageId");

const coffeeFarmId = document.querySelector("#coffeeFarmId");
const coffeeVariety = document.querySelector("#coffeeVarietyId");
const coffeeProcess = document.querySelector("#coffeeProcessId");
const coffeeDescriptors = document.querySelector("#coffeeDescriptorsId");
const coffeeImage = document.querySelector("#coffeeImageId");

const farmList = document.querySelector("#farmList"); 
const coffeeList = document.querySelector("#coffeeList");// object and not an array

const farmTable = document.querySelector("#farmTable");

function build_farms_table(farms){
    console.log(farms);
    for (const farm of farms){

        let row = document.createElement("tr");

        let nameData = document.createElement("td");
        let inputName = document.createElement("input");
        inputName.value = farm.name;
        nameData.appendChild(inputName);
        row.appendChild(nameData);
        farmTable.appendChild(row);

        let locationData = document.createElement("td");
        let inputLocation = document.createElement("input");
        inputLocation.value = farm.location;
        locationData.appendChild(inputLocation);
        row.appendChild(locationData);
        farmTable.appendChild(row);

        let descriptionData = document.createElement("td");
        let inputDescription = document.createElement("input");
        inputDescription.value = farm.description;
        descriptionData.appendChild(inputDescription);
        row.appendChild(descriptionData);
        farmTable.appendChild(row);

        let imageData = document.createElement("td");
        let inputImage = document.createElement("input");
        inputImage.value = farm.image;
        imageData.appendChild(inputImage);
        row.appendChild(imageData);
        farmTable.appendChild(row);

        const deleteButton = document.createElement("button");
        deleteButton.innerText = "Delete";
        deleteButton.addEventListener("click", () => {
            fetch('http://127.0.0.1:5000/api/farms/' + farm.id, {
                method: "DELETE",
                headers: {
                    "Content-type": "application/json; charset=UTF-8"
                }
                })
                .then(response => response.json())
                .then(data => console.log(data)); 
            });
        
        const updateButton = document.createElement("button");
        updateButton.innerText = "Update Data";
        updateButton.addEventListener("click", () => {
            fetch('http://127.0.0.1:5000/api/farms/' + farm.id, {
                method: "PUT",
                body: JSON.stringify({
                    name: inputName.value ,
                    location: inputLocation.value ,
                    description: inputDescription.value , 
                    image: inputImage.value
                }),
                headers: {
                    "Content-type": "application/json; charset=UTF-8"
                }
                })
                .then(response => response.json())
                .then(data => console.log(data)); 
            });
        
        let actionData = document.createElement("td");
        actionData.appendChild(deleteButton);
        actionData.appendChild(updateButton);
        row.appendChild(actionData);
        farmTable.appendChild(row);
    
        // let newRow = farmTable.insertRow(-1);

        // let newNameCell = newRow.insertCell(0);
        // let newNameText = document.createTextNode(farm.name);
        // newNameCell.appendChild(newNameText);

        // let newLocationCell = newRow.insertCell(1);
        // let newLocationText = document.createTextNode(farm.location);
        // newLocationCell.appendChild(newLocationText);

        // let newDescriptionCell = newRow.insertCell(2);
        // let newDescriptionText = document.createTextNode(farm.description);
        // newDescriptionCell.appendChild(newDescriptionText);

        // let newImageCell = newRow.insertCell(3);
        // let newImageText = document.createTextNode(farm.image);
        // newImageCell.appendChild(newImageText);

        
        // let newActionCell = newRow.insertCell(4);
        // newActionCell.appendChild(deleteButton);
    }

}

window.onload = function (){

    fetch('http://127.0.0.1:5000/api/farms', {
        method: "GET",
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
        })
        .then(response => response.json())
        .then(data => build_farms_table(data)); 
}

addFarmButton.addEventListener("click", function(){

    fetch('http://127.0.0.1:5000/api/farms', {
        method: 'POST',
        body: JSON.stringify({
            name: farmName.value ,
            location: farmLocation.value ,
            description: farmDescription.value , 
            image: farmImage.value
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8'
        }
        })
        .then(response => response.json())
        .then(data => console.log(data)); // на стороне клиента хдес можем сжделать попап что тип добавилось в бд
            
})

addCoffeeButton.addEventListener("click", function(){

    fetch('http://127.0.0.1:5000/api/coffees', {
        method: 'POST',
        body: JSON.stringify({
            farm_id: coffeeFarmId.value ,
            variety: coffeeVariety.value ,
            process: coffeeProcess.value , 
            descriptors: coffeeDescriptors.value , 
            image: coffeeImage.value
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8'
        }
        })
        .then(response => response.json())
        .then(data => console.log(data));
            
})