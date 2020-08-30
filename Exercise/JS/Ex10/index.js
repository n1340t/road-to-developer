// arr is 2D array 6 x6
const testArr = [
  [-9, -9, -9, 1, 1, 1],
  [0, -9, 0, 4, 3, 2],
  [-9, -9, -9, 1, 2, 3],
  [0, 0, 8, 6, 6, 0],
  [0, 0, 0, -2, 0, 0],
  [0, 0, 1, 2, 4, 0]
];
function hourglassSum(arr) {
  const ARR_WIDTH = arr.length;
  const SUB_ARR_WIDTH = arr.length - 1;
  const newArr = [];
  for (let j = 0; j < ARR_WIDTH; j++) {
    for (let i = 0; i < ARR_WIDTH; i++) {
      newArr.push(arr[j][i]);
    }
  }
  // Finding max with all value less than 0
  let max = 7 * -9;
  for (let row = 1; row < SUB_ARR_WIDTH; row++) {
    for (let col = 1; col < SUB_ARR_WIDTH; col++) {
      let sum = newArr[row * ARR_WIDTH + col];
      for (let x = col - 1; x <= col + 1; x++) {
        sum += newArr[(row - 1) * ARR_WIDTH + x];
        sum += newArr[(row + 1) * ARR_WIDTH + x];
      }
      if (max < sum) {
        max = sum;
      }
    }
  }
  return max;
}

hourglassSum(testArr);
