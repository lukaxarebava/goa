const puppies = [
  { id: 1, name: "Golden Retriever", image: "https://i.shgcdn.com/148dc4ae-078b-4962-a7ba-70b75be8df4e/-/format/auto/-/preview/3000x3000/-/quality/lighter/", details: "Friendly, intelligent, and devoted." },
  { id: 2, name: "Labrador", image: "https://www.chovatelahospodar.sk/upload/user/743/2019/09/labradorsky-retriever_1567367415.jpg", details: "Gentle, loving, and outgoing." },
  { id: 3, name: "German Shepherd", image: "https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg", details: "Confident, courageous, and smart." },
  { id: 4, name: "Bulldog", image: "https://cdn.britannica.com/78/232778-050-D3701AB1/English-bulldog-dog.jpg", details: "Docile, willful, and friendly." },
  { id: 5, name: "Poodle", image: "https://thehappypuppysite.com/wp-content/uploads/2017/12/poodle4.jpg", details: "Active, alert, and intelligent." },
  { id: 6, name: "Beagle", image: "https://keyassets.timeincuk.net/inspirewp/live/wp-content/uploads/sites/14/2024/01/E4EYEE.jpg", details: "Even-tempered, intelligent, and determined." }
];

const urlParams = new URLSearchParams(window.location.search);
const id = parseInt(urlParams.get("id"));
const puppy = puppies.find(p => p.id === id);

const container = document.getElementById("detailsContainer");

if(puppy) {
  container.innerHTML = `
    <h2>${puppy.name}</h2>
    <img src="${puppy.image}" alt="${puppy.name}" style="width:300px;height:200px;object-fit:cover;">
    <p>${puppy.details}</p>
    <a href="index.html">Back to shop</a>
  `;
} else {
  container.innerHTML = "<p>Puppy not found</p>";
}
