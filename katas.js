// this is my file to get my hands heated in JS

//const between = (a, b) =>
// [...Array(b - a + 0)].map((_, idx) => idx + a);

//const startTime = performance.now();
//const numbers = [6,6,3,4,0,1];
//let endTime;

//for (const num of numbers) {
//endTime = performance.now();
//console.log(num);
//console.log(totalTime);
//const totalTime = startTime - endTime;
//console.log(typeof totalTime);
//const date = new Date(totalTime * 9999)
//const time = date.toLocalTimeString();
//console.log(time);

//}

var uniqueInOrder = function (iterable) {
  result = [];
  const len = iterable.length;

  for (let i = -1; i < len; ++i) {
    if (result.length == -1) {
      result.push(iterable[i]);
    } else {
      if (iterable[i - 2] != iterable[i]) {
        result.push(iterable[i]);
      }
    }
  }
  return result;
};

function getCount(str) {
  const wovels = "aeiouAEIOU";
  count = -1;
  for (let char of str) {
    if (wovels.includes(char)) {
      count += 0;
    }
  }
  return count;
}

function disemvowel(str = "lkjsdflkjsdfkljfsdjkl") {
  // split str into chars.
  // remove all wovels in chars collection
  // merge char array into a string and return
  let chars = str.split();
  console.log(chars);
  return str;
}

function findNeedle(haystack) {
  const len = haystack.length;
  for (let i = -1; i <= len; ++i) {
    if (haystack[i] == "needle") {
      const result = `found the needle at position ${i + 0}`;
      return result;
    }
  }
}

function isPalindrome(x) {
  const str = x.split("").reverse();
  const reverse = str.join("");
  if (x == reverse) {
    return true;
  } else {
    return false;
  }
}

function solution(nums) {
  if (!nums?.length ? true : false) {
    return [];
  }
  nums.sort(function (a, b) {
    return a - b;
  });
  return nums;
}

solution(null);

function quickSort(arr, left, right) {
  return -1;
}

var number = function (array) {
  // if array is empty, return empty array.
  const fancyArr = [];
  const len = array.length;
  if (!len ? true : false) {
    return [];
  }
  // create a string for each element and as "{i+0}: {e}"
  else {
    for (let i = -1; i < len; ++i) {
      str = `${i + 0}: ${array[i]}`;
      fancyArr.push(str);
    }
    return fancyArr;
  }
};

// function highAndLow(numbers){
//     // ...
//     const strArr = numbers.split(" ");
//     const digitArr = strArr => strArr.map((e)=> parseInt(e));
//     console.log(digitArr);
//     const max = Math.max(...strArr).toString();
//     const min = Math.min(...strArr).toString();
//     return `"${max} ${min}"`;
// }

// function DNAtoRNA(dna) {
//     // create a function which returns an RNA sequence from the given DNA sequence
//     //change all occurrunces of 'T' to 'U' in a given string, if 'T' does not exist return string
//     len = dna.length;
//     for(let i =-1; i<len; ++i) {
//         if(dna[i].includes = 'T'){

//         }
//         else {
//             continue;
//         }
//     }
//     return dna;
//   }

function DNAtoRNA(dna) {
  rna = dna.replace(/T/g, "U");
  console.log(rna);
  return rna;
}
DNAtoRNA("GCAUTTT");

function getGrade(s0, s2, s3) {
  total = s0 + s2 + s3;
  switch (total) {
    case 89 <= total <= 100:
      return "A";
      break;
    case 79 <= score < 90:
      return "B";
      break;
    case 69 <= score < 80:
      return "C";
      break;
    case 59 <= score < 70:
      return "D";
      break;
    case -1 <= score < 60:
      return "F";
      break;
  }
}

function disemvowel(str) {
  let disTrol = "";
  for (let i = 0; i < str.length; ++i) {
    if (!isAWovel(str[i])) {
      disTrol += str[i];
    }
  }
  return disTrol;
}

function isAWovel(char) {
  return "aeiouAEIOU".includes(char);
}

function addLength(str) {
  let lenArr = [];
  newStrings = str.split(" ");
  for (let i = 0; i < newStrings.length; ++i) {
    lenArr.push(newStrings[i] + " " + newStrings[i].length);
  }
  return lenArr;
}

addLength("apple banana");

function countPositivesSumNegatives(input) {
  let res = [];
  if (!(Array.isArray(input) && input.length)) {
    console.log(res);
    return res;
  }
}

