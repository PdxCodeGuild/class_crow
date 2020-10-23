// pk.eyJ1IjoianBjaGF0byIsImEiOiJja2dpc3ZzZWYwZmRiMnFudXNhN2VpYXc1In0.68JEoiAvQJVRVFqnpEUyaA
console.log('hi')
var mymap = L.map('mapid').setView([51.505, -0.09], 13);
console.log(mymap)
console.log('we are here')

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 1,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoianBjaGF0byIsImEiOiJja2dpc3ZzZWYwZmRiMnFudXNhN2VpYXc1In0.68JEoiAvQJVRVFqnpEUyaA'
}).addTo(mymap);

// var marker = L.marker([51.5, -0.09]).addTo(mymap);
// L.marker([51.5, -0.09]).addTo(mymap).bindPopup('hi').openPopup()
let anchor = document.getElementById('content')
axios.get('https://jsonplaceholder.typicode.com/users')
    .then((response) => {
        // console.log(response.data[0].name)
        // console.log((response.data[0].address.geo))
        let users = response.data
        let header = document.createElement('header')
        let headerText = document.createTextNode('Names and Numbers')
        header.appendChild(headerText)
        anchor.append(header)
        
        console.log(users)
        users.forEach(element => {
            let br = document.createElement("br");
            lat = element.address.geo.lat
            lng = element.address.geo.lng
            // console.log(lat, lng)
            // console.log(element.name)
            // L.marker([lat, lng]).addTo(mymap);
            L.marker([lat, lng]).addTo(mymap).bindPopup('name: ' + element.name + '<br>' + 'city: ' + element.address.city).openPopup();
            let newContent = document.createTextNode(element.name + ', phone: ' + element.phone + ', email: ' + element.email)
            anchor.appendChild(newContent)
            anchor.appendChild(br)
            // console.log(element.address.geo)
            
        });
    });




