class Node {
  constructor(val, next = null, prev = null) {
    this.val = val;
    this.next = next;
    this.prev = prev;
  }
}

class MyLinkedList {
  constructor() {
    this.head = null;
  }
  get(index) {
    let current = this.head;
    while (current && index > 0) {
      current = current.next;
      index -= 1;
    }
    return current ? current.val : -1;
  }

  addAtHead(val) {
    const newNode = new Node(val, this.head);
    this.head = newNode;
  }
  addAtTail(val) {
    const newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
    } else {
      let node = this.head;
      while (node.next) {
        node = node.next;
      }
      node.next = newNode;
      newNode.prev = node;
    }
  }
  addAtIndex(index, val) {
    if (index < 0) return;

    if (index === 0) {
      this.addAtHead(val);
      return;
    }

    let current = this.head;
    for (let i = 0; current && i < index - 1; i++) {
      current = current.next;
    }

    if (!current) return;

    const newNode = new Node(val, current.next);
    current.next = newNode;
  }
  deleteAtIndex(index) {
    if (index < 0) return;

    if (index === 0) {
      if (this.head) {
        this.head = this.head.next;
      }
      return;
    }

    let current = this.head;
    for (let i = 0; current && i < index - 1; i++) {
      current = current.next;
    }

    if (!current || !current.next) return;

    current.next = current.next.next;
  }
}