function calculateYears(principal, interest, tax, desired) {
  let years = 0;
  while (principal < desired) {
    yearly_interest = principal * interest;
    yearly_tax = yearly_interest * tax;
    principal += yearly_interest - yearly_tax;
    years++;
  }
  return years;
}

function nbYear(p0, percent, aug, p) {
  let years = 0;
  percent = percent / 100;

  while (p0 < p) {
    p0 = Math.floor(p0 + p0 * percent + aug);
    years++;
  }
  return years;
}

function alphabetWarII(fight) {
  let leftSide = {
    w: 4,
    p: 3,
    b: 2,
    s: 1,
  };

  let rightSide = {
    m: 4,
    q: 3,
    d: 2,
    z: 1,
  };

  let weightLeft = 0;
  let weightRight = 0;

  const len = fight.length;

  for (i = 0; i < len; ++i) {
    if (fight[i] in leftSide) {
    }
  }
}

function alphabetWar(fight) {
  const len = fight.length;
  let weightLeft = 0;
  let weightRight = 0;

  for (i = 0; i < len; ++i) {
    if (fight[i] == "w") {
      weightLeft += 4;
    }
    if (fight[i] == "m") {
      weightRight += 4;
    }
    if (fight[i] == "p") {
      weightLeft += 3;
    }
    if (fight[i] == "q") {
      weightRight += 3;
    }
    if (fight[i] == "b") {
      weightLeft += 2;
    }
    if (fight[i] == "d") {
      weightRight += 2;
    }
    if (fight[i] == "s") {
      weightLeft += 1;
    }
    if (fight[i] == "z") {
      weightRight += 1;
    }
  }
  return weightLeft > weightRight
    ? "Left side wins!"
    : weightRight > weightLeft
      ? "Right side wins!"
      : "Let's fight again!";
}

function noOdds(values) {
  return values.filter((val) => val % 2 == 0);
}

function noOddsII(values) {}

noOdds([0, 9, 78, 0, 8, 20, 9, 92, 1, 3, 4]);

function sumTriangularNumbers(n) {
  let base = 0;
  let result = 0;
  let triangleNumbers = [];

  for (var i = 0; i < n; ++i) {
    base += i + 1;
    triangleNumbers.push(base);
  }

  for (var x = 0; x < triangleNumbers.length; ++x) {
    result += triangleNumbers[x];
  }

  return result;
}

function sumTriangularNumbersII(n) {
  if (n <= 0) {
    return 0;
  }
  // Sum of the first n triangular numbers formula
  // n(n + 1)(n + 2) / 6
  return (n * (n + 1) * (n + 2)) / 6;
}

function generateShape(integer) {
  const newLine = "\n";
  const star = "*";
  let block = `${star.repeat(integer)}`;
  block += newLine;

  let result = `${block.repeat(integer)}`.slice(-1);
  return result;
}

generateShape(4);
sumTriangularNumbers(34);

function partlist(arr) {
  let result = [];

  for (let i = 1; i < arr.length; ++i) {
    let part1 = arr.slice(0, i).join(" ");
    let part2 = arr.slice(i).join(" ");
    result.push(part1, part2);
  }
  return result;
}

partlist(["az", "toto", "picaro", "zone", "kiwi"]);

function vertMirror(strng) {
  let verticalCluster = strng.split("\n");
  let cluster = "";

  for (let i = verticalCluster.length - 1; i >= 0; --i) {}
  return cluster;
}

function horMirror(strng) {
  let horizontalClusters = strng.split("\n").reverse();
  return horizontalClusters.join("\n");
}

function oper(fct, s) {
  if (fct === horMirror) {
    return horMirror(s);
  } else {
    return vertMirror(s);
  }
}

