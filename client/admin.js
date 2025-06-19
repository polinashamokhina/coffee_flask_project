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