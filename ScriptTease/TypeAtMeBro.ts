export function noBoringZeros(n: number): number {
  let digitString: string = n.toString();
  let digitArr: Array<String> = [];

  for (let i = 0; i < digitString.length - 1; ++i) {
    if (digitString[i] === "0" && digitString[i + 1] != "0") {
      digitArr.push(digitArr[i], digitArr[i + 1]);
    }
  }
  console.log(digitArr);
  return 0;
}

noBoringZeros(34923490423000000);