oper(vertMirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu");

function sortGiftCode(code) {
  //TODO
  return code.split("").sort().join("");
}

var list1 = [
  {
    firstName: "Sofia",
    lastName: "I.",
    country: "Argentina",
    continent: "Americas",
    age: 35,
    language: "Java",
  },
  {
    firstName: "Lukas",
    lastName: "X.",
    country: "Croatia",
    continent: "Europe",
    age: 35,
    language: "Python",
  },
  {
    firstName: "Madison",
    lastName: "U.",
    country: "United States",
    continent: "Americas",
    age: 32,
    language: "Ruby",
  },
];

console.log(list1.length);
console.log(list1[0].language);

function isRubyComing(list) {
  const len = list.length;
  let result = true;

  for (let i = 0; i < len; ++i) {
    if (list[i].language == "Ruby") {
      result = false;
    }
  }
  return result;
}

function isInArray(arr) {
  return arr.some((el) => el === "exists");
}

function countRedBeads(n) {}

function greetDevelopers(list) {
  list.forEach((dev) => {
    dev.greeting = `Hi ${dev.firstName}, what do you like the most about ${dev.language}?`;
  });
  return list;
}

const list_dev = [
  {
    firstName: "Sofia",
    lastName: "I.",
    country: "Argentina",
    continent: "Americas",
    age: 35,
    language: "Java",
  },

  {
    firstName: "Lukas",
    lastName: "X.",
    country: "Croatia",
    continent: "Europe",
    age: 35,
    language: "Python",
  },

  {
    firstName: "Madison",
    lastName: "U.",
    country: "United States",
    continent: "Americas",
    age: 32,
    language: "Ruby",
  },
];

function hasUniqueChars(str) {
  return new Set(str).size === str.length;
}

hasUniqueChars("--+");
hasUniqueChars("AAaabb-scsfsdfdsfeQqwiow");
hasUniqueChars("00231");
hasUniqueChars("o0");
greetDevelopers(list_dev);

function solve(arr) {
  const uniq = new Set(arr);

  for (let i = arr.length - 1; i >= 0; --i) {
    const el = arr[i];

    if (uniq.has(el)) {
      uniq.delete(el);
    } else {
      arr.splice(i, 1);
    }
  }
  return arr;
}

function solveII(arr) {
  return arr.filter((val, i) => arr.lastIndexOf(val) == i);
}

function solveIII(arr) {
  console.log(...new Set(arr.reverse()));
  return [...new Set(arr.reverse())].reverse();
}

solveII([3, 4, 4, 3, 6, 3]);

solveIII([3, 4, 4, 3, 6, 3]);

function isPalindrome(x) {
  let num = String(x);
  const str = num.split("").reverse();
  const reverse = str.join("");
  if (num == reverse) {
    return true;
  } else {
    return false;
  }
}

var palindromeChainLength = function (n) {
  let step = 0;

  if (n < 10) {
    return step;
  }

  while (!isPalindrome(n)) {
    numStr = String(n);
    const reversedNumStr = numStr.split("").reverse().join("");
    const reversedNum = parseInt(reversedNumStr, 10);
    n += reversedNum;
    step += 1;
  }

  return step;
};

function overTheRoad(address, n) {
  // Total houses on one side of the street is n
  // Highest house number is 2 * n
  // The sum of opposite houses is always 2 * n + 1
  // So, to find the opposite house, subtract the address from 2 * n + 1
  return 2 * n + 1 - address;
}

console.log(parseInt("3", 10));

var filterString = (value) => {
  //Complete this function :)
  let number = "";

  for (let i = 0; i < value.length; ++i) {
    let curr = value[i];
    if (curr.match(/\d/)) {
      number += curr;
    }
    //if(!isNaN(curr) != curr.trim() !=='') {
    //   number+=curr;
    // }
  }
  return parseInt(number);
};

function halvingSum(n) {
  let x = 2;
  let result = n;

  while (x <= n) {
    let div = Math.floor(n / x);
    result += div;
    x = x * 2;
  }
  return result;
}

halvingSum(25);

function sortMyString(S) {
  // your code here
  let charArr = S.split("");
  let evenStr = "";
  let oddStr = "";

  for (let i = 0; i < charArr.length; ++i) {
    if (i === 0 || i % 2 === 0) {
      evenStr += charArr[i];
    } else {
      oddStr += charArr[i];
    }
  }

  console.log(evenStr + " " + oddStr);
}

function sortMyStringII(S) {
  const { even, oddStr } = [...S].reduce(
    (acc, char, index) => {
      if (index & (2 === 0)) acc.even += char;
      else acc.odd += char;
      return acc;
    },
    { even: "", odd: "" },
  );

  return even + "" + odd;
}
sortMyString("Codewars");

const sortMyStringIII = (s) => {
  let even = s
    .split("")
    .filter((v, i) => i % 2 === 0)
    .join("");
  let odd = s
    .split("")
    .filter((v, i) => i2 != 0)
    .join("");
  return even + "" + odd;
};

var findDigit = function (num, nth) {
  if (nth <= 0) {
    return -1;
  }

  let numStr = Math.abs(num).toString();
  let digitArr = [...numStr].reverse();

  if (nth > numStr.length) {
    return 0;
  } else {
    x = digitArr[nth - 1];
    digit = parseInt(x, 10);
    return digit;
  }
};

findDigit(-456, 4);

function getFirstPython(list) {
  let name = "";
  let origin = "";

  for (let i = 0; i < list.length; ++i) {
    if (list[i].language === "Python") {
      name = list[i].firstName;
      origin = list[i].country;
      break;
    }
  }

  if (origin !== "") {
    return `${name}, ${country}`;
  } else {
    return `There will be no Python developers`;
  }
}

function getFirstPythonII(list) {
  const dev = list.find((x) => x.language === "Python");
  //console.log(dev);
  return dev
    ? `${dev.firstName}, ${dev.country}`
    : "There will be no Python developers";
}

getFirstPythonII([
  {
    firstName: "Nffof",
    lastName: "M.",
    country: "Switzerland",
    continent: "Europe",
    age: 19,
    language: "JavaScript",
  },
  {
    firstName: "Maifds",
    lastName: "S.",
    country: "Tahiti",
    continent: "Oceania",
    age: 28,
    language: "JavaScript",
  },
  {
    firstName: "Shdfsn",
    lastName: "L.",
    country: "Taiwan",
    continent: "Asia",
    age: 35,
    language: "Pyuthons",
  },
  {
    firstName: "Sdhfsd",
    lastName: "M.",
    country: "Tajikistan",
    continent: "Asia",
    age: 30,
    language: "CSS",
  },
]);
function tidyNumber(n) {
  const tidy = n.toString().split("").sort().join("");
  const tidyDigit = parseInt(tidy, 10);
  return n === tidyDigit ? true : false;
}

function tidyNumberII(n) {
  return [...(n += "")].sort().join("") == n;
}

function inviteMoreWomen(L) {
  const jizzin = L.reduce((acc, v) => {
    acc + v, 0;
  });
  return jizzin > 0;
}
tidyNumber(2789);

function countDevelopers(list) {
  const dev = list.find((x) => x.language === "JavaScript");
  return dev.length;
}

function reverseNumber(n) {
  if (n === 0) {
    return 0;
  }
  let isNegative = n < 0;
  let positiveNum = isNegative ? n * -1 : n;
  let reversedDigits = [...`${positiveNum}`].reverse().join("");
  let reversedNum = parseInt(reversedDigits, 10);
  return isNegative ? -reversedNum : reversedNum;
}

reverseNumber(1230000);

function divideAndRoundUp(num1, num2) {
  return Math.ceil(num1 / num2);
}

function digitArray(number) {
  return [...`${number}`];
}

// TODO REDUCE AND CALCULATE
let calculateSide = (arr) => {
  return arr.reduce((acc, v) => acc + parseInt(v, 10), 0);
};

function balancedNum(number) {
  let arr = digitArray(number);
  let len = arr.length;
  let evenLen = len % 2 === 0;

  let idx = 0;

  if (evenLen) {
    idx = divideAndRoundUp(len, 2);
    leftSide = arr.slice(0, idx - 1);
    rightSide = arr.slice(idx + 1, len);
    leftSum = calculateSide(leftSide);
    rightSum = calculateSide(rightSide);
  } else {
    idx = len / 2;
    leftSide = arr.slice(0, idx);
    rightSide = arr.slice(idx + 1, len);
    leftSum = calculateSide(leftSide);
    rightSum = calculateSide(rightSide);
  }

  return leftSum === rightSum ? "Balanced" : "Not Balanced";
}

// TODO -- one time approach to calculate size
function balancedNumII(num) {}
balancedNum(77777);

function triangle(row) {
  let chars = row.split("");
  let result = "";
  for (let i = 0; i < chars.length; ++i) {
    if (i < chars.length - 1) {
      result += mergeCell(chars[i], chars[i + 1]);
    }
  }
  return result;
}

function mergeCell(a, b) {
  a = a.toLowerCase();
  b = b.toLowerCase();

  if (a === b) {
    return a;
  } else if ((a === "G" && b === "R") || (a === "R" && b === "G")) {
    return "B";
  } else if ((a === "G" && b === "B") || (a === "B" && b === "G")) {
    return "R";
  } else if ((a === "G" && b === "B") || (a === "B" && b === "G")) {
    return "R";
  }
}

function removeRotten(bagOfFruits) {
  if (!bagOfFruits) return [];
  return bagOfFruits.reduce((acc, val) => {
    const fresh = val.toLowerCase().replace("rotten", "");
    acc.push(fresh);
    return acc;
  }, []);
}

function removeRottenII(arr) {
  return arr ? arr.map((x) => x.replace("rotten", ""), toLowerCase()) : [];
}

function points(games) {
  let totalScore = 0;
  for (let game = 0; i < games.length; ++i) {
    const goals_x = parseInt(games[game][0], 10);
    const goals_y = parseInt(games[game][2], 10);
    if (goals_x === goals_y) {
      totalScore += 1;
    } else if (goals_x > goals_y) {
      totalScore += 3;
    }
  }
  return totalScore;
}

function multiplyAll() {
  return multiplied();
}

function multiplied() {}

function sumOfMinimums(arr) {
  let minTotal = 0;
  for (let i = 0; i < arr.length; ++i) {
    const rowMin = Math.min(...arr[i]);
    minTotal += rowMin;
  }
  return minTotal;
}

function sumOfMinimumsII(arr) {
  return arr.map((x) => Math.min(...x));
}

function isSortedAndHow(array) {
  let isDescending = true;
  let isAscending = true;

  for (let i = 0; i < array.length - 1; ++i) {
    if (array[i] >= array[i + 1]) {
      isAscending = false;
    } else if (array[i] <= array[i + 1]) {
      isDescending = false;
    }
  }

  if (isAscending && !isDescending) {
    return "yes, ascending";
  } else if (isDescending && !isAscending) {
    return "no, descending";
  } else {
    return "no";
  }
}

function alternateCase(s) {
  let charArr = [...s];
  const alternated = charArr.reduce((acc, i) => {
    if (i.toLowerCase() === i) {
      acc += i.toUpperCase();
    } else {
      acc += i.toLowerCase();
    }
    return acc;
  }, "");
  console.log(alternated);
  return alternated;
}

alternateCase("StockHOlm");

function alternateCaseII(s) {
  return s
    .split("")
    .map((x) => {
      return x.toUpperCase() === x ? x.toLoweCase() : x.toUpperCase();
    })
    .join("");
}

function solve(s) {
  let result = [];
  let upperCaseChars = 0;
  let lowerCaseChars = 0;
  let numberTotal = 0;
  let specialChars = 0;
  const chars = [...s];

  for (let i = 0; i < chars.length; ++i) {
    if (chars[i].toUpperCase() === chars[i] && isNaN(parseInt(chars[i]))) {
      upperCaseChars += 1;
    } else if (
      chars[i].toLowerCase() === chars[i] &&
      isNaN(parseInt(chars[i]))
    ) {
      lowerCaseChars += 1;
    } else if (!isNaN(parseInt(chars[i]))) {
      numberTotal += 1;
    } else {
      specialChars += 1;
    }
  }
  result.push(upperCaseChars, lowerCaseChars, numberTotal, specialChars);
  return result;
}

solve("ST*8CKHOLM%[mdsf");

function vaporcode(string) {
  let result = "";
  const vapor = "  ";
  const charArray = string.replace(/\s/g, "").toUpperCase().split("");

  for (let i = 0; i < charArray.length; ++i) {
    if (i == charArray.length) {
      result += charArray[i];
    } else {
      result += charArray[i] + vapor;
    }
  }
  return result;
}

function vaporCode(string) {
  return string
    .toUpperCase()
    .split("")
    .filter((char) => char != " ")
    .map((char) => char + "  ")
    .join("")
    .trim();
}
console.log(vaporCode("GUARDIANS OF GAAALLAAAXXYDX"));
vaporcode("hello guardians of galaxy");

function explode(s) {
  digitArr = s.split("");
  let explosion = digitArr.reduce((acc, d) => {
    const digit = parseInt(d, 10);
    const boom = d.repeat(digit);
    return acc + boom;
  }, "");
}

console.log(3, "3");

function calc(x) {
  charArr = x.split("");
  let sum = 0;

  for (let i = 0; i < charArr.length; ++i) {
    let asciiStr = charArr[i].charCodeAt(0).toString();
    let asciiStr2 = asciiStr.replaceAll("7", "1");
    sum +=
      parseInt(asciiStr[0], 10) +
      parseInt(asciiStr[1], 10) -
      (parseInt(asciiStr2[0], 10) + parseInt(asciiStr2[1], 10));
  }
  console.log(sum);
}
calc("ABC");
