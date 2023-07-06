class Queue {
  constructor() {
    this.data = [];
  }

  enqueue(element) {
    this.data.push(element);
  }

  dequeue() {
    return this.data.shift();
  }

  read() {
    return this.data[0];
  }
}
