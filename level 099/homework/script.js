/*
  JS სკოუპები

  სკოუპი = სივრცე სადაც ცვლადი ჩანს

  1) Global – ფუნქციის გარეთ
  2) Function – var ფუნქციის შიგნით
  3) Block – let/const ბლოკში
  4) Module – ES module-სcope

  Hoisting: var/ფუნქცია იწევა ზედა ხაზზე; let/const – TDZ (ReferenceError).

  function test(){
    var a=1;
    if(true){ var b=2; let c=3; }
    console.log(a); // 1
    console.log(b); // 2
    // console.log(c); // Error
  }

  Lexical scope: შიდა ფუნქცია ხედავს გარე ცვლადებს.

  Closure: ფუნქცია ინახავს გარე ცვლადს.
  function counter(){ let x=0; return ()=>++x; }

  Shadowing: შიდა ცვლადი ფარავს გარეას.
*/







/*
  გლობალური სკოუპის მაგალითი:
*/

// გლობალური ცვლადი
let name = "Luka";

function sayName(){
  // აქ შეგვიძლია name-ის გამოყენება, რადგან ის გლობალურ სკოუპშია
  // და გლობალური ცვლადები ხილულია ყველა ფუნქციიდან
  console.log("hello " + name);
}

sayName(); // "hello Luka"






/*
  გლობალური vs ლოკალური სკოუპი:
*/

// გლობალური ცვლადი
let name = "Luka";

function sayName(){
  // გლობალურ ცვლადზე წვდომა შესაძლებელია აქაც
  console.log("გამარჯობა, " + name);

  // ლოკალური ცვლადი ფუნქციის შიგნით
  let message = "ეს არის ლოკალური მესიჯი";
  console.log(message); // მუშაობს აქ
}

sayName();

// console.log(message);
// ↑ ReferenceError: message is not defined
// რადგან message არის ლოკალური და ფუნქციის გარეთ მისი გამოყენება შეუძლებელია











/*
  ლექსიკური სკოუპის მაგალითი:
*/

function outer(){
  let outerVar = "გარე ფუნქციის ცვლადი";

  function inner(){
    // შიდა ფუნქციას შეუძლია outerVar-ის გამოყენება,
    // რადგან JS იყენებს ლექსიკურ სკოუპს:
    // შიდა ფუნქცია ხედავს იმ ცვლადებს, რომლებიც
    // მის გარე ფუნქციაშია დეკლარირებული.
    console.log(outerVar);
  }

  inner();
}

outer();