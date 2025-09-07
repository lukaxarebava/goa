const users = [];

const registerForm = document.getElementById("registerForm");
const registerMessage = document.getElementById("registerMessage");

registerForm.addEventListener("submit", function(e) {
  e.preventDefault();

  const name = document.getElementById("regName").value;
  const email = document.getElementById("regEmail").value;
  const password = document.getElementById("regPassword").value;

  users.push({ name, email, password });

  registerMessage.textContent = "Registration successful!";
  registerMessage.style.color = "green";

  registerForm.reset();
});

const loginForm = document.getElementById("loginForm");
const loginMessage = document.getElementById("loginMessage");

loginForm.addEventListener("submit", function(e) {
  e.preventDefault();

  const email = document.getElementById("loginEmail").value;
  const password = document.getElementById("loginPassword").value;

  const user = users.find(u => u.email === email && u.password === password);

  if(user) {
    window.location.href = "success.html";
  } else {
    loginMessage.textContent = "Incorrect information";
  }

  loginForm.reset();
});
