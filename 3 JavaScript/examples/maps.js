let mymap = L.map('mapid').setView([51.505, -0.09], 1);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: ''
}).addTo(mymap);

const url = 'https://jsonplaceholder.typicode.com/users';

axios.get(url)
  .then(function (response) {
    // iterate through the objects in the response
    for (let person of response.data){
        // create a marker for lat lon
        let marker = L.marker([person.address.geo.lat, person.address.geo.lng]).addTo(mymap);

        // create a popup for the marker that will show the user's name and address information
        marker.bindPopup(`<b>${person.name}</b><br><p>${person.address.street}</p><p>${person.address.suite}</p>
        <p>${person.address.city}</p><p>${person.address.zipcode}</p>`).openPopup();

        // create card for each person 

        let newCard = document.createElement('li');
        newCard.innerHTML = `
        <div class="card">
            <div class="card-body">
            <h5 class="card-title">${person.name}</h5>
            <li id="location">lat: ${person.address.geo.lat} long: ${person.address.geo.lng}</li>
            <li id="location"> ${person.address.city}</li>
            </div>
        </div> 
    `;
        document.querySelector('#cards').append(newCard);

    }    
  })
  .catch(function (error) {
    console.log(error);
  })