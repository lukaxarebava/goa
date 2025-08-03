const form = document.getElementById("myForm");
const resultDiv = document.getElementById("result");

const monthNames = [
  "იანვარი", "თებერვალი", "მარტი", "აპრილი", "მაისი", "ივნისი",
  "ივლისი", "აგვისტო", "სექტემბერი", "ოქტომბერი", "ნოემბერი", "დეკემბერი"
];

form.addEventListener("submit", function(event) {
  event.preventDefault();

  const name = form.elements["name"].value;
  const surname = form.elements["surname"].value;
  const date = new Date(form.elements["date"].value);

  const day = date.getDate();           
  const monthIndex = date.getMonth();    
  const year = date.getFullYear();     

  const monthName = monthNames[monthIndex];

  resultDiv.innerHTML = `${name} ${surname} - დაბადების თარიღი: ${day} ${monthName} ${year}`;
});
