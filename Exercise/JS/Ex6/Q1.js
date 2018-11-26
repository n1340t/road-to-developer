function outputCount(count) {
  document.getElementById(
    "totalSquares"
  ).innerHTML = `There are ${count} perfect squares`;
}

//JS CODE START
let blockIndex = 9; //start at 9
let blockLength = 1000;
let totalBlock = ARRAY.length / blockLength - 1; //blockIndex start from 0;
function increaseBlockIndex() {
  blockIndex += 1;
  return blockIndex;
}
// Manage worker
window.onload = function() {
  let worker1,
    worker2,
    worker3,
    worker4,
    worker5,
    worker6,
    worker7,
    worker8,
    worker9,
    worker10;

  worker1 = new Worker("Q1worker.js");
  worker1.id = "worker1";

  worker2 = new Worker("Q1worker.js");
  worker2.id = "worker2";

  worker3 = new Worker("Q1worker.js");
  worker3.id = "worker3";

  worker4 = new Worker("Q1worker.js");
  worker4.id = "worker4";

  worker5 = new Worker("Q1worker.js");
  worker5.id = "worker5";

  worker6 = new Worker("Q1worker.js");
  worker6.id = "worker6";

  worker7 = new Worker("Q1worker.js");
  worker7.id = "worker7";

  worker8 = new Worker("Q1worker.js");
  worker8.id = "worker8";

  worker9 = new Worker("Q1worker.js");
  worker9.id = "worker9";

  worker10 = new Worker("Q1worker.js");
  worker10.id = "worker10";

  let workerArray = [];
  let resultCount = 0;
  workerArray.push(
    worker1,
    worker2,
    worker3,
    worker4,
    worker5,
    worker6,
    worker7,
    worker8,
    worker9,
    worker10
  );
  function getBlockData(blockIndex) {
    return ARRAY.slice(
      blockIndex * blockLength,
      (blockIndex + 1) * blockLength
    );
  }
  function runWorker(idx) {
    workerArray[idx].onmessage = function(event) {
      if (event.data) {
        resultCount += event.data.totalSquareCount;
        // console.log(resultCount);
        if (blockIndex < totalBlock) {
          let nextBlockIndex = increaseBlockIndex();
          let sendBlockData = getBlockData(nextBlockIndex);
          workerArray[idx].postMessage({
            blockIndex: nextBlockIndex,
            sendBlockData: sendBlockData,
            worker: idx
          });
        } else {
          workerArray[idx].terminate();
          outputCount(resultCount);
        }
      } else {
        workerArray[idx].terminate();
      }
    };
  }
  // Initialize onmessage
  for (let i = 0; i < workerArray.length; ++i) {
    runWorker(i);
  }

  // postMessage
  for (let i = 0; i < workerArray.length; i++) {
    let blockData = getBlockData(i);
    workerArray[i].postMessage({
      blockIndex: i,
      sendBlockData: blockData,
      worker: i
    });
  }
};
