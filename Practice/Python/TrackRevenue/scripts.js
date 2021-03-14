class Queue {
  constructor() {
    this.items = [];
  }
  enqueue(element) {
    this.items.push(element);
  }
  dequeue() {
    if (this.isEmpty()) {
      return 'Underflow';
    }
    return this.items.shift();
  }
  isEmpty() {
    return this.items.length === 0;
  }
  size() {
    return this.items.length;
  }
}

const str = 'aabcccdddeeff';
const tempQueue = new Queue();
let char;
let nextChar;
tempQueue.enqueue(str[0]);
for (let i = 0; i <= str.length; i++) {
  char = str[i];
  nextChar = str[i + 1];
  if (char === nextChar) {
    tempQueue.enqueue(char);
  } else {
    const size = tempQueue.size();
    while (!tempQueue.isEmpty()) {
      const char1 = tempQueue.dequeue();
      if (size < 3) {
        console.log(char1);
      }
    }
    tempQueue.enqueue(nextChar);
  }
}
