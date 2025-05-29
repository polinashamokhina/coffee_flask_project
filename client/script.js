// fetch('http://127.0.0.1:5000/api/farms', {
//   method: 'POST',
//   body: JSON.stringify({
//     name: "ABU",
//     location: "Panama" ,
//     description: "Small farm with only brigth and floral coffee profiles"
//   }),
//   headers: {
//     'Content-type': 'application/json; charset=UTF-8'
//   }
// })
//   .then(response => response.json())
//   .then(data => console.log(data));
const allCards = document.querySelector(".allCards");

window.onload = function(){
  fetch('http://127.0.0.1:5000/api/farms')
  .then(response => response.json())
  .then(data => {
    
    data.forEach(farms => {
      const div_name = document.createElement("div");
      const div_location = document.createElement("div");
      const div_description = document.createElement("div");
      const image = document.createElement("img");
      const div_card = document.createElement("div");
      
      div_name.innerText = farms.name;
      div_location.innerText = farms.location;
      div_description.innerText = farms.description;
      image.src = farms.image;

      
      div_name.classList.add("card-farm");
      div_location.classList.add("card-country");
      div_description.classList.add("card-description");
      image.classList.add("img");
      div_card.classList.add("card");

      div_card.appendChild(image);
      div_card.appendChild(div_name);
      div_card.appendChild(div_location);
      div_card.appendChild(div_description);
      

      allCards.appendChild(div_card);
      
                 });
  })
}
