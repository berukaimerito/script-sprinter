"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.noBoringZeros = void 0;
function noBoringZeros(n) {
    var digitString = n.toString();
    var digitArr = [];
    for (var i = 0; i < digitString.length - 1; ++i) {
        if (digitString[i] === "0" && digitString[i + 1] != "0")
            digitArr.push(digitArr[i], digitArr[i + 1]);
    }
    console.log(digitArr);
    return 0;
}
exports.noBoringZeros = noBoringZeros;
noBoringZeros(34923490423000000);
