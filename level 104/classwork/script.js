// ----------------------------
// STRING METHODS
// ----------------------------

// split()
// გამყოფს სტრინგს პატარა სტრინგებად და აბრუნებს მას როგორც მასივს
let str = "I love JS";
let arr = str.split(" "); // ["I", "love", "JS"]

// join()
// აერთიანებს მასივის ელემენტებს სტრინგად, გამოიყენება დელიმიტერთან ერთად
let joined = arr.join("-"); // "I-love-JS"

// ----------------------------
// ARRAY METHODS
// ----------------------------

// concat()
// აერთიანებს ორ ან მეტ მასივს ახალ მასივში
let arr1 = [1,2];
let arr2 = [3,4];
let combined = arr1.concat(arr2); // [1,2,3,4]

// push()
// დაამატებს ელემენტს მასივის ბოლოს
arr1.push(5); // arr1 = [1,2,5]

// pop()
// წაშლის ბოლო ელემენტს მასივიდან და დააბრუნებს მას
let last = arr1.pop(); // last = 5, arr1 = [1,2]

// shift()
// წაშლის პირველ ელემენტს მასივიდან და დააბრუნებს მას
let first = arr1.shift(); // first = 1, arr1 = [2]

// unshift()
// დაამატებს ელემენტ(ებ)ს მასივის დასაწყისში
arr1.unshift(0); // arr1 = [0,2]

// slice()
// აბრუნებს ახალი მასივის ნაწილს, არ ცვლის ორიგინალს
let sliced = arr2.slice(1,3); // [4] (note: slice(start, end) – end არ შედის)

// splice()
// ცვლის მასივს: წაშლა, დამატება ან ორივე ერთად
let arr3 = [1,2,3,4];
arr3.splice(1,2, "a","b"); 
// 1 = start index, 2 = number of elements to remove, "a","b" = elements to add
// arr3 = [1,"a","b",4]

// flat()
// ბრტყელი მასივის შექმნა, თუ მასივში აქვს nested arrays
let nested = [1,[2,3],[4,[5]]];
let flat1 = nested.flat(); // [1,2,3,4,[5]]
let flat2 = nested.flat(2); // [1,2,3,4,5]

// ----------------------------
// ARRAY PROPERTY
// ----------------------------

// length
// მასივის ან სტრინგის ზომა (ელემენტების რაოდენობა)
let arr4 = [1,2,3];
console.log(arr4.length); // 3
console.log(str.length);  // 9 ("I love JS")
