onmessage = workerCheckSquare;
function checkSquareNumber(data) {
  let countSquare = 0;
  for (let i = 0; i < data.length; i++) {
    if (Math.sqrt(data[i]) % 1 === 0) {
      countSquare++;
    }
  }
  return countSquare;
}
function workerCheckSquare(event) {
  if (event.data) {
    let totalSquareCount = checkSquareNumber(event.data.sendBlockData);
    let senbBackData = {
      totalSquareCount: totalSquareCount,
      blockIndex: event.data.blockIndex,
      worker: event.data.worker
    };
    postMessage(senbBackData);
  }
}
